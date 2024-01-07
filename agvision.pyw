#!/usr/bin/env python

"""agvision.pyw: A python application to display video feed
    on the screen using minimal compute power"""

__author__ = "Jason Halliday"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason Halliday"]
__version__ = "1.0"
__maintainer__ = "Jason Halliday"
__email__ = "j-halliday@ti.com"
__status__ = "Production"

from tkinter import *
from cv2 import VideoCapture, resize, cvtColor, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH, COLOR_BGR2RGBA, CAP_DSHOW
from PIL import Image, ImageTk 

JOB = None
width, height = 1920, 1080

# Define a video capture object 
vid = VideoCapture(0, CAP_DSHOW) 

# Set the width and height 
vid.set(CAP_PROP_FRAME_WIDTH, width) 
vid.set(CAP_PROP_FRAME_HEIGHT, height)

def open_camera(widget): 
    global JOB
  
    # Capture the video frame by frame 
    _, frame = vid.read()
    frame = resize(frame, (666, 345))
  
    # Convert image from one color space to other 
    opencv_image = cvtColor(frame, COLOR_BGR2RGBA)
  
    # Capture the latest frame and transform to image 
    captured_image = Image.fromarray(opencv_image)
  
    # Convert captured image to photoimage 
    photo_image = ImageTk.PhotoImage(image=captured_image)
  
    # Displaying photoimage in the label 
    widget.photo_image = photo_image
  
    # Configure image in the label 
    widget.configure(image=photo_image) 
  
    # Repeat the same process after every 100 milliseconds 
    JOB = widget.after(34, open_camera, widget)

def close_camera(widget):
    widget.after_cancel(JOB)
    widget.configure(image='')
  
# Create a GUI app 
app = Tk() 
app.bind('<Escape>', lambda e: app.quit())
app.config(bg="red")
app.geometry('%dx%d+%d+%d' % (670, 348, 0, 415))
app.resizable(width=False, height=False)
app.attributes("-topmost", True)
app.title("AGVision")
app.iconbitmap("ti.ico")

# frame = Frame(app, height=450, width=650)
label_widget = Label(app, bg="red")
label_widget.grid(row=1, column=0, columnspan=2)
  
# Create a button to open the camera in GUI app 
# button1 = Button(app, text="Open Camera", command= lambda: open_camera(label_widget)) 
# button1.grid(row=0, column=0) 

# button2 = Button(app, text="Close Camera", command= lambda: close_camera(label_widget)) 
# button2.grid(row=0, column=1)

open_camera(label_widget)
  
# Create an infinite loop for displaying app on screen 
app.mainloop() 
