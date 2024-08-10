# importing libraries
import pickle
import numpy as np
import cv2
import cvzone
import os
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

# Initializing the Firebase app with credentials and configure it with the database and storage URLs.
# This sets up the connection to the Firebase Realtime Database and Firebase Storage
cred = credentials.Certificate("studentclassattendance-654ee-firebase-adminsdk-q2abk-0bbb21d14a.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://studentclassattendance-654ee-default-rtdb.firebaseio.com/",
    'storageBucket': "studentclassattendance-654ee.appspot.com"
})

#creating a reference to the Firebase Storage bucket, which will be used to interact with the storage service
bucket = storage.bucket()

#These lines initialize a video capture object using OpenCV, setting the width and height of the cap
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#This line loads a background image from a file
imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list iterration
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
#print(len(imgModeList))

# Load the encoding file
# These lines load the previously saved encoding file using pickle. The file contains face encodings and corresponding student IDs.
print("Loading Encoding File ...")
file = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
#print(studentIds)
print("Encode File Loaded Successful")

# These lines initialize variables used for tracking the mode type, a counter, the student ID, and an image of the student
modeType = 0
counter = 0
id = -1
imgStudent = []

# This initiates an infinite loop where the main processing of the captured video frames takes place
while True:
    success, img = cap.read()
# This section resizes the captured frame (img) to 25% of its original size and converts it to RGB color format.
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#  the face locations and encodings are obtained using the face_recognition library on the resized and RGB converted frame
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
# These lines update the background image (imgBackground) with the original captured frame (img) and the mode image based on the current modeType
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.compare_faces(encodeListKnown, encodeFace)
           # print("matches", matches)
           # print("faceDis", faceDis)

            matchIndex = np.argmin(faceDis)
            #print("Match Index", matchIndex)

            if matches[matchIndex]:
                # Face recognized
                #print("Known Face Detected")
                #print(studentIds[matchIndex])
                y1,x2 , y2, x1 = faceLoc
                y1,x2 , y2, x1 = y1*4,x2*4 , y2*4, x1*4
                bbox = 55+x1, 162+y1, x2-x1, y2-y1
                imgBackground = cvzone.cornerRect(imgBackground,bbox, rt = 0)
                id = studentIds[matchIndex]
                if counter == 0:
                    # Loading mode
                    #cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

     # If a face is recognized
        if counter != 0:

            if counter == 1:
                #Get the data
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)

                #Get the Image from the storage
                blob = bucket.get_blob(f'images/{id}.jpg')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                #Update attendance
                datetimeObject = datetime.strptime(studentInfo['Last_Attendance_time'],
                                                  "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now()-datetimeObject).total_seconds()
                print(secondsElapsed)
                if secondsElapsed > 10:
                    ref = db.reference(f'Students/{id}')
                    studentInfo['Total_Attendance'] +=1
                    ref.child('Total_Attendance').set(studentInfo['Total_Attendance'])
                    ref.child('Last_Attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
            if modeType != 3:
                # Displaying information on the background image
                # (Details such as total attendance, course, student ID, etc.)
                # Updating the counter and mode type
                # Resetting the counter and modeType after 20 frames
                if 10 < counter < 20:
                    modeType = 2
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
                if counter <= 10:
                    cv2.putText(imgBackground,str(studentInfo['Total_Attendance']),(861,125),
                                cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                    cv2.putText(imgBackground,str(studentInfo['Course']),(1006,550),
                                cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv2.putText(imgBackground,str(id),(1006,493),
                                cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv2.putText(imgBackground,str(studentInfo['Standing']),(910,625),
                                cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    cv2.putText(imgBackground,str(studentInfo['Year']),(1025,625),
                                cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    cv2.putText(imgBackground,str(studentInfo['Semester']),(1125,625),
                               cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    (w, h), _ = cv2.getTextSize(studentInfo['Name'], cv2.FONT_HERSHEY_COMPLEX,1,1)
                    offset = (414-w)//2
                    cv2.putText(imgBackground, str(studentInfo['Name']),(808 + offset,445),
                               cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50),1)
                    imgBackground[175:175+216, 909:909+216] = imgStudent

                counter += 1
                if counter >= 20:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    else:
        # If no face is detected, reset modeType and counter
        modeType = 0
        counter = 0


# Display the updated background image
    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)


