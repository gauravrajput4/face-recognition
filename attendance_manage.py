from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os  # For path checking
from tkinter import messagebox
import mysql.connector
import cv2
import csv
from tkinter import filedialog

# Read the password from the file
password_file_path = "material/password.txt"
with open(password_file_path, 'r') as file:
    password = file.read().strip()  # Assuming the password is stored in plain text


mydata=[]
class attendance_man:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #======================Variables==================
        self.var_stuid=StringVar()
        self.var_name=StringVar()
        self.var_time=StringVar()
        self.var_roll=StringVar()
        self.var_department=StringVar()
        self.var_date=StringVar()
        self.var_email=StringVar()
        self.var_attendance=StringVar()
        
        # Icon
        if os.path.exists("icon/face-recognition.ico"):
            self.root.iconbitmap("icon/face-recognition.ico")
        else:
            print("Icon file not found, proceeding without setting icon.")
            
        
        # Image1
        image_path = "icon/student1.jpg"
        if os.path.exists(image_path):
            img_op1 = Image.open(image_path)
            img1 = img_op1.resize((350, 130), Image.ANTIALIAS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_label = Label(self.root, image=self.photoimg1)
            f_label.place(x=0, y=0, width=350, height=130)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
            
        # Image2
        image_path = "icon/student2.jpg"
        if os.path.exists(image_path):
            img_op2 = Image.open(image_path)
            img2 = img_op2.resize((350, 130), Image.ANTIALIAS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_label = Label(self.root, image=self.photoimg2)
            f_label.place(x=350, y=0, width=350, height=130)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
        
        # Image3
        image_path = "icon/student3.jpg"
        if os.path.exists(image_path):
            img_op3 = Image.open(image_path)
            img3 = img_op3.resize((350, 130), Image.ANTIALIAS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            f_label = Label(self.root, image=self.photoimg3)
            f_label.place(x=700, y=0, width=350, height=130)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
            
        # Image4
        image_path = "icon/student4.jpg"
        if os.path.exists(image_path):
            img_op4 = Image.open(image_path)
            img4 = img_op4.resize((350, 130), Image.ANTIALIAS)
            self.photoimg4 = ImageTk.PhotoImage(img4)

            f_label = Label(self.root, image=self.photoimg4)
            f_label.place(x=1050, y=0, width=350, height=130)
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
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT ",font=("times new roman",35,"bold"),background="cyan",fg="black")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        #main frame
        main_frame=Frame(bg_img,border=2)
        main_frame.place(x=5,y=55,width=1260,height=490)
        
        #Left Side Label Frame
        left_frame=LabelFrame(main_frame,border=2,relief="solid",text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=620,height=470)
        
        #Student Class Information
        stu_class_frame=LabelFrame(left_frame,border=2,relief="solid",text="Student Information",font=("times new roman",12,"bold"),background="white")
        stu_class_frame.place(x=10,y=110,width=600,height=200)
        
        #Student Id label
        
        student_id_label=Label(stu_class_frame,text="Student Id:-",font=("times new roman",10,"bold"),background="white")
        student_id_label.grid(row=0,column=0,padx=2,pady=4)
        
        student_id_entry=ttk.Entry(stu_class_frame,textvariable=self.var_stuid,width=25,font=("times new roman",10,"bold"))
        student_id_entry.grid(row=0,column=1,padx=2,pady=4,sticky=W)
        
        
        
        #Student Name
        
        sname_label=Label(stu_class_frame,text="Student Name:-",font=("times new roman",10,"bold"),background="white")
        sname_label.grid(row=1,column=0,padx=2,pady=4)
        
        sname_entry=ttk.Entry(stu_class_frame,textvariable=self.var_name,width=25,font=("times new roman",10,"bold"))
        sname_entry.grid(row=1,column=1,padx=2,pady=4,sticky=W)
        
        
        #Time
        time_label=Label(stu_class_frame,text="Time:-",font=("times new roman",10,"bold"),background="white")
        time_label.grid(row=2,column=0,padx=2,pady=4)
        
        time_entry=ttk.Entry(stu_class_frame,textvariable=self.var_time,width=25,font=("times new roman",10,"bold"))
        time_entry.grid(row=2,column=1,padx=2,pady=4,sticky=W)
        #Attendance Status
        attendance_label=Label(stu_class_frame,text="Attendance Status:-",font=("times new roman",10,"bold"),background="white")
        attendance_label.grid(row=3,column=0,padx=2,pady=4)
        
        attendance_combo=ttk.Combobox(stu_class_frame,textvariable=self.var_attendance,font=("times new roman",10,"bold"),state="readonly")
        attendance_combo["values"]=("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=4,pady=4,sticky=W)
        
        
        
        #Roll No
        rollno_label=Label(stu_class_frame,text="Roll No:-",font=("times new roman",10,"bold"),background="white")
        rollno_label.grid(row=0,column=2,padx=2,pady=4)
        
        rollno_entry=ttk.Entry(stu_class_frame,textvariable=self.var_roll,width=25,font=("times new roman",10,"bold"))
        rollno_entry.grid(row=0,column=3,padx=2,pady=4,sticky=W)
        
        #Department
        department_label=Label(stu_class_frame,text="Department:-",font=("times new roman",10,"bold"),background="white")
        department_label.grid(row=1,column=2,padx=2,pady=4)
        
        department_entry=ttk.Entry(stu_class_frame,textvariable=self.var_department,width=25,font=("times new roman",10,"bold"))
        department_entry.grid(row=1,column=3,padx=2,pady=4,sticky=W)
        
        
        #Date
        date_label=Label(stu_class_frame,text="Dates:-",font=("times new roman",10,"bold"),background="white")
        date_label.grid(row=2,column=2,padx=2,pady=4)
        
        date_entry=ttk.Entry(stu_class_frame,textvariable=self.var_date,width=25,font=("times new roman",10,"bold"))
        date_entry.grid(row=2,column=3,padx=2,pady=4,sticky=W)
        
        #Email
        email_label=Label(stu_class_frame,text="Email:-",font=("times new roman",10,"bold"),background="white")
        email_label.grid(row=3,column=2,padx=2,pady=4)
        
        email_entry=ttk.Entry(stu_class_frame,textvariable=self.var_email,width=25,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=3,padx=2,pady=4,sticky=W)
        
        #Button Frame
        btn_frame=LabelFrame(left_frame,border=2,relief="solid",font=("times new roman",12,"bold"),background="white")
        btn_frame.place(x=10,y=320,width=600,height=120)
        
        #Import csv
        save_button=Button(btn_frame,command=self.importcsv,text="Import csv",width=25,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        save_button.grid(row=0,column=0,pady=10,padx=15)
        
        #Export csv
        update_button=Button(btn_frame,command=self.exportcsv,text="Export csv",width=25,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_button.grid(row=0,column=1,pady=10,padx=5)
        
        #Update
        delete_button=Button(btn_frame,text="Update",width=25,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        delete_button.grid(row=1,column=0,pady=10,padx=15)
        
        #Reset
        reset_button=Button(btn_frame,command=self.reset_data,text="Reset",width=25,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_button.grid(row=1,column=1,pady=10,padx=5)
        
        
        #Right Side Label Frame
        right_frame=LabelFrame(main_frame,border=2,relief="solid",text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=635,y=10,width=620,height=470)
         
         #Table Frame
        table_frame=LabelFrame(right_frame,border=2,relief="solid",font=("times new roman",12,"bold"),background="white")
        table_frame.place(x=10,y=10,width=600,height=450)
        
        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")
        
        self.attendance_table=ttk.Treeview(table_frame,columns=("id","Roll","Name","Department","Time","Date","Attendance","Email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        
        self.attendance_table.heading("id",text="Student id")
        self.attendance_table.heading("Roll",text="Roll No")
        self.attendance_table.heading("Name",text="Student Name")
        self.attendance_table.heading("Department",text="Department")
        self.attendance_table.heading("Time",text="Time")
        self.attendance_table.heading("Date",text="Date")
        self.attendance_table.heading("Attendance",text="Attendance Status")
        self.attendance_table.heading("Email",text="Email")
        
        self.attendance_table["show"]= "headings"
        
        self.attendance_table.column("id",width=100)
        self.attendance_table.column("Roll",width=100)
        self.attendance_table.column("Name",width=100)
        self.attendance_table.column("Department",width=100)
        self.attendance_table.column("Time",width=100)
        self.attendance_table.column("Date",width=100)
        self.attendance_table.column("Attendance",width=120)
        self.attendance_table.column("Email",width=200)
        
        
        self.attendance_table.pack(fill=BOTH,expand=True)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor) 
        
    #=============Fetch data===============
    def fetchdata(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)
            

    def importcsv(self):
        global mydata 
        mydata.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetype=(("CSV files", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if filename:  # Check if a file was selected
            with open(filename, 'r') as myfile:  # Open the file in read mode
                csvread = csv.reader(myfile, delimiter=",")  # Specify the delimiter as ","
                mydata = []  # Initialize an empty list to store the data
                for row in csvread:
                    mydata.append(row)
                self.fetchdata(mydata)  # Call fetchdata method with the data
                
    #================Export CSV==================
    def exportcsv(self):
        try:
            global mydata
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data Found! Please Import First.", parent=self.root)
                return False
            
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetype=(("CSV files", "*.csv"), ("All Files", "*.*")), parent=self.root)
            if filename:
                with open(filename, mode='w', newline='') as myfile:
                    exp_write = csv.writer(myfile, delimiter=',')
                    for row in mydata:
                        exp_write.writerow(row)  # Use writerow to write a single row
                messagebox.showinfo("Success", "Data Exported Successfully!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Due to: {str(ex)}", parent=self.root)
    #==================Get cursor=================
    def get_cursor(self,event=""):
        cursor_row=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_row)['values']
        rows=content['values']
        self.var_stuid.set(rows[0])
        self.var_name.set(rows[1])
        self.var_time.set(rows[2])
        self.var_attendance.set(rows[3])
        self.var_roll.set(rows[4])
        self.var_department.set(rows[5])
        self.var_date.set(rows[6])
        self.var_email.set(rows[7])
        
    #=============Reset==============
    def reset_data(self):
        self.var_stuid.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_attendance.set("Status")
        self.var_roll.set("")
        self.var_department.set("")
        self.var_date.set("")
        self.var_email.set("")

        
        
        
# Initialize the Tkinter window
if __name__ == "__main__":
    root = Tk()
    obj = attendance_man(root)
    root.mainloop()