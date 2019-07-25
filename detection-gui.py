import numpy as np
import cv2 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image


global canvas

window = tk.Tk()
window.title("Face Recognition")
window.geometry('600x400')
canvas_width = 600
canvas_height = 400
canvas = Canvas(window, width = canvas_width, height = canvas_height, relief = 'raised')
canvas.pack()


head = Label(window, text= "Face Detection & Recognition", width=30, fg= "blue", font=" Georgia 14 bold")
head.place(x=20, y=20)

path = 'C:\\Users\\Swornim\\Face_detection\\Images\\default.jpg'

photo = ImageTk.PhotoImage(Image.open(path))

canvas.create_image(250,70, anchor=NW, image=photo)

def browse_image():
	global image_selected
	global photo
	global img
	global path_to_image

	path_to_image = filedialog.askopenfilename(initialdir = "C:\\Users\\Swornim\\Face_detection\\Images\\yalefaces",title = "Select file",filetypes = (("jpeg files","*.jpg"),("jpeg files","*.jpeg*")))
	
	try:
		if path_to_image:
			img = np.array(Image.open(path_to_image))
			photo = ImageTk.PhotoImage(Image.open(path_to_image))
			print(path_to_image)
			canvas.create_image(250,70, anchor=NW, image=photo)
			image_selected = True

	except IOError as err:
		image_selected = False
		messagebox.showinfo("File Error",err)

	print(img.shape)

def detect_face():
	global img
	face_cascade = cv2.CascadeClassifier("C:\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
	faces = face_cascade.detectMultiScale(img, scaleFactor = 1.16, minNeighbors = 5)

	print(faces)

	for x,y,w,h in faces:
		canvas.create_rectangle(x+250, y+70, w+x+250, h+y+70, outline = '#39ff14' , width = 2)
	

button1= tk.Button(window, text = "Browse", width = 20, command = browse_image)
button1.place(x=60 , y=70)

button2= tk.Button(window, text = "Add Image to Dataset",width = 20)
button2.place(x=60 , y=115)

button3= tk.Button(window, text = "Database Info",width=20)
button3.place(x=60 , y=160)

button4= tk.Button(window, text = "Face Recognition",width=20 , command = detect_face)
button4.place(x=60 , y=205)

button5= tk.Button(window, text="Delete Image",width=20)
button5.place(x=60 , y=250)

window.mainloop()


