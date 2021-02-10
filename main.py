from tkinter import *
from PIL import Image, ImageTk
root= Tk()
root.geometry('300x300')
root.title('Main Form')

def emp():
    root.destroy()
    import employee


def busi():
    root.destroy()
    import business

canvas = Canvas(root, width = 150, height = 150)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("C:\\Users\\DELL\\Desktop\\resume\\logo.png"))
canvas.create_image(20, 20, anchor=NW, image=img)


label=Label(root,text="Welcome to ShineNetCore :)",bg='blue',width=25,font=('bold',15))
label.place(x=10,y=150)

b1=Button(root,text='Business Form',bg='orange',font=5,command=busi)
b1.place(x=20,y=200)

b2=Button(root,text='Employee Form',bg='green',font=5,command=emp)
b2.place(x=160,y=200)


root.mainloop()

