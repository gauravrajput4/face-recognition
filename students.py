from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os  # For path checking
from tkinter import messagebox
import mysql.connector
import cv2

# Read the password from the file
password_file_path = "material/password.txt"
with open(password_file_path, 'r') as file:
    password = file.read().strip()  # Assuming the password is stored in plain text

class Students:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Icon
        if os.path.exists("icon/face-recognition.ico"):
            self.root.iconbitmap("icon/face-recognition.ico")
        else:
            print("Icon file not found, proceeding without setting icon.")
            
        #=========================variable Declaration===========================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_sid=StringVar()
        self.var_sname=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_add=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()
           
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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),background="cyan",fg="black")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        #main frame
        main_frame=Frame(bg_img,border=2)
        main_frame.place(x=5,y=55,width=1260,height=490)
        
        #Left Side Label Frame
        left_frame=LabelFrame(main_frame,border=2,relief="solid",text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=620,height=490)
        
        #Current Course Information
        course_frame=LabelFrame(left_frame,border=2,relief="solid",text="Current Course Information",font=("times new roman",12,"bold"),background="white")
        course_frame.place(x=10,y=10,width=600,height=100)
        
        #department Label
        
        dep_label=Label(course_frame,text="Department",font=("times new roman",10,"bold"),background="white")
        dep_label.grid(row=0,column=0,padx=2,pady=4)
        
        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly")
        dep_combo["values"]=("Select","IT","Civil","Mechanical","Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=4,pady=4,sticky=W)
        
        #Course Label
        
        course_label=Label(course_frame,text="Courses:-",font=("times new roman",10,"bold"),background="white")
        course_label.grid(row=0,column=2,padx=2,pady=4)
        
        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly")
        course_combo["values"]=("Select","BCA","MCA","BBA","MBA","B.Tech","FE","SE","TE","FE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=4,pady=4,sticky=W)
        
        #Year Label
        year_label=Label(course_frame,text="Year:-",font=("times new roman",10,"bold"),background="white")
        year_label.grid(row=1,column=0,padx=2,pady=4)
        
        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly")
        year_combo["values"]=("Select","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=4,pady=4,sticky=W)
        
        #Semester Label
        sem_label=Label(course_frame,text="Semester:-",font=("times new roman",10,"bold"),background="white")
        sem_label.grid(row=1,column=2,padx=2,pady=4)
        
        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_sem,font=("times new roman",10,"bold"),state="readonly")
        sem_combo["values"]=("Select","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=4,pady=4,sticky=W)
        
        #Student Class Information
        stu_class_frame=LabelFrame(left_frame,border=2,relief="solid",text="Student Class Information",font=("times new roman",12,"bold"),background="white")
        stu_class_frame.place(x=10,y=110,width=600,height=200)
        
        #Student Id label
        
        student_id_label=Label(stu_class_frame,text="Student Id:-",font=("times new roman",10,"bold"),background="white")
        student_id_label.grid(row=0,column=0,padx=2,pady=4)
        
        student_id_entry=ttk.Entry(stu_class_frame,textvariable=self.var_sid,width=25,font=("times new roman",10,"bold"))
        student_id_entry.grid(row=0,column=1,padx=2,pady=4,sticky=W)
        
        
        
        #Class Division
        
        class_div_label=Label(stu_class_frame,text="Class Div:-",font=("times new roman",10,"bold"),background="white")
        class_div_label.grid(row=1,column=0,padx=2,pady=4)
        
        class_div_combo=ttk.Combobox(stu_class_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="readonly")
        class_div_combo["values"]=("Select","A","B","C","D","E","F","G","H","I","J")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=4,pady=4,sticky=W)
        
        #Gender
        gender_label=Label(stu_class_frame,text="Gender:-",font=("times new roman",10,"bold"),background="white")
        gender_label.grid(row=2,column=0,padx=2,pady=4)
        
        gender_combo=ttk.Combobox(stu_class_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly")
        gender_combo["values"]=("Select","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=4,pady=4,sticky=W)
        
        #Email
        email_label=Label(stu_class_frame,text="Email:-",font=("times new roman",10,"bold"),background="white")
        email_label.grid(row=3,column=0,padx=2,pady=4)
        
        email_entry=ttk.Entry(stu_class_frame,textvariable=self.var_email,width=25,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=4,sticky=W)
        
        #Address
        Address_label=Label(stu_class_frame,text="Address:-",font=("times new roman",10,"bold"),background="white")
        Address_label.grid(row=4,column=0,padx=2,pady=4)
        
        address_entry=ttk.Entry(stu_class_frame,textvariable=self.var_add,width=25,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=4,sticky=W)
        
        #student Name
        student_name_label=Label(stu_class_frame,text="Student Name:-",font=("times new roman",10,"bold"),background="white")
        student_name_label.grid(row=0,column=2,padx=2,pady=4,sticky=W)
        
        name_entry=ttk.Entry(stu_class_frame,textvariable=self.var_sname,width=25,font=("times new roman",10,"bold"))
        name_entry.grid(row=0,column=3,padx=2,pady=4,sticky=W)
        
        #Roll NO
        roll_num_label=Label(stu_class_frame,text="Roll No:-",font=("times new roman",10,"bold"),background="white")
        roll_num_label.grid(row=1,column=2,padx=2,pady=4,sticky=W)
        
        roll_no_entry=ttk.Entry(stu_class_frame,textvariable=self.var_rollno,width=25,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=2,pady=4,sticky=W)
        
        #DOB
        dob_label=Label(stu_class_frame,text="Date of Birth:-",font=("times new roman",10,"bold"),background="white")
        dob_label.grid(row=2,column=2,padx=2,pady=4,sticky=W)
        
        dob_entry=ttk.Entry(stu_class_frame,textvariable=self.var_dob,width=25,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=4,sticky=W)
        
        #phone NO:
        phone_label=Label(stu_class_frame,text="Phone No:-",font=("times new roman",10,"bold"),background="white")
        phone_label.grid(row=3,column=2,padx=2,pady=4)
        
        phone_entry=ttk.Entry(stu_class_frame,textvariable=self.var_phone,width=25,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=4,sticky=W)
        
        #radio button for take photo 
        radiobtn1=ttk.Radiobutton(stu_class_frame,variable=self.var_radio1,text="Take Photo",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=4)
        
        radiobtn2=ttk.Radiobutton(stu_class_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=2,pady=4)
        
        #Button Frame
        btn_frame=LabelFrame(left_frame,border=2,relief="solid",font=("times new roman",12,"bold"),background="white")
        btn_frame.place(x=10,y=320,width=600,height=120)
        
        #Save Button
        save_button=Button(btn_frame,text="Save Data",command=self.add_data,width=30,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        save_button.grid(row=0,column=0)
        
        #UPDATE Button
        update_button=Button(btn_frame,text="Update Data",command=self.update_data,width=30,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_button.grid(row=0,column=1)
        
        #DELETE Button
        delete_button=Button(btn_frame,text="Delete Data",command=self.delete_data,width=30,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        delete_button.grid(row=1,column=0)
        
        #RESET Button
        reset_button=Button(btn_frame,command=self.reset_data,text="Reset Data",width=30,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_button.grid(row=1,column=1)
        
        
        
        #ADD PHOTO SAMPLE Button
        add_photo_button=Button(btn_frame,command=self.generate_dataset,text="Add Sample Photo",width=30,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        add_photo_button.grid(row=2,column=0)
        
        #UPDATE PHOTO SAMPLE Button
        update_photo_button=Button(btn_frame,text="Update Sample Photo",width=30,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_photo_button.grid(row=2,column=1)
        
        #Right Side Label Frame
        right_frame=LabelFrame(main_frame,border=2,relief="solid",text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=635,y=10,width=660,height=490)
        
        #Show Data in table
        show_del_frame=LabelFrame(right_frame,border=2,relief="solid",text="View Student details and Search System",font=("times new roman",12,"bold"),background="white")
        show_del_frame.place(x=10,y=10,width=600,height=60)
        
        #Search 
        search_label=Label(show_del_frame,text="Search By",font=("time new roman",13,"bold"),bg="blue",fg="red",cursor="hand2")
        search_label.grid(row=0,column=0,padx=5 ,pady=5,sticky=W)
        
        
        search_combo=ttk.Combobox(show_del_frame,width=10,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Student id","Roll No","DOB")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=4,pady=4,sticky=W)
        
        ele=ttk.Entry(show_del_frame,width=12,font=("times new roman",13,"bold"))
        ele.grid(row=0,column=2,padx=2,pady=4,sticky=W)
        
        search_button=Button(show_del_frame,text="Search",width=10,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        search_button.grid(row=0,column=3, padx=5)
        
        showall_button=Button(show_del_frame,text="Show All",width=10,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        showall_button.grid(row=0,column=4,padx=5)
        
        #Table Frame
        table_frame=LabelFrame(right_frame,border=2,relief="solid",font=("times new roman",12,"bold"),background="white")
        table_frame.place(x=10,y=75,width=600,height=370)
        
        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","division","roll","gender","dob","email","phone","add","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("roll",text="Roll NO")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("add",text="Address")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("add",width=200)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cur)
        self.fetchingData()
        
        
    #===============Function Declaraton=============
    
    def add_data(self):
        if self.var_dep.get()=="Select" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error","All field or required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd=password,database="face_attendance")
                mycur=conn.cursor()

                
                mycur.execute("insert into stu_attendance value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_sid.get(),
                                                                                                                self.var_sname.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_rollno.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_add.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                                
                                                                                                            ))
                
                conn.commit()
                self.fetchingData()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfull",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due to :{str(ex)}",parent=self.root)  
        
        
    #=============== FETCH ING DATA FROM TABLE ====================
    def fetchingData(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd=password,database="face_attendance")
        mycur=conn.cursor()
        
        mycur.execute("select * from stu_attendance")
        data=mycur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children()) 
            for i in data:
                self.student_table.insert('', 'end', values=i)
            
            conn.commit()
        conn.close()
    #====================Get CURSOR===================================
    def get_cur(self,event=""):
        cur_focus=self.student_table.focus()   
        content=self.student_table.item(cur_focus)
        data=content['values']    
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_sid.set(data[4]),
        self.var_sname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_add.set(data[12]),
        self.var_radio1.set(data[13])
    #================update data========================
    def update_data(self):
        if self.var_dep.get()=="Select" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error","All field or required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update == True:
                    conn = None
                    conn=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd=password,
                        database="face_attendance")
                    mycur=conn.cursor()
                    mycur.execute("update stu_attendance SET Dep = %s,course = %s,year = %s,semester = %s,sname = %s, division = %s, rollno = %s, gender = %s, dob = %s, email = %s,phone = %s,address = %s,photosample = %s where sid = %s ",(
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                            self.var_sname.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_rollno.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_add.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_sid.get()
                                                                                                                                                                         ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details has been updated",parent=self.root)
                conn.commit()
                self.fetchingData()
                conn.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Due to :{str(ex)}",parent=self.root)
    
    #==================delete data==============
    def delete_data(self):
        if self.var_sid.get()=="":
            messagebox.showerror("Eror","Student id must be required",parent=self.root)
            
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd=password,database="face_attendance")
                    mycur=conn.cursor()
                    sql="delete from stu_attendance where sid=%s"
                    val=(self.var_sid.get(),)
                    mycur.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetchingData()
                conn.close()
                messagebox.showinfo("Delete","Successfully Delete",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Due to :{str(ex)}",parent=self.root)        
    #=================Reset Button===================
    def reset_data(self):
        self.var_dep.set("Select")
        self.var_course.set("Select")
        self.var_year.set("Select")
        self.var_sem.set("Select")
        self.var_sid.set("")
        self.var_sname.set("")
        self.var_div.set("Select")
        self.var_rollno.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_add.set("")        
        self.var_radio1.set("")
        
    #==========generate Dataset or take photo sample===========
    def generate_dataset(self):
        if self.var_dep.get()=="Select" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error",'All field are required',parent = self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd=password,database="face_attendance")
                my_cur=conn.cursor()
                my_cur.execute("select * from stu_attendance")
                myresult=my_cur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cur.execute("update stu_attendance SET Dep=%s,course=%s,year=%s,semester=%s,sname=%s, division=%s, rollno=%s, gender=%s, dob=%s, email=%s,phone=%s,address=%s,photosample=%s where sid=%s ",(
                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                            self.var_sname.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_rollno.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_add.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_sid.get()
                                                                                                                                                                         ))
                conn.commit()
                self.fetchingData()
                self.reset_data()
                conn.close()
                #=======================Load predefined data on face frontals from open cv=====
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scalling factor = 1.3
                    # Minimum Neighbor = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                try:
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if ret:
                            cropped_face = face_cropped(my_frame)
                            if cropped_face is not None:
                                img_id += 1
                                face = cv2.resize(cropped_face, (450, 450))
                                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                                file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                cv2.imwrite(file_name_path, face)
                                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating datasets complete!")
                except Exception as ex:
                    messagebox.showerror("Error", f"An error occurred: {str(ex)}")

            except Exception as ex:
                messagebox.showerror("Error",f"Due to:{str(ex)}",parent=self.root)
    
        
# Initialize the Tkinter window
if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()