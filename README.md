# Student-Class-Attendance-System

# INTRODUCTION 
 
These days, technology seeks to convey a large amount of knowledge-based technical advancements. Deep Learning is an intriguing subject that allows a machine to educate itself using datasets as input and then deliver an acceptable output during testing using various learning techniques. Nowadays, attendance is seen as a critical aspect for both students and teachers in educational institutions. With the progress of deep learning technology, the computer can now automatically recognise the students' attendance performance and keep a record of it. In general, a student's attendance system can be kept in two different ways, namely,   
 + __Manual Attendance System (MAS)__ 
Manual Student Attendance Management is a method in which a teacher in charge of a particular topic must manually call the students' names and record their attendance. Manual attendance may be viewed as a time- consuming process, and it is possible that the instructor will miss someone, or that pupils will respond to the absence of their friends many times. As a result, a difficulty occurs. when we think about the traditional process of taking attendance in the classroom.   
 + __Automated Attendance System (AAS)__ 
Our ongoing research endeavors involve the comprehensive investigation and development of an Automated Attendance System (AAS), a sophisticated technological solution designed to streamline and enhance the efficiency of attendance tracking processes. The foundation of our research lies in the exploration and analysis of the Automated Attendance System, with a focus on leveraging advanced technological methodologies to create a robust and user-friendly system that can significantly improve the accuracy and reliability of attendance management in various organizational settings. 
## 1.1 Background    
In Ugandan police have confirmed that Chinese telecommunications giant Huawei is rolling out a massive surveillance system that uses facial recognition and other artificial intelligence software to fight crime in the country. In 2023, the city of Kampala at ISBAT University, Miss Nidhi Soni designs a recognition system for Ugandan Sign Language gestures by building a convolutional neural network that accurately predicts sign language gestures (Soni, 2023).    In South Africa, in 2016, the city of Johannesburg announced it was rolling out smart CCTV cameras complete with automatic number plate recognition and facial recognition.   
As of late 2017, China has deployed facial recognition and artificial intelligence technology in Xinjiang. Reporters visiting the region found surveillance cameras installed every hundred meters or so in several cities, as well as facial recognition checkpoints at areas like gas stations, shopping centers, and mosque entrances. In 2020, China provided a grant to develop facial recognition technology to identify people wearing surgical or dust masks by matching solely to eyes and foreheads.   
In 2019, USA researchers reported that Immigration and Customs Enforcement uses facial recognition software against state driver's license databases, including for some states that provide licenses to undocumented immigrants.  

## 1.2 Problem Statement     

The existing manual attendance system in educational organisations is cumbersome, especially with a large number of students. It involves time-consuming processes like maintaining logbooks and records. The project aims to address these concerns by introducing a face detection and recognition system.   
This project is motivated by the inefficiency of current attendance methods, such as clickers, ID card swapping, and manual name recording. It seeks to develop a system that can automatically detect and recognise faces in a classroom. This system will enhance classroom control during lectures and ensure accurate attendance records.   

## 1.3 Objectives of the Study 
### 1.3.1 Main Objective    

To develop a web-based application that will enable system to perform real-time face recognition to facilitate classroom control and attendance. 

### 1.3.2 Specific Objectives  

#### i.	To collect student’s images for face recognition 
#### ii.	To analyze, encode student’s images for real-time face recognition model 
#### iii.	To train a machine learning model for real-time recognition system 
#### iv.	To build a web-based application for student class attendance system 
 
 
## 1.4 Research Questions 

i.	What methods and ethical considerations should be employed in collecting and managing students' images to ensure privacy and data security in the context of face recognition for a class attendance system? 

ii.	How can facial image encoding techniques be optimized and standardized to enhance the accuracy and efficiency of a real-time face recognition model for monitoring student attendance? 

iii.	What are the most effective machine learning algorithms and training strategies for developing a robust real-time face recognition system capable of accurately identifying students in various environmental conditions within an educational setting?   

iv.	What design principles and user experience factors should be taken into account when developing a web-based application for a student class attendance system that incorporates real-time face recognition, ensuring accessibility, usability, and overall effectiveness in an educational environment?   

## 1.5 Scope of Study

The proposal will target educational institutions in Uganda capable of adopting such technology, ensuring that they have the necessary infrastructure to support face recognition systems.  

## 1.6 Significance of the Study    

This project addresses several key issues that schools and universities face when managing attendance records. By reducing administrative workload and attendance fraud, the system streamlines processes and saves time for both students and staff. Enhanced security features ensure the integrity of attendance records, while providing real-time monitoring and flexibility for students and staff. Finally, by improving engagement, the system can help boost attendance rates and foster a more positive learning environment.   
    
 

# LITERATURE REVIEW 

## 2.1 Introduction 

Every institution that depends on people must account for its employees as a first step in the modern-day.  As a result, creating and maintaining a suitable management system costs the different organizations a substantial sum of money. In many countries, government organizations and educational institutions keep track of attendance using paper-based methods.  For example, to maintain track of each student's attendance, it takes time to call out their name at the beginning of the course. False signs, names missing from spreadsheets, manually inputting data into systems, and the possibility of proxy attendance are further problems (Abdalkarim, 2022). Such techniques have a few problems that have grown over time. To track attendance, it is crucial to swap out these outdated practices for modern ones. As a result, a lot of work and research has been done in this area using current technologies. Especially, automatic recognition of a particular individual based on distinguishing characteristics such as QR code, ID and password, face recognition, fingerprint recognition is of interest to researcher. 2.2 Use of Computer Vision in Student Class Attendance System 
Computer Vision is a field of artificial intelligence (AI) enabling computers to derive information from images, videos and other inputs. 

## 2.3 Benefits of Using Computer Vision In Student Class Attendance System 

Implementing computer vision in a student class attendance system brings forth a myriad of benefits that enhance efficiency and accuracy. One significant advantage is the automation of the attendance tracking process. Traditional methods, such as manual roll calls or sign-in sheets, can be time-consuming and prone to errors. Computer vision technology allows for the seamless and automatic recognition of students as they enter the classroom, eliminating the need for manual intervention. This not only saves valuable class time but also reduces the likelihood of errors in attendance records. Furthermore, computer vision enhances security and prevents proxy attendance. By utilizing facial recognition, the system can accurately identify each student, making it nearly impossible for someone else to impersonate them. This not only ensures the integrity of attendance records but also fosters a more secure and controlled learning environment. Additionally, the real-time nature of computer vision enables instant monitoring and alerts, allowing educators to address attendance issues promptly. In the realm of data analysis, computer vision contributes to valuable insights that can aid in improving educational outcomes. By collecting and analyzing attendance data over time, educators and administrators can identify patterns, trends, and correlations. This information can be utilized to tailor teaching strategies, identify at-risk students, and implement targeted interventions. Overall, the incorporation of computer vision in student class attendance systems not only streamlines administrative processes but also opens the door to data-driven decision-making for educational improvement. 

## 2.4 Digitalizing the Old Approach 

Traditional student attendance involves all the roll-calling issues and takes a lot of time for students and teachers to conduct departmental sessions. The procedure is lengthy and takes many instructors' and students' time. Substituting the conventional procedure, teachers had to call each student's name in class and note the attendance when the student answered.  It offers a more straightforward and quicker approach to monitoring attendance.  Instructors will no longer require a paper sheet to mark student attendance in their proposed system.  They can construct attendance records by obtaining the necessary information from the database, making the entire procedure paperless. Another Research used mobile devices in the attendance management system were developed and put into practice (Abdalkarim, 2022).  A mobile-based attendance management program for Android systems was developed using VB.NET and SQL Server.  This project allows for the maintenance of student attendance, calculating attendance grades, and creating a report.  Five components make up the system:  admin, registration, student, SMS, and an Android component.  Students can use the android part to send messages to the system informing lecturers of their absence. Parents can also get SMS notifications on students' behaviour. 

### 2.4.1 Face Recognition Based Systems  

The idea of finding human faces in referenced photographs or videos is known as face detection. A face recognition system is a type of tech that can compare face images from a video or photograph to a database of known and unknown faces. The Face, Recognition-based Attendance Management System, was developed by Smitha to develop an organized classroom attendance system using face recognition methods.  Through facial ID, the system can record involvement. Through a camera, it finds faces and then recognizes them. The system is split into two parts:  facial recognition and detection.  Using the Local Binary Pattern Histogram (LBPH), the system will identify faces of students in the live-streamed video from the class and, if the recognized face is found in the database, will mark their attendance. Face recognition technology was also discussed by Varadharajan et al. in their paper. (Abdalkarim, 2022) They placed a camera inside the class, using this technique to take pictures.  The attendance is registered as a present after faces are found and identified in the database. Parents are informed of a student's disappearance if their attendance is noted as absent. The research by Chandramouli et al, wherein they utilized NVIDIA's Jetson Nano, is one of many that tries to modernize how attendance is managed in a certain method and even the parameters for time management. The device is set in the class, where the names and photos of the students are held. Open CV is used to obtain the photos. The processor board would be NVIDIA Jetson Nano's Developer kit. A Haar classifier is used to identify faces once the extraction has been processed.  They subsequently identified with the aid of the LBPH Algorithm. An Excel spreadsheet is generated and refreshed hourly with data from the appropriate class teacher. Ofualagba et al. Suggested a system named Automated Student Attendance Management System Using Face Recognition that highlights the use of Cloud Computing (CC) technological concepts to boost the performance of face identification methods.  The FACECUBE system, which is suggested here, uses facial recognition to take attendance.  The system provides students, instructors, and administrators with online features. However, putting this system together involves several steps, including purchasing new hardware and software. Susanto et al. were attempted to perform a slightly different type of research concerning the detection of face recognition of lecturers who are present in the application system via an Android device.  They make a connection with face recognition detection and, after that, save it to the database that was used as information about the presence of lecturers who are teaching.  The local binary pattern histogram (LBPH) classifier approach, which may be used as a strategy in the attendance system of lecturers to be more efficient and productive, is used to evaluate the facial recognition system. An open-source, generic application for assessing daily attendance using face recognition and making use of the Android system was proposed in the Hava et al. study. Almost every institution may readily get it at no cost.  With this suggested solution, Google Sheets are automatically created and available to the institution with no effort.  The system involves facial identification and recognition algorithms to identify individual students and record their participation. Prangchumpol mentions in his research, "Face Recognition for Attendance Management System Using Multiple Sensors," that his performance still falls short when it comes to accurately identify students' faces and that he is still unable to confirm or rectify the data when a mistake occurs in class. Therefore, he seeks to improve the efficiency of the face recognition-based attendant system and make the system's principles simple for students to understand. This sort of validation aims to discover how to detect faces utilizing the Android Face Recognition with Deep Learning approach.  The database is linked to the web server using cloud storage. Alburaiki et al. developed a methodology that solved three key elements:  First, using mobile phone cameras and automatically recognizing and analyzing faces. The second is a machine-learning-based facial recognition API. Lastly, maps API. The outcome demonstrates that face recognition has attained high accuracy in identifying students' faces even in unfavorable conditions.  The system displayed practical examples of responses by marking the student's attendance after identifying the student's face and location, as well as the lecturer has the option to access a report of submitted attendance. A portable attendance system that could be accessed from any location at any time inspired Salac's study. Without carrying paper and PCs, the lecturer may simply verify attendance using an Android smartphone.  The students' Android phones make it simple for them to check their attendance information. Additionally, SMS technology is employed to ensure the safety of the students and to notify families about their child's attendance.  Face recognition is also used to establish a proper attendance record.  A particular student's face is detected and recorded as present in the database using the Android device's camera. When necessary, attendance reports could also be formed. 

## 2.5 Related Works 
 + __A Web-Based Real Time Recognition System For Sign Language Gestures__
Nidhi Soni, this system is used for creating an effective and efficient translation system that can provide dynamic communication between people who use spoken language and people who use sign language. This system was built on convolutional neural network that accurately predicts sign language gestures. 

 + __Web Based Student Information Management__
 S.R.Bharamagoudar et al., this paper assist in automating the existing manual system. It can be monitored and controlled remotely. This paper provides accurate information always. All years together gathered information can be saved and can be accessed at any time. The purpose is to design a college website which contains up to date information of the college. That should improve efficiency of college record management.

 + __Attendance Management System__
 G.Gangagowri et al., this system is used Way to SMS software. This software is used to send SMS easily to their parent’s. This system can store their data about the students and those cares absent student details. It is an efficient method to store the attendance in the Web Site rather than wasting the paper. It also updates the student report directly on the server reducing the faculty’s time on logging from the computer.

 + __Online Student Attendance System__
 P. N. Garad et al, in this project, we gave access to three users i.e. Admin, Student, Others. This project is based on client-server. Here, the serve is Tomcat and client is JSP. In this project teachers or the admin will be filling attendance and sending message to the student who is absent. They will have privilege to fill attendance form, update attendance form, send message to the guardian’s account whose child is absent, also those attendance is less than 75%, and they also have privilege to send message to the students whose fees are pending. He staff can also view the message whenever they want and also can modify the details of students. Parents have privilege to view attendance and to view message sent by the teacher. Students also have their account with the privilege to view message sent by the subject teacher and to view the attendance (Kano, 2021).

 + __Web Based Coaching Institute Management System__
 Mayuri Kamble et al, “Coaching Institute Management System” software developed for an institute has been designed to achieve maximum efficiency and reduce the time taken to handle the storing activity. It is designed to replace an existing manual record system thereby reducing time taken for calculations and for storing data (Kano, 2021). The system is strong enough to withstand regressive daily operations under conditions where the database is maintained and cleared over a certain time of span. The implementation of the system in the organization will considerably reduce data entry, time and also provide readily calculated reports.

 + __Classroom Attendance Application__
 Pranjul Khare1 et al, the scope of the project is the system on which the software is installed, i.e. the project is developed as an ANDROID application, and it will work for a particular institute. Android is a mobile operating system (OS) based on the Linux kernel and currently developed by Google with a user interface based on direct manipulation. RAD approaches to software development have put less emphasis on planning tasks and more emphasis on development. It has revealed that an online system for recording and reporting students ’attendances is indeed a needed application in order to make the process more efficient and time-saving where more than 70% of the sample group agreed to that matter.

# MATERIALS AND METHODS 

## 3.1 Dataset Collection 

The dataset consists of images of students as passport photo of size 216x216, as there is no publicly available dataset for Student Class Attendance System and we can not use any random passport photo, a dataset had to be created from scratch. The dataset for the project consisted of two sample images taken for each student of Student Class Attendance System from various lighting, angles and backgrounds to ensure accuracy during the training process. Below are some image mode among the collected dataset. 
  
__Figure 1: Background image of Student Attendance System__
![background](https://github.com/user-attachments/assets/eecca80a-aa83-4489-850f-ab81dd05a16a)

__Figure 2: Modes 1 & 2 of the Student Class Attendance System respectively active for displaying and recording student attendance information details.__

![1](https://github.com/user-attachments/assets/d2b34c95-e0ea-4ec9-aa66-4dfee544892e)   ![2](https://github.com/user-attachments/assets/5a6b902d-de70-476e-b28a-e2b7e2711a9e)

  
__Figure 3: Modes 3 & 4 of the Student Class Attendance System respectively mark and already marked for taken records feedback__
![3](https://github.com/user-attachments/assets/b60c9736-1b67-48e6-86ea-d772f4ab4f5e)    ![4](https://github.com/user-attachments/assets/09ee2adc-922f-4181-a57c-859a5cb40a1a)

## 3.2 Requirement Analysis 

The requirements gathered from users was categorized into functional and non-functional requirements. 
__Table 3: Table of Functional Requirements__
<img width="951" alt="Screenshot 2024-08-10 at 20 12 51" src="https://github.com/user-attachments/assets/6eb9df8d-8654-44be-bc46-cdbffc7f4a5e">

__Table 4: Table of Non-Functional Requirements__
<img width="941" alt="Screenshot 2024-08-10 at 20 15 15" src="https://github.com/user-attachments/assets/30abf86a-c8d6-45d8-96e1-17c40918aabe">
 
## 3.3 Data Preprocessing  
Data preprocessing was a crucial step in building a machine learning model for Student face recognition. Some of the data preprocessing steps used in this project are as follows: 
### 3.3.1 Data Collection and Labeling 

A diverse dataset consisting of 2 sample images of each student were collected from different orientations and lighting. These images were then preprocessed by imposing them on a white background and ensuring that all of the images were of equal length, width and that no part of the face was cut out of frame during data collection. Each face was then Encoded accordingly. 

### 3.3.2 Data Cleaning 

This was done to remove noise in the images from the dataset, as well as parts of images that were unnecessary. 3.3.3 Feature Extraction 
The relevant features from the input data were extracted since it is image-based student class attendance system. Afterwards, techniques like face shape recognition were used to extract meaningful features using the cvzone library, especially the cvzone.cornerRect. 
## 3.4 Development of the System 
### 3.4.1 Development Life Cycle of the Proposed System 

The Real-time student class attendance system went through the following steps as the development of the system. 
	I. __Requirements Analysis__
The user and target groups were identified, as well as the scope of the project was defined. The objectives of the project were laid out. All the requirements that would be necessary during the project was identified. 
	II.__Data Collection__
A dataset consisting of two sample images of size 216x216 were collected for face recognition with each face having student details. III. 	Data Preparation 
The raw data of images was preprocessed and cleaned and ensured that they all are relatively the same size so that they could then be passed into the face recognition for training. 
        IV. __Algorithm Selection__
Research was done into the different algorithms that can be used for the Student Class Attendance system such as CNN and Vision Transformers among other relevant Image Detection techniques, and finally, the conclusion to use the face recognition algorithm was reached. 
	V. __Model Training__
Training the model was performed on the data collected to come up with a well-trained model. 
In this case, face_recognition.face_encodings were used to train the model. 
	VI. __Model Testing__ 
The model was tested by using the trained model as the classifier and using different libraries to make the prediction in real time with a user placing their faces in front of the camera to yield a prediction of the faces that were being detected. 
      VII. __User Interface Development__ 
The user interface is a simple window that opens with the use of opencv. When this window is launched, the user is required to place their face in front of the window to allow the model to capture and detect the face shape. 

### 3.4.2 Tools and Technologies used for Software Development 

For the back end, Python was the main language that was used for developing the system. 
Additionally, some Python IDEs were also used during the duration of this project. 
 i. __Python__
Python was the general-purpose programming language that was used throughout the project; from the process of collecting the dataset, to training and then testing the model. 
 ii. __PyCharm__ 
Pycharm is an opensource Interactive, Development Environment (IDE) that was used to create code for the project. 
Some of the crucial libraries that were used during the development of the project include; 
1. __Cv2 (OpenCV)__
In this project, this library was used for computer vision for image and video processing. It was used for Face Data Collection where it was used to capture real-time video frames from a camera to collect data for the student class attendance faces and save the captured frames as images for further processing and building the dataset. The library is also used for data preprocessing for tasks such as resizing, normalization, and filtering, to prepare the images for training the machine learning model. Additionally, it is also used for face detection for detecting and tracking the face or specific regions of interest in the video frames. It was also used to implement real-time face recognition using the trained machine learning model in conjunction with cv2, also for capturing frames from the camera, preprocess them, and feed them into the model to obtain real-time predictions. It is also used to create a user interface to display the video feed from the camera and overlay recognition results on the video stream in real-time (Soni, 2023). Finally, cv2 is used to visualize the results of the face recognition system during testing and evaluation and also overlay predicted labels or bounding boxes on the input video frames for analysis. 

2. __Cvzone__
In this project, cvzone, especially the cvzone.cornerRect module was utilized to perform face tracking and detection tasks. The cornerRect class provided by cvzone helped in accurately detecting and tracking faces in real-time from video frames. This library also supports Realtime Face Detection where one can Implement real-time face tracking and detection using cvzone.cornerRect to capture and process video frames from the camera feed. This real-time detection is essential for recognizing student faces on the fly (Soni, 2023). Another significant use of this library is for Face Segmentation where one can utilize the FaceDetector class to segment and extract the face regions from the video frames which is a crucial step in isolating the face from the rest of the image for more accurate recognition. Furthermore, the cvzone.ClassificationModule in the cvzone library provides a Classifier class that can be used for training and utilizing a classification model for recognizing different classes or categories (British Journal of Computer, 2022). The Classifier can be used to train a machine learning model to recognize the different student face shapes. It can be used for Data Preparation to prepare the dataset of Student face shapes, including images or features representing each faces and their corresponding labels (class or category names). It can also be used to Train the Classifier by creating an instance of the Classifier class and specify the parameters for the classification model (e.g., the type of model, hyperparameters). 

3. __Numpy__
NumPy is a fundamental library in Python that plays a crucial role in the development of Student Class Attendance systems. In Student Class Attendance systems, the representation of images as arrays was essential for efficient processing, and NumPy excels in handling multidimensional arrays with its powerful array manipulation capabilities. Face images can be represented as NumPy arrays, where each pixel's intensity values are stored in a structured manner. This allowed us to perform various operations, such as resizing, cropping, and normalization, easily and efficiently. Additionally, NumPy provides mathematical functions that are instrumental in implementing algorithms for facial feature extraction and analysis. Furthermore, NumPy's array broadcasting feature is particularly beneficial in the context of Student face recognition. It enables the efficient application of operations on arrays of different shapes and sizes without the need for explicit looping, which significantly enhance the performance of our student face recognition algorithm. The ability to perform element-wise operations on entire arrays simplifies the implementation of complex mathematical computations involved in facial feature matching and comparison. Overall, NumPy's versatility and efficiency made it a cornerstone in the development of our robust and high-performance student class attendance systems. 
 
 
# RESULTS AND DISCUSSIONS 
## 4.1 Results 

The system can be accessed by running the python file that will open the webcam of the device. In order to perform student face recognition, the user must place his/her face in front of the webcam and allow the system to recognize and classify the student face for taking attendance in real-time. 

__Figure 4: Interface when making a prediction for student attendance system__
<img width="984" alt="Screenshot 2024-08-10 at 20 24 15" src="https://github.com/user-attachments/assets/0367f044-f6df-4c32-b0f2-164c05b572ed">

<img width="1003" alt="Screenshot 2024-08-10 at 20 25 41" src="https://github.com/user-attachments/assets/1e56a9fd-dbee-4276-8c26-92a85a296b96">

<img width="1022" alt="Screenshot 2024-08-10 at 20 25 55" src="https://github.com/user-attachments/assets/9ebcc7cd-6db3-44ed-881e-21eece571be8">

<img width="990" alt="Screenshot 2024-08-10 at 20 26 11" src="https://github.com/user-attachments/assets/5d68894a-e19e-46e3-87b7-3fc2859261ae">

## 4.2 Usability of Web Based Student Class Attendance System Using Artificial Intelligence   

People who have used the system so far have found the system to be responsive and giving an accurate prediction most of the times. The system is easy to use and does not require the user to fill in any extra unnecessary information which increases the ease of use. The user is only required to place the face in front of the camera at a relative distance to obtain a prediction.

## 4.2.1 System Validation 

The system validation was done with the aim of seeing how applicable it would be in the market for doing Student Class Attendance System. The project was subjected to both unit testing and system testing. In the unit testing, each aspect of the system was tested individually to see how it worked and for the system testing, the entire system was tested as a whole (Soni, 2023). The image classification file should load as required without any very long pauses. When used, the system should be able to detect face when placed in front of the camera and then make predictions from the system that should be as accurate as possible. The system should not freeze in the middle of predictions. It was found that the system met all the above requirements. 

## 4.2.2 User Acceptance 

The system was tried by both registered and non-registered students. It was found to be an effective tool that reduces the complexity for both student management and student attendance records. 

### 4.2.3 Model Evaluation 

The main metrics that were used to evaluate the model were Accuracy, Confusion Matrix, Precision, based on Euclidean distance. Model evaluation allows one to measure the effectiveness and accuracy of the trained model. It provides insights into how well the model is generalizing to unseen data and how it is performing on the task it was designed for. When experimenting with multiple model architectures or hyperparameters, evaluation helps you choose the best-performing model for deployment. You can compare different models based on their evaluation metrics and select the one with the highest accuracy or the best trade-off between precision and recall, depending on the specific application. Overfitting occurs when a model performs well on the training data but poorly on unseen data. Evaluation helps you detect overfitting by examining the difference in performance between the training set and the test set. If there is a significant drop in performance on the test set compared to the training set, it indicates overfitting. Evaluation can help you understand the model's strengths and weaknesses. For example, analyzing the confusion matrix can reveal which classes the model is struggling to recognize correctly, allowing you to focus on improving performance in those areas. 

## 4.3 Discussion 

During the course of this project, findings have shown that there is a keen interest within the community to take up a real time student class attendance system that will allow for accessibility, educational institutes to adopt the cutting-edge technology of student class attendance system using artificial intelligence (British Journal of Computer, 2022). As the system is easy to navigate, it takes away of the walls that may prevent users from accessing a tool like this for fear of being difficult to navigate or use. This provides an opportunity for the project to be implemented in various public or private organizations and institutions that are interested in making their spaces more accessible. 
 
 
 
 
# CONCLUSION AND RECOMMENDATIONS 
## 5.1 Conclusion 

As stated in the previous chapters, the project analysis was done to come up with a web-based student class attendance system as stated in the findings and results above. In order to make use of the system, a user accesses the system by running the appropriate file, when the file launches and the web cam is activated, the user must place his/her face at a relative distance from the webcam, the system will then provide real-time feedback on each face shape and display the records details instantly. With the ability of student class attendance system to perform realtime face recognition to facilitate classroom control and attendance. This project can be a great tool, which can elevate the burden of recording attendance manually, hence the aim of this project to facilitate and enhance student engagement (Abdalkarim, 2022). One of the most challenging and time-consuming duties is managing the attendance of students.  Every study by researchers aims to simplify such a challenging process using various methods and technologies, student class attendance system fully meets the objectives of the system which it has been developed. The system has reached a steady state where all bugs have been eliminated. The system is operated at a high level of efficiency and all the user associated with the system understands its advantage. The system solves the problem, that it was intended to solve as requirement specification. 

## 5.2 Recommendations 
As a result of the finding made during the analysis and design stages of this research work. In order to improve the effectiveness of the site to its greater height and full potential, its recommended to train the model using deep learning techniques like Vison Transformers or Yolo Real-Time face recognition and tracking to assess the performance and to see how a student class attendance system model trained on vision transformers or yolo would perform in comparison to python face recognition library. 
 
 
__REFERENCES__ 
 
Soni, N. (2023). Real-Time recognition system for sign language gestures . Kampala: ISBAT University. 
Abdalkarim, B. A. (2022). Smart Attendance Systems. Konya: Salahaddin University-Erbil. 
Kano, B. U. (2021). Attendance Management System. kano: Bayero University Kano. 
British Journal of Computer, N. a. (2022). Students' Attendance Management in higher institution using azure cognitive service and opencv face detection & recognition Attendance System. london: British Journal. 

__Note__: Project Report Submitted in Partial Fulfillment of the Requirements for the Degree of Bachelor of Science in Artificial Intelligence and Machine Learning of the [International Business, Science and Technology University.](https://isbatuniversity.ac.ug/) November, 2023, Kampala, Uganda

