from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os  # For path checking
import mysql.connector
from students import Students
from train import TrainData
from face_recognition import Face_Recognition
from attendance_manage import attendance_man
from developer import Deve


def main():
    win=Tk()
    app=Signin(win)
    win.mainloop()

# Read the password from the file
password_file_path = "material/password.txt"
with open(password_file_path, 'r') as file:
    password = file.read().strip()  # Assuming the password is stored in plain text

class Signin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600+0+0")
        self.root.resizable(0,0)
        self.root.title("Sign In")

        # Icon
        if os.path.exists("icon/face-recognition.ico"):
            self.root.iconbitmap("icon/face-recognition.ico")
        else:
            print("Icon file not found, proceeding without setting icon.")
        
        # Background Image
        image_path = "icon/bg.jpg"
        if os.path.exists(image_path):
            bg= Image.open(image_path)
            bg= bg.resize((900, 600), Image.ANTIALIAS)
            self.photoimg5 = ImageTk.PhotoImage(bg)

            bg_img = Label(self.root, image=self.photoimg5)
            bg_img.place(x=0, y=0, width=900, height=600)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
        
        # User Login Label
        userlogin = Label(bg_img, text="USER LOGIN", font=("Microsoft Yahei UI Light", 18), foreground="firebrick1", background="white")
        userlogin.place(x=555, y=110)
        
        # User Entry Field
        self.user_enter = Entry(bg_img, width=25, font=("Microsoft Yahei UI Light", 12), foreground="firebrick1",bd=0)
        self.user_enter.place(x=520, y=160)  # Adjusted the placement to avoid overlap with the label
        self.user_enter.insert(0, "User Name")
        
        # Bind the focus in event
        self.user_enter.bind('<FocusIn>', self.on_enter)
        
        #frame
        Frame(bg_img,width=240,height=2,bg="red").place(x=520,y=182)
        
        # password Entry Field
        self.password = Entry(bg_img, width=25, font=("Microsoft Yahei UI Light", 12), foreground="firebrick1",bd=0)
        self.password.place(x=520, y=200)  # Adjusted the placement to avoid overlap with the label
        self.password.insert(0, "Password")
        
        # Bind the focus in event
        self.password.bind('<FocusIn>', self.on_enterpass)
        
        #frame
        Frame(bg_img,width=240,height=2,bg="red").place(x=520,y=222)
        
        

        # Eye Button for Password
        self.eye_open = ImageTk.PhotoImage(Image.open("icon/openeye.png").resize((16, 16), Image.ANTIALIAS))
        self.eye_close = ImageTk.PhotoImage(Image.open("icon/closeye.png").resize((16, 16), Image.ANTIALIAS))
        self.eye_btn = Button(bg_img, image=self.eye_open, cursor="hand2", bd=0, bg="white", activebackground="white", command=self.toggle_password_visibility)
        self.eye_btn.place(x=730, y=200)

        self.password_visible = False
        
        #==================forgot===================
        forgotButton=Button(bg_img,command=self.forgot_win,text="Forgot Password?",font=("Microsoft Yahei UI Light", 10,"bold"),foreground="red",bd=0,bg="white",activebackground="white",cursor="hand2",activeforeground="red")
        forgotButton.place(x=637, y=230)
        
        #Login Button
        loginButton=Button(bg_img,text="Login",command=self.login,width=25,font=("Arial", 12,"bold"),foreground="white",bg="red",activebackground="red",cursor="hand2",activeforeground="white")
        loginButton.place(x=505, y=300)
        
        orlabel=Label(bg_img,text="----------------OR----------------",width=20,font=("Arial", 14,"bold"),foreground="red",bg="white")
        orlabel.place(x=505, y=360)
        
        #facebook
        fb=Image.open("icon/facebook.png")
        fbook=fb.resize((32,32), Image.ANTIALIAS)
        self.photoimgfb=ImageTk.PhotoImage(fbook)
        fb_btn=Button(bg_img,image=self.photoimgfb,cursor="hand2",bd=0, bg="white", activebackground="white")
        fb_btn.place(x=570,y=390,width=32,height=32)
        fb_btn.bind("<Button-1>", lambda event:os.startfile('https://www.facebook.com/gauravkumar.rajpoot2161?mibextid=ZbWKwL'))
        
        #linkdin
        linke=Image.open("icon/linkedin.png")
        lnk=linke.resize((32,32), Image.ANTIALIAS)
        self.linkeimg=ImageTk.PhotoImage(lnk)
        linke_btn=Button(bg_img,image=self.linkeimg,cursor="hand2",bd=0, bg="white", activebackground="white")
        linke_btn.place(x=620,y=390,width=32,height=32)
        linke_btn.bind("<Button-1>", lambda event:os.startfile('https://www.linkedin.com/in/gaurav-rajput-95267026b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app'))
        
        #twitter
        tw=Image.open("icon/twitter.png")
        tweet=tw.resize((32,32), Image.ANTIALIAS)
        self.photoimgtw=ImageTk.PhotoImage(tweet)
        tweet_btn=Button(bg_img,image=self.photoimgtw,cursor="hand2",bd=0, bg="white", activebackground="white")
        tweet_btn.place(x=670,y=390,width=32,height=32)
        tweet_btn.bind("<Button-1>", lambda event:os.startfile('https://twitter.com/i/flow/login?'))
        
        #create an account
        newaclabel=Label(bg_img,text="Don't have an account?",width=20,font=("Open Sans",9),foreground="red",bg="white")
        newaclabel.place(x=500, y=450)
        signupbtn=Button(bg_img,text="Create an Account",command=self.reg_win,font=("Open sans",9,"bold underline"),bg="white",fg="blue",bd=0,cursor="hand2",activebackground="white",activeforeground="blue")
        signupbtn.place(x=640,y=450)


    def reg_win(self):
        self.new_win=Toplevel(self.root)
        self.app=SignUp(self.new_win)  

    def toggle_password_visibility(self):
        if self.password_visible:
            self.password.config(show="*")
            self.eye_btn.config(image=self.eye_open)
            self.password_visible = False
        else:
            self.password.config(show="")
            self.eye_btn.config(image=self.eye_close)
            self.password_visible = True

    def on_enter(self, event):
        if self.user_enter.get() == 'User Name':
            self.user_enter.delete(0, END)

    def on_enterpass(self, event):
        if self.password.get() == 'Password':
            self.password.delete(0, END)
            self.password.config(show="*")
            
    def login(self):
        if self.user_enter.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All field required!")
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd=password)
                mycur = conn.cursor()
            except:
                messagebox.showerror("Error","Conection is no established try again!")
                return
            mycur.execute("USE userdata")
            query="select * from udata where username=%s and passwd=%s"
            mycur.execute(query,(self.user_enter.get(),self.password.get()))
            row=mycur.fetchone()

            if row==None:
                messagebox.showerror("error","Invalid username and password!")
            else:
                messagebox.showinfo("Welcome","Login successfully!")
                self.main_win=Toplevel(self.root)
                self.app=Face_Recognition_System(self.main_win)
                
    def forgot_win(self):
        if self.user_enter.get()=="":
            messagebox.showerror("error","Please enter user name")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", passwd=password)
            mycur = conn.cursor()
            mycur.execute("use userdata")
            query="select * from udata where username=%s"
            value=(self.user_enter.get(),)
            row=mycur.fetchone()

            if row==None:
                messagebox.showerror("error","Please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Button")
                self.root.geometry("340x450+610+170")
                self.root.resizable(0,0)


class SignUp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600+0+0")
        self.root.resizable(0,0)
        self.root.title("Sign Up")

        # Icon
        if os.path.exists("icon/face-recognition.ico"):
            self.root.iconbitmap("icon/face-recognition.ico")
        else:
            print("Icon file not found, proceeding without setting icon.")
            
        #=========================variable Declaration===========================
        self.var_email=StringVar()
        self.var_username=StringVar()
        self.var_password=StringVar()
        self.var_confirmpass=StringVar()
        self.check=IntVar()
        
        # Background Image
        image_path = "icon/background.jpg"
        if os.path.exists(image_path):
            bg= Image.open(image_path)
            bg= bg.resize((900, 600), Image.ANTIALIAS)
            self.photoimg5 = ImageTk.PhotoImage(bg)

            bg_img = Label(self.root, image=self.photoimg5)
            bg_img.place(x=0, y=0, width=900, height=600)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
        
        # User Login Label
        usersignup = Label(bg_img, text="CREATE AN ACCOUNT", font=("Microsoft Yahei UI Light", 18), foreground="firebrick1", background="white")
        usersignup.place(x=555, y=70)
        
        email=Label(bg_img,text="Email",width=5,font=("Arial", 12),foreground="red",bg="white")
        email.place(x=520,y=130)
        email_enter = Entry(bg_img, width=25,textvariable=self.var_email, font=("Microsoft Yahei UI Light", 12), foreground="white",bd=0,background="red")
        email_enter.place(x=520,y=160)
        
        username=Label(bg_img,text="Username",width=9,font=("Arial", 12),foreground="red",bg="white")
        username.place(x=520,y=200)
        username_enter = Entry(bg_img,textvariable=self.var_username, width=25, font=("Microsoft Yahei UI Light", 12), foreground="white",bd=0,background="red")
        username_enter.place(x=520,y=230)
        
        password=Label(bg_img,text="Password",width=9,font=("Arial", 12),foreground="red",bg="white")
        password.place(x=520,y=270)
        password_enter = Entry(bg_img,textvariable=self.var_password, width=25, font=("Microsoft Yahei UI Light", 12), foreground="white",bd=0,background="red")
        password_enter.place(x=520,y=300)
        
        c_password=Label(bg_img,text="Confirm Password",width=15,font=("Arial", 12),foreground="red",bg="white")
        c_password.place(x=520,y=340)
        c_password_enter = Entry(bg_img,textvariable=self.var_confirmpass, width=25, font=("Microsoft Yahei UI Light", 12), foreground="white",bd=0,background="red")
        c_password_enter.place(x=520,y=370)
        
        check_btn=Checkbutton(bg_img,variable=self.check,text="I agree to the terms & conditions",font=("Arial", 9),cursor="hand2",activebackground="white",activeforeground="red",foreground="red",background="white",bd=0)
        check_btn.place(x=520,y=410)
        
        #Signup Button
        signupButton=Button(bg_img,text="SignUp",command=self.connect_db,width=25,font=("Arial", 12,"bold"),foreground="white",bg="red",activebackground="red",cursor="hand2",activeforeground="white")
        signupButton.place(x=540, y=470)
        
        orlabel=Label(bg_img,text="Already Account",font=("Open Sans", 10,"bold"),foreground="red",bg="white")
        orlabel.place(x=520, y=520)
        
        loginbtn=Button(bg_img,text="Log in",command=self.log_win,font=("Open sans",9,"bold underline"),bg="white",fg="blue",bd=0,cursor="hand2",activebackground="white",activeforeground="blue")
        loginbtn.place(x=640,y=520)
    
    def connect_db(self):
        if self.var_email.get()=="" or self.var_username.get()=="":
            messagebox.showerror("Error","All fields are required!", parent=self.root)
        elif self.var_password.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Passwords must match", parent=self.root)
        elif self.check.get()==0:
            messagebox.showerror("Error","Please accept Terms & Conditions!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd=password)
                mycur = conn.cursor()
                
                # Check if database exists
                mycur.execute("SHOW DATABASES")
                databases = mycur.fetchall()
                if ('userdata',) not in databases:
                    mycur.execute('CREATE DATABASE userdata')
                    
                mycur.execute('USE userdata')
                
                # Check if table exists
                mycur.execute("SHOW TABLES")
                tables = mycur.fetchall()
                if ('udata',) not in tables:
                    mycur.execute('CREATE TABLE udata (email VARCHAR(50), username VARCHAR(50) PRIMARY KEY, passwd VARCHAR(50), cpasswd VARCHAR(50))')
                
                query=('select * from udata where username= %s')
                mycur.execute(query,(self.var_username.get(),))
                res = mycur.fetchone()
                
                if  res != None:
                    messagebox.showerror("Error","user  already registered.",parent=self.root)
                else:
                    mycur.execute('INSERT INTO udata (email, username, passwd, cpasswd) VALUES (%s, %s, %s, %s)',
                            (self.var_email.get(), self.var_username.get(), self.var_password.get(), self.var_confirmpass.get()))
                
                    conn.commit()
                    conn.close()
                
                    messagebox.showinfo("Success","User registered successfully!", parent=self.root)
                
                    # Clear all entry fields after successful registration
                    self.var_email.set('')
                    self.var_username.set('')
                    self.var_password.set('')
                    self.var_confirmpass.set('')
                    self.check.set(0)
                
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root) 
    def log_win(self):
        self.root.destroy()


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Icon
        if os.path.exists("icon/face-recognition.ico"):
            self.root.iconbitmap("icon/face-recognition.ico")
        else:
            print("Icon file not found, proceeding without setting icon.")

        # Image1
        image_path = "icon/image1.jpg"
        if os.path.exists(image_path):
            img_op1 = Image.open(image_path)
            img1 = img_op1.resize((300, 130), Image.ANTIALIAS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_label = Label(self.root, image=self.photoimg1)
            f_label.place(x=50, y=0, width=300, height=130)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
            
        # Image2
        image_path = "icon/image2.jpg"
        if os.path.exists(image_path):
            img_op2 = Image.open(image_path)
            img2 = img_op2.resize((300, 130), Image.ANTIALIAS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_label = Label(self.root, image=self.photoimg2)
            f_label.place(x=350, y=0, width=300, height=130)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
        
        # Image3
        image_path = "icon/img3.jpg"
        if os.path.exists(image_path):
            img_op3 = Image.open(image_path)
            img3 = img_op3.resize((300, 130), Image.ANTIALIAS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            f_label = Label(self.root, image=self.photoimg3)
            f_label.place(x=650, y=0, width=300, height=130)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
            
        # Image4
        image_path = "icon/image4.jpg"
        if os.path.exists(image_path):
            img_op4 = Image.open(image_path)
            img4 = img_op4.resize((300, 130), Image.ANTIALIAS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            f_label = Label(self.root, image=self.photoimg4)
            f_label.place(x=950, y=0, width=300, height=130)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
        
        
        #Background Image
        image_path = "icon/backgroup.jpg"
        if os.path.exists(image_path):
            bg= Image.open(image_path)
            bg= bg.resize((1530, 790), Image.ANTIALIAS)
            self.photoimg5 = ImageTk.PhotoImage(bg)

            bg_img = Label(self.root, image=self.photoimg5)
            bg_img.place(x=0, y=130, width=1530, height=790)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
        #title name
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTANDANCE",font=("times new roman",35,"bold"),background="cyan",fg="black")
        title_lbl.place(x=0,y=0,width=1500,height=45)
        
        
        #Students Button
        stu1=Image.open("icon\student.png")
        stu=stu1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(stu)
        students_btn=Button(bg_img,image=self.photoimg6,command=self.student_details,cursor="hand2")
        students_btn.place(x=150,y=100,width=150,height=150)
        
        students_btn1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        students_btn1.place(x=150,y=250,width=150,height=50)
        
        
        
        #Face Detector
        face_det=Image.open("icon/profile.png")
        face_det=face_det.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(face_det)
        fd_btn=Button(bg_img,command=self.Face_data,image=self.photoimg7,cursor="hand2")
        fd_btn.place(x=400,y=100,width=150,height=150)
        
        fd_btn1=Button(bg_img,command=self.Face_data,text="FACE DETECTOR",font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        fd_btn1.place(x=400,y=250,width=150,height=50)
        
        
        
        #Attandance
        attandance1=Image.open("icon/attendance.png")
        attandance=attandance1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(attandance)
        attandance_btn=Button(bg_img,command=self.Attend_data,image=self.photoimg8,cursor="hand2")
        attandance_btn.place(x=650,y=100,width=150,height=150)
        
        attandance_btn1=Button(bg_img,command=self.Attend_data,text="Attandance",font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        attandance_btn1.place(x=650,y=250,width=150,height=50)
        
        
        
        #Train Data
        t_data1=Image.open("icon/train-data.png")
        t_data=t_data1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(t_data)
        tdata_btn=Button(bg_img,command=self.train_details,image=self.photoimg9,cursor="hand2")
        tdata_btn.place(x=900,y=100,width=150,height=150)
        
        tdata_btn1=Button(bg_img,command=self.train_details,text="TRAIN DATA",font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        tdata_btn1.place(x=900,y=250,width=150,height=50)
        
        
        
        #Photos
        photo1=Image.open("icon/picture.png")
        photo=photo1.resize((150, 150), Image.ANTIALIAS)
        self.photoimgp=ImageTk.PhotoImage(photo)
        photo_btn=Button(bg_img,command=self.open_img,image=self.photoimgp,cursor="hand2")
        photo_btn.place(x=150,y=350,width=150,height=150)
        
        photo_btn1=Button(bg_img,command=self.open_img,text="PHOTOS",font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        photo_btn1.place(x=150,y=500,width=150,height=50)
        
        
        
        #Help Desk
        hdesk1=Image.open("icon\help-desk.png")
        hdesk=hdesk1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(hdesk)
        helpdesk_btn=Button(bg_img,image=self.photoimg11,cursor="hand2")
        helpdesk_btn.place(x=650,y=350,width=150,height=150)
        
        helpdesk_btn1=Button(bg_img,text="Help Desk",font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        helpdesk_btn1.place(x=650,y=500,width=150,height=50)
        
        #Developer 
        d_data1=Image.open("icon/dev.png")
        d_data=d_data1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(d_data)
        ddata_btn=Button(bg_img,command=self.develop,image=self.photoimg10,cursor="hand2")
        ddata_btn.place(x=900,y=350,width=150,height=150)
        
        ddata_btn1=Button(bg_img,command=self.develop,text="Developer",font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        ddata_btn1.place(x=900,y=500,width=150,height=50)
        
        
        
        #exit
        exitbut1=Image.open("icon\exit.gif")
        exitbut=exitbut1.resize((150, 150), Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(exitbut)
        exitbut_btn=Button(bg_img,command=self.iamexit,image=self.photoimg12,cursor="hand2")
        exitbut_btn.place(x=400,y=350,width=150,height=150)
        
        exitbut_btn1=Button(bg_img,command=self.iamexit,text="Exit",font=("times new roman",12,"bold"),background="black",fg="white",cursor="hand2")
        exitbut_btn1.place(x=400,y=500,width=150,height=50)
    
    #=================================train data============================================
    def open_img(self):
        os.startfile("data")
        
    #==================================Function Button=======================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Students(self.new_window)
    
    def train_details(self):
        self.new_window=Toplevel(self.root)
        self.app=TrainData(self.new_window)
    
    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def Attend_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance_man(self.new_window)
    
    def develop(self):
        self.new_window=Toplevel(self.root)
        self.app=Deve(self.new_window)
    #==================Exit=================
    def iamexit(self):
        self.iamexit=messagebox.askyesno("Face Recognition","Are you sure exit")
        if  self.iamexit>0:
            self.root.destroy()
        else:
            return
        
# Initialize the Tkinter window
if __name__ == "__main__":
    main()
