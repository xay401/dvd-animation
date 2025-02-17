from tkinter import * # import everything from tkinter
import time # import the time module

WIDTH = 1000 # set the width of the window to 1000
HEIGHT = 1000 # set the height of the window to 1000
xVelocity = 10 # set the x velocity to 10
yVelocity = 15  # set the y velocity to 15


window = Tk() # create a window

canvas = Canvas(window, width=WIDTH, height=HEIGHT) # create a canvas
canvas.pack()   # pack the canvas


#background_image = PhotoImage(file="you_file_here") # load the background image
#background = canvas.create_image(0, 50, image=background_image, anchor=NW) # create the background image on the canvas

photo_image = PhotoImage(file="dvd.png") # load the image
my_image = canvas.create_image(0, 50, image=photo_image, anchor=NW) # create the image on the canvas

image_width = photo_image.width() # get the width of the image
image_height = photo_image.height() # get the height of the image

def update_image(): # function to update the image
    global xVelocity, yVelocity # make the xVelocity and yVelocity global
    coordinates = canvas.coords(my_image) # get the coordinates of the image
    if(coordinates[0]>=WIDTH-image_width or coordinates[0]<0): # if the image hits the right or left side of the window
        xVelocity = xVelocity *-1 # reverse the x velocity
    if(coordinates[1]>=WIDTH-image_height or coordinates[1]<0): # if the image hits the top or bottom of the window
        yVelocity = yVelocity *-1 # reverse the y velocity
    canvas.move(my_image,xVelocity,yVelocity) # move the image
    window.update() # update the window
    window.after(10, update_image) # call the function again after 10 milliseconds
 
update_image() # call the function
window.mainloop() # run the window