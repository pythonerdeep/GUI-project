from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
root=Tk()
root.geometry("500x600")
root.title('Employee Form')

Fullname=StringVar()
Fname=StringVar()
emailid=StringVar()
var=StringVar(root, "1")
z=StringVar()
xx=StringVar()
num=IntVar()
address=StringVar()
c=StringVar()

def quit_program():
    root.destroy()
def database():
    f_name=Fname.get()
    name=Fullname.get()
    email=emailid.get()
    gender = var.get()
    field=z.get()
    jtype=xx.get()
    number=num.get()
    addre=address.get()
    country=c.get()
    conn=sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Employee (f_name TEXT, name TEXT, Email TEXT, gender TEXT, field TEXT, jobtype TEXT, number TEXT, address TEXT, country TEXT)')
    cursor.execute('INSERT INTO Employee (f_name, Name, email, gender, field, jobtype, number, address, country) VALUES(?,?,?,?,?,?,?,?)',(f_name,name,email,field,jtype,gender,number,addre,country))
    conn.commit()
    messagebox.showinfo("ShineNetCore Says","Record Inserted Successfully")

def fileDialog():
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                            filetypes=(("jpeg", "*.jpg"), ("All Files", "*.*")))
    label=Label(root,text=" ")
    label.place(x=150,y=510)
    label.config(text=filename)

label_0=Label(root,text="Employee Registration Form", width=30,font=('bold',20))
label_0.place(x=20,y=53)

label_1=Label(root,text="FullName",width=10,font=5)
label_1.place(x=80,y=110)
entry_1=Entry(root,textvar=Fullname,font=5)
entry_1.place(x=220,y=110)


label_2=Label(root,text="Father's Name",width=15,font=5)
label_2.place(x=70,y=150)
entry_2=Entry(root,textvar=Fname,font=5)
entry_2.place(x=220,y=150)

label_3=Label(root,text="Email_ID",width=10,font=5)
label_3.place(x=70,y=190)
entry_3=Entry(root,textvar=emailid,font=5)
entry_3.place(x=220,y=190)


label_4=Label(root,text="Gender",width=10,font=5)
label_4.place(x=70,y=230)
Radiobutton(root,text="Male",padx=5,variable=var,value='male').place(x=210,y=230)
Radiobutton(root,text='Female',padx=20,variable=var,value='female').place(x=300,y=230)

label_5=Label(root,text="Choose Field",width=10,font=5)
label_5.place(x=70,y=270)
list2=['Web design','Sales & Marketing','Software','PHP','Networking']
droplist2=OptionMenu(root,z,*list2)
droplist2.config(width=20)
z.set("Area of Interest")
droplist2.place(x=220,y=265)

label_6=Label(root,text="Job Type",width=15,font=5)
label_6.place(x=60,y=310)
list3=['Full Time','Part Time','Work From Home']
droplist3=OptionMenu(root,xx,*list3)
droplist3.config(width=20)
xx.set('Job Type')
droplist3.place(x=220,y=310)

label_7=Label(root,text="MobileNumber",width=15,font=5)
label_7.place(x=60,y=350)
entry_7=Entry(root,textvar=num,font=5)
entry_7.place(x=220,y=355)

label_8=Label(root,text="Address",width=10,font=5)
label_8.place(x=70,y=390)
entry_8=Entry(root,textvar=address,font=5)
entry_8.place(x=220,y=390)

label_9=Label(root,text="Country",width=10,font=5)
label_9.place(x=70,y=430)
list1=['Canada','India','UK','Nepal','Australia']
droplist=OptionMenu(root,c,*list1)
droplist.config(width=20)
c.set("Select your Country")
droplist.place(x=220,y=430)

label_10=Label(root,text='Resume/CV',width=10,font=5)
label_10.place(x=70,y=470)
l=Button(root,text='Choose file',width=10,font=5,command=fileDialog)
l.place(x=220,y=470)
#create button
btn=Button(root,text='Submit',font=2,bg='green',command=database)
btn.place(x=180,y=540)
bt=Button(root,text='Quit',font=2,bg='red',command=quit_program)
bt.place(x=280,y=540)

root.mainloop()
