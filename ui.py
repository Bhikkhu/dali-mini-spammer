from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window
root = Tk()
rows = 7
columns = 7
# Adding widgets to the root window
  
# Creating a photoimage object to use image

photo = PhotoImage(file = r"test.png")
photo2 = PhotoImage(file = r"test2.png")

# Resizing image to fit on button
photoimage = photo.subsample(3, 3)
photoimage2 = photo.subsample(3, 3)
  
# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button


def hello_generator(x, y):
    return lambda: hello(x, y)

def hello(x, y):
    print(f"helloooo, {x}, {y}!")
    buttons[x, y].configure(image = photoimage2)
    buttons[(column, row)].grid(row = row, column = column)

buttons = {}
for column in range(columns):
    for row in range(rows):
        buttons[(column, row)] = Button(root, image = photoimage,
                    compound = LEFT, command = hello_generator(column, row))
        photo = PhotoImage(file = r"test.png")
       #  buttons[(column, row)].config(height=100, width=100)
        buttons[(column, row)].grid(row = row, column = column)



