import os
import numpy
import cv2 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Face Recognition")
window.geometry('600x400')


head = Label(window, text= "Face Detection & Recognition", width=30, fg= "blue", font=" Georgia 14 bold")
head.place(x=20, y=20)
#head.grid(row=0,column=0)

path = 'C:\\Users\\Swornim\\Face_detection\\Images\\default.jpg'

photo = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image=photo)
panel.place(x=350,y=70)
#panel.grid(row=0, column=1)

def browse_image():
	global image_file_name
	global image_selected 
	global file_to_copy

	path_to_image = filedialog.askopenfilename(initialdir = "C:\\Users\\Swornim\\Face_detection\\Images",title = "Select file",filetypes = (("jpeg files","*.jpg"),("jpeg files","*.jpeg*")))
	
	try:
		if path_to_image:
			path1 = 'C:\\Users\\Swornim\\Face_detection\\Images\\default.jpg'
			photo1 = ImageTk.PhotoImage(Image.open(path1))
			print(path_to_image)
			panel1 = tk.Label(window, image=photo1)
			panel1.place(x= 50,y= 70)
			#image_file_name = os.path.(path_to_image)
			#file_to_copy = path_to_image
			image_selected = True

	except IOError as err:
		image_selected = False
		messagebox.showinfo("File Error",err)


 

#photo = tk.PhotoImage(file="C:\\Users\\Swornim\\Face_detection\\Images")

button1= tk.Button(window, text="Select Image", width=20, command=browse_image)
button1.place(x=60 , y=70)

button2= tk.Button(window, text="Add Image to Dataset",width=20)
button2.place(x=60 , y=115)

button3= tk.Button(window, text="Database Info",width=20)
button3.place(x=60 , y=160)

button4= tk.Button(window, text="Face Recognition",width=20)
button4.place(x=60 , y=205)

button5= tk.Button(window, text="Delete Image",width=20)
button5.place(x=60 , y=250)



window.mainloop()


