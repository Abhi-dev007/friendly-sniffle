import tkinter
from tkinter import *
from PIL import Image, ImageTk


def display_invalid_window():
    mainwindow = tkinter.Tk()
    mainwindow.title('Sudoku')
    mainwindow.geometry('640x480')
    label = tkinter.Label(mainwindow, text="You entered a invalid Sudoku", fg="red", font=('Arial', 16, 'bold'))
    label.pack(side='top')
    oop_image = Image.open("C:\\Users\\Abhishek Pandey\\Downloads\\oops_image.jpg")
    oop_image = oop_image.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(oop_image)
    label1 = tkinter.Label(mainwindow, image=img)
    label1.pack(pady=30)

    button = tkinter.Button(mainwindow, text='Quit', width=50, fg='white', background='black',
                            command=mainwindow.destroy)
    button.pack(side='bottom', pady=20)

    mainwindow.mainloop()
