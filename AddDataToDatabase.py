# Importing necessary libraries from Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

# Initialize connection to Firebase Realtime Database
cred = credentials.Certificate("studentclassattendance-654ee-firebase-adminsdk-q2abk-0bbb21d14a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://studentclassattendance-654ee-default-rtdb.firebaseio.com/"
})

# Reference to the 'Students' node in the Firebase Realtime Database
ref = db.reference('Students')

# Student data to be added to the database
data = {
    "01": {
        "Name": "Mr. Henry Semakula",
        "Course": "Supervisor",
        "Semester": 0,
        "Standing": "A",
        "Year": 2023,
        "Total_Attendance": 0,
        "Last_Attendance_time": "2023-12-18 10:45:00"
    },
    "1234": {
        "Name": "Shongo Onosala Aaron",
        "Course": "BSc AI & ML",
        "Semester": 4,
        "Standing": "A",
        "Year": 2023,
        "Total_Attendance": 0,
        "Last_Attendance_time": "2023-12-18 10:45:00"
    }
}

# Adding the student data to the database
for key, value in data.items():
    ref.child(key).set(value)
