from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os  # For path checking

class Deve:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Page")

        # Icon
        if os.path.exists("icon/face-recognition.ico"):
            self.root.iconbitmap("icon/face-recognition.ico")
        else:
            print("Icon file not found, proceeding without setting icon.")
            
        
        # Image1
        image_path = "icon/Gaurav.jpg"
        if os.path.exists(image_path):
            bgimg = Image.open(image_path)
            img = bgimg.resize((1530, 790), Image.ANTIALIAS)
            self.photoimg1 = ImageTk.PhotoImage(img)

            bg_img = Label(self.root, image=self.photoimg1)
            bg_img.place(x=0, y=0, width=1530, height=790)
        else:
            print(f"Image file {image_path} not found. Please check the path.")
            
        #instagram
        insta=Image.open("icon/instagram.png")
        ins=insta.resize((32,32), Image.ANTIALIAS)
        self.photoimgins=ImageTk.PhotoImage(ins)
        insta_btn=Button(bg_img,image=self.photoimgins,cursor="hand2")
        insta_btn.place(x=1330,y=150,width=32,height=32)
        insta_btn.bind("<Button-1>", lambda event:os.startfile('https://www.instagram.com/akhil.8_'))
        
        #facebook
        fb=Image.open("icon/facebook.png")
        fbook=fb.resize((32,32), Image.ANTIALIAS)
        self.photoimgfb=ImageTk.PhotoImage(fbook)
        fb_btn=Button(bg_img,image=self.photoimgfb,cursor="hand2")
        fb_btn.place(x=1330,y=200,width=32,height=32)
        fb_btn.bind("<Button-1>", lambda event:os.startfile('https://www.facebook.com/gauravkumar.rajpoot2161?mibextid=ZbWKwL'))
        
        #linkdin
        linke=Image.open("icon/linkedin.png")
        lnk=linke.resize((32,32), Image.ANTIALIAS)
        self.linkeimg=ImageTk.PhotoImage(lnk)
        linke_btn=Button(bg_img,image=self.linkeimg,cursor="hand2")
        linke_btn.place(x=1330,y=250,width=32,height=32)
        linke_btn.bind("<Button-1>", lambda event:os.startfile('https://www.linkedin.com/in/gaurav-rajput-95267026b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app'))
        
        #twitter
        tw=Image.open("icon/twitter.png")
        tweet=tw.resize((32,32), Image.ANTIALIAS)
        self.photoimgtw=ImageTk.PhotoImage(tweet)
        tweet_btn=Button(bg_img,image=self.photoimgtw,cursor="hand2")
        tweet_btn.place(x=1330,y=300,width=32,height=32)
        tweet_btn.bind("<Button-1>", lambda event:os.startfile('https://twitter.com/AkhilRajput1641'))
        
        #Github
        ghub=Image.open("icon/github.png")
        github=ghub.resize((32,32), Image.ANTIALIAS)
        self.ghubimg=ImageTk.PhotoImage(github)
        ghub_btn=Button(bg_img,image=self.ghubimg,cursor="hand2")
        ghub_btn.place(x=1330,y=350,width=32,height=32)
        ghub_btn.bind("<Button-1>", lambda event:os.startfile('https://github.com/akhils6155'))
        
        #email
        email=Image.open("icon/social.png")
        mail=email.resize((32,32), Image.ANTIALIAS)
        self.emailimg=ImageTk.PhotoImage(mail)
        email_btn=Button(bg_img,image=self.emailimg,cursor="hand2")
        email_btn.place(x=1330,y=400,width=32,height=32)
        email_btn.bind("<Button-1>", lambda event:os.startfile('mailto:graj75657@gmail.com'))    
            
# Initialize the Tkinter window
if __name__ == "__main__":
    root = Tk()
    obj = Deve(root)
    root.mainloop()