from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
from tkinter import messagebox

class TrainData:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.initialize_window()

    def initialize_window(self):
        self.root.geometry("1300x790+0+0")

        # Set icon
        icon_path = "icon/face-recognition.ico"
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        else:
            print("Icon file not found, proceeding without setting icon.")

        # Title
        title_lbl = Label(self.root, text="Train Data", font=("times new roman", 35, "bold"),
                          background="yellow", fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45) 

        # Load and display images
        image_paths = ["icon/facerec1.jpg", "icon/facerec2.jpg", "icon/facerec3.jpg", "icon/facerec4.jpg"]
        for i, image_path in enumerate(image_paths):
            if os.path.exists(image_path):
                img_op = Image.open(image_path)
                img_resized = img_op.resize((310, 130), Image.ANTIALIAS)
                photoimg = ImageTk.PhotoImage(img_resized)

                f_label = Label(self.root, image=photoimg)
                f_label.place(x=i * 310, y=50, width=310, height=130)

                # Keep reference to the image to prevent garbage collection
                f_label.image = photoimg
            else:
                print(f"Image file {image_path} not found. Please check the path.")

        # Train Button
        train_btn = Button(self.root, text="TRAIN DATA", command=self.train_classifier,
                           font=("times new roman", 20, "bold"), background="white", fg="red", cursor="hand2")
        train_btn.place(x=0,y=190,width=1300,height=60)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        if not path:
            messagebox.showerror("Error", "No images found in data directory!")
            return

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert to grayscale
            imagenp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)

            # Show image during training (optional)
            cv2.imshow("Training", imagenp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = TrainData(root)
    root.mainloop()
