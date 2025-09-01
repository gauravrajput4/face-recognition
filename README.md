# Face Recognition Attendance System

A Python-based face recognition system for automated attendance management using OpenCV and Tkinter GUI.

## Features

- **Student Registration**: Add and manage student information
- **Face Training**: Train the system with student photos
- **Real-time Face Recognition**: Automatic attendance marking via webcam
- **Attendance Management**: View and manage attendance records
- **MySQL Database Integration**: Store student and attendance data
- **User Authentication**: Secure login system

## Requirements

```
opencv-python
tkinter
PIL (Pillow)
mysql-connector-python
numpy
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gauravrajput4/face-recognition.git
cd face-recognition
```

2. Install required packages:
```bash
pip install opencv-python pillow mysql-connector-python numpy
```

3. Set up MySQL database and update connection details in the code

4. Create password file:
```bash
echo "your_password" > material/password.txt
```

## Usage

1. Run the main application:
```bash
python main.py
```

2. Login with your credentials

3. **Add Students**: Register new students with their photos
4. **Train Data**: Train the face recognition model
5. **Face Recognition**: Start real-time attendance marking
6. **View Attendance**: Check attendance records

## File Structure

- `main.py` - Main application entry point with login
- `students.py` - Student registration and management
- `train.py` - Face recognition model training
- `face_recognition.py` - Real-time face detection and recognition
- `attendance_manage.py` - Attendance viewing and management
- `classifier.xml` - Trained face recognition model
- `haarcascade_frontalface_default.xml` - Face detection cascade
- `data/` - Directory for storing training images
- `icon/` - Application icons and images

## Database Setup

Create a MySQL database with tables for:
- Student information (ID, name, department, course, etc.)
- Attendance records (student ID, date, time, status)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
