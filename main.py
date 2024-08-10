# Import necessary libraries
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

# Initialize the Firebase app with credentials and configure the database and storage URLs
# This sets up the connection to the Firebase Realtime Database and Firebase Storage
cred = credentials.Certificate("studentclassattendance-654ee-firebase-adminsdk-q2abk-0bbb21d14a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://studentclassattendance-654ee-default-rtdb.firebaseio.com/",
    'storageBucket': "studentclassattendance-654ee.appspot.com"
})

# Create a reference to the Firebase Storage bucket for interaction with the storage service
bucket = storage.bucket()

# Initialize a video capture object using OpenCV, setting the width and height of the capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the background image from a file
imgBackground = cv2.imread('Resources/background.png')

# Import the mode images into a list for iteration
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Load the encoding file
# This file contains face encodings and corresponding student IDs
print("Loading Encoding File ...")
with open('EncodeFile.p', 'rb') as file:
    encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encoding File Loaded Successfully")

# Initialize variables for tracking mode type, counter, student ID, and student image
modeType = 0
counter = 0
id = -1
imgStudent = []

# Main processing loop for captured video frames
while True:
    success, img = cap.read()
    # Resize the captured frame to 25% of its original size and convert to RGB color format
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Obtain face locations and encodings using the face_recognition library
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # Update the background image with the captured frame and mode image based on the current modeType
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                # Face recognized
                y1, x2, y2, x1 = [coordinate * 4 for coordinate in faceLoc]
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]
                if counter == 0:
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

    # If a face is recognized
    if counter != 0:
        if counter == 1:
            # Get the student data from the database
            studentInfo = db.reference(f'Students/{id}').get()
            print(studentInfo)

            # Get the student image from storage
            blob = bucket.get_blob(f'images/{id}.jpg')
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            imgStudent = cv2.imdecode(array, cv2.IMREAD_COLOR)

            # Update attendance if the elapsed time since the last attendance is more than 10 seconds
            datetimeObject = datetime.strptime(studentInfo['Last_Attendance_time'], "%Y-%m-%d %H:%M:%S")
            secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
            if secondsElapsed > 10:
                ref = db.reference(f'Students/{id}')
                studentInfo['Total_Attendance'] += 1
                ref.child('Total_Attendance').set(studentInfo['Total_Attendance'])
                ref.child('Last_Attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                modeType = 3
                counter = 0
                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

        if modeType != 3:
            # Display student information on the background image
            if 10 < counter < 20:
                modeType = 2
                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
            if counter <= 10:
                cv2.putText(imgBackground, str(studentInfo['Total_Attendance']), (861, 125),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(studentInfo['Course']), (1006, 550),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(id), (1006, 493),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(studentInfo['Standing']), (910, 625),
                            cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgBackground, str(studentInfo['Year']), (1025, 625),
                            cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgBackground, str(studentInfo['Semester']), (1125, 625),
                            cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                (w, h), _ = cv2.getTextSize(studentInfo['Name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                offset = (414 - w) // 2
                cv2.putText(imgBackground, str(studentInfo['Name']), (808 + offset, 445),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)
                imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

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
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
