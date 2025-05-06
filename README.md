# ATTENDANCE MANAGEMENT SYSTEM USING FACE RECOGNITION #

Take the hassle out of Mess Attendance Tracking.

This system uses Face Recognition to automatically mark Mess Attendance in real-time and generate clean reports — fast, accurate, and easy to use.



### 🚀 FEATURES

- Real-time face detection and attendance marking

- Automatic CSV generation of attendance records

- Manual attendance entry (optional)

- Easy dataset creation (image capture + training)

- Simple GUI (Tkinter)

- Visual attendance reports



### 🛠️ TECH STACK

- Python 3.x

- OpenCV for Image Processing 

- HAAR Cascade classifier for face detection

- LBPH (Local Binary pattern Histogram) for Face Recognition algorithm

- Tkinter for GUI Development

- Numpy/Pandas & CSV for Data Handling



### PROJECT STRUCTURE

<pre>                ATTENDANCE-MANAGEMENT-SYSTEM-USING-FACE-RECOGNITION/
                ├── Attendance/                      # Attendance CSV files (records)
                ├── StudentDetails/                  # CSV/database of student details
                ├── TrainingImage/                   # Raw training images of faces
                ├── TrainingImageLabel/              # Labelled training images
                ├── UI_Image/                        # UI icons/images used in GUI
                │
                ├── haarcascade_frontalface_alt.xml      # Haar cascade model (face detection - alt)
                ├── haarcascade_frontalface_default.xml  # Haar cascade model (face detection - default)
                │
                ├── attendance.py                    # Marks attendance manually from images(main file)
                ├── automaticAttendance.py           # Real-time face detection and automatic attendance
                ├── show_attendance.py               # Display attendance records
                ├── takeImage.py                     # Capture student images (dataset creation)
                ├── takemanually.py                  # Manually add attendance entries
                ├── trainImage.py                    # Train face recognition model from images
                ├── test.py                          # Test the recognition model
                │
                ├── project_requirement.txt          # Project-specific dependencies / instructions
                ├── requirements.txt                 # Python dependencies
                ├── AMS.ico                          # Application icon
                │
                └── README.md                        # This file
</pre>


### 🏗️ HOW IT WORKS

> STUDENT REGISTRATION → IMAGE CAPTURE → MODEL TRAINING → REAL-TIME DETECTION → ATTENDANCE CSV

- Uses Haar Cascades for face detection.

- Matches face with trained images (EigenFace / LBPH Recognizer from OpenCV)

- Marks present & generates a timestamped CSV.



### Project Flow 
Registering a new User 
    -Run the attendance.py file, Click on Register a New Student 

    -A window pops up where you need to enter your Roll No. and Name and then click ob 'Take Image' button

    -Now you'll get a camera window opened and it will detect your face and take upto 50 Images and store it to designed folder (named "TrainignImage")
    
    -Once the image is taken and you get a notification as "Images Saved for {student name} and {roll no.} ", click on "Register the Student". This will train the model and convert images into numeric format so that system can understand . After training the image, next time the system will identify the face if shown the same face.

    -After completing this model, click on "Take Attendance". Here a pop up window opens and you have to enter the meal name as Breakfast, Lunch, Dinner or Snacks. After this click on "Fill Attendance" and a Camera window pops up, it checks if the face is recognised with the data stored.

    -After the face is recognised, it creates a '.csv' file for every Meal and separate every '.csv' file according to the Meal.  

    -Attendance can be viewed after clicking on 'View Attendance' button. It will show the recorx in tabular format.



### ❓ TROUBLESHOOTING

> WEBCAM NOT DETECTED
    - Check if camera access is blocked by OS

> FACE NOT DETECTED PROPERLY
    - Ensure good lighting & clear face position.
    - Use haarcascade_default.xml for more robust detection.

> OPENCV ERRORS(MODULE NOT FOUND)
    -Ensure OPENCV is installed correctly:
    > pip install opencv-contrib-python
