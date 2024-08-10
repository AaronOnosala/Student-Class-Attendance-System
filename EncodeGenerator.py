# importing libraries
import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

# This sets up the connection to the Firebase Realtime Database and Firebase Storage.
cred = credentials.Certificate("studentclassattendance-654ee-firebase-adminsdk-q2abk-0bbb21d14a.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://studentclassattendance-654ee-default-rtdb.firebaseio.com/",
    'storageBucket': "studentclassattendance-654ee.appspot.com"
})

# Importing Student images to be stored in as data with corresponding student IDs.
folderPath = 'images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentIds = []
#Reading each image using OpenCV, extracts the student ID from the filename, uploads the image to Firebase Storage, and prints the list of student IDs.
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


    #print(path)
    #print(os.path.splitext(path)[0])
print(studentIds)
# Function to encode student images
def findEncoding(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncoding(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding completed Successfully")

# Saving the encoded face data along with student IDs
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
