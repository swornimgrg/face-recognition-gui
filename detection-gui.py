import os
import numpy as np
import cv2 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

global panel
window = tk.Tk()
window.title("Face Recognition")
window.geometry('600x400')


head = Label(window, text= "Face Detection & Recognition", width=30, fg= "blue", font=" Georgia 14 bold")
head.place(x=20, y=20)

path = 'C:\\Users\\Swornim\\Face_detection\\Images\\default.jpg'

photo = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image=photo)
panel.place(x=350,y=70)

def browse_image():
	global image_selected
	global photo
	global img
	global path_to_image

	path_to_image = filedialog.askopenfilename(initialdir = "C:\\Users\\Swornim\\Face_detection\\Images\\yalefaces",title = "Select file",filetypes = (("jpeg files","*.jpg"),("jpeg files","*.jpeg*")))
	
	try:
		if path_to_image:
			photo = ImageTk.PhotoImage(Image.open(path_to_image))
			print(path_to_image)
			panel = tk.Label(window, image=photo)
			panel.place(x= 250,y= 70)
			image_selected = True

	except IOError as err:
		image_selected = False
		messagebox.showinfo("File Error",err)



def detect_face():

	face_cascade= cv2.CascadeClassifier("C:\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

	img = cv2.imread(path_to_image)

	faces = face_cascade.detectMultiScale(img, scaleFactor = 1.16, minNeighbors = 5)
	print(faces)

	for x,y,w,h in faces:
		img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

	#photo = ImageTk.PhotoImage(Image.open(path_to_image))



button1= tk.Button(window, text="Browse", width=20, command=browse_image)
button1.place(x=60 , y=70)

button2= tk.Button(window, text="Add Image to Dataset",width=20)
button2.place(x=60 , y=115)

button3= tk.Button(window, text="Database Info",width=20)
button3.place(x=60 , y=160)

button4= tk.Button(window, text="Face Recognition",width=20,command=detect_face)
button4.place(x=60 , y=205)

button5= tk.Button(window, text="Delete Image",width=20)
button5.place(x=60 , y=250)

window.mainloop()


