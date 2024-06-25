from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os  # For path checking
import cv2 as cv
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox 

# Read the password from the file
password_file_path = "material/password.txt"
with open(password_file_path, 'r') as file:
    password = file.read().strip()  # Assuming the password is stored in plain text

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Icon
        if os.path.exists("icon/face-recognition.ico"):
            self.root.iconbitmap("icon/face-recognition.ico")
        else:
            print("Icon file not found, proceeding without setting icon.")
        
        #title name
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),background="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        # Image1
        image_path = "icon/face_recognition1.jpg"
        if os.path.exists(image_path):
            img_op1 = Image.open(image_path)
            img1 = img_op1.resize((700, 600), Image.ANTIALIAS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_label = Label(self.root, image=self.photoimg1)
            f_label.place(x=0, y=50, width=700, height=600)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
            
        # Image2
        image_path = "icon/face_recognition2.jpg"
        if os.path.exists(image_path):
            img_op2 = Image.open(image_path)
            img2 = img_op2.resize((600, 600), Image.ANTIALIAS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_labe2 = Label(self.root, image=self.photoimg2)
            f_labe2.place(x=700, y=50, width=600, height=600)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
        #button
        face_detect=Button(self.root,command=self.face_reco,text="Face Recognize",font=("times new roman",12,"bold"),background="green",fg="white",cursor="hand2")
        face_detect.place(x=900,y=580,width=150,height=50)
        
    # ===========================Attendance======================
    def mark_attendance(self, i,j,n,m,t):
        with open("material/students.csv", "a", newline="\n") as f:
            MyDataList=f.readlines()
            name_list=[]
            for line in MyDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (j not in name_list) and (n not in name_list) and (m not in name_list) and (t not in name_list) ): 
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.write(f"\n{i},{j},{n},{m},{t},{dtstring},{d1},Present")
                
    # =======================Face Recognition==================
    def face_reco(self):
        def draw_boundry(img, classifier, scaleFactor, miniNeighbors, color, text, clf):
            gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, miniNeighbors)

            coord=[]
            
            for (x, y, w, h) in features:
                cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict/300)))
                
                conn = mysql.connector.connect(host="localhost", user="root", passwd=password, database="face_attendance")
                my_cur = conn.cursor()
                
                my_cur.execute("select sid from stu_attendance where sid="+str(id))                    
                i = my_cur.fetchone()
                i="+".join(i)
                
                my_cur.execute("select sname from stu_attendance where sid="+str(id))                    
                j = my_cur.fetchone()
                j="+".join(j)
                
                my_cur.execute("select rollno from stu_attendance where sid="+str(id))                    
                n = my_cur.fetchone()
                n="+".join(n)
                
                my_cur.execute("select Dep from stu_attendance where sid="+str(id))                    
                m = my_cur.fetchone()
                m="+".join(m)
                
                my_cur.execute("select email from stu_attendance where sid="+str(id))                    
                t = my_cur.fetchone()
                t="+".join(t)
                
                if confidence > 77:
                    cv.putText(img, f"Student id: {i}", (x, y-75), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    cv.putText(img, f"Roll: {n}", (x, y-55), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    cv.putText(img, f"Name: {j}", (x, y-35), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    cv.putText(img, f"Department: {m}", (x, y-20), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    cv.putText(img, f"Email: {t}", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    self.mark_attendance(i, j, n, m, t)
                else:
                    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv.putText(img, "Unknown face", (x, y-55), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)

                coord=[x,y,w,h]
            return coord
            
        def recognize(img, clf, faceCascade):
            coord=draw_boundry(img, faceCascade, 1.1, 10, (255, 25, 255), "face", clf)
            return img
        
        faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
        #clf=cvEigenFaceRecognizer_create()
        clf = cv.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv.imshow("Welcome To Face Recognition", img)
            
            if cv.waitKey(1) == 13:
                break

        video_cap.release()
        cv.destroyAllWindows()

# Initialize the Tkinter window
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
