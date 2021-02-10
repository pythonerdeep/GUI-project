from tkinter import *
import sqlite3
from tkinter import filedialog
from tkinter import messagebox

def create_first_frame():
    label = Label(first_frame, text="Step 1", width=10, font=('bold', 30))
    label.place(x=80, y=-100)

    ab = Label(first_frame, text='Name',font=5)
    ab.grid()
    xy = Entry(first_frame, textvar=Fullname,font=5)
    xy.grid(row=0, column=1, pady=10, padx=20, sticky=N)

    number = Label(first_frame, text='MobileNumber',font=5)
    number.grid()
    number = Entry(first_frame, textvar=Mobilenumber,font=5)
    number.grid(row=1, column=1, pady=10, padx=20, sticky=N)

    email = Label(first_frame, text='EmailID',font=5)
    email.grid()
    email = Entry(first_frame, textvar=Emailid,font=5)
    email.grid(row=2, column=1, pady=10, padx=20, sticky=N)

    # create the button for the frame
    first_quite_btn = Button(first_frame, text="Quit",font=2, bg="gray", command=quite_program)
    first_quite_btn.grid(column=0, row=3, pady=10, sticky=N)
    first_next_btn = Button(first_frame, text='Next',font=2, bg='blue', command=call_second_frame)
    first_next_btn.grid(column=3, row=3, pady=10, stick=N)


def create_second_frame():
    label2= Label(second_frame, text="Step 2", width=10, font=('bold', 30))
    label2.place(x=-40, y=-100)

    f = Label(second_frame, text='Any Govt. ID', font=5)
    f.place(x=-60, y=-20)
    list = ['Aadhar Card', 'Voter ID', 'Passport', 'DL']
    droplist = OptionMenu(second_frame, c, *list)
    droplist.config(width=15)
    c.set("Select Your ID")
    droplist.place(x=80, y=-23)

    b = Button(second_frame, text='Upload', font=2, bg='orange', command=fileDialog)
    b.grid(column=1, row=2, pady=20)

    # b11 = Button(third_frame, text='save', font=2, bg='gray', command=file_save)
    # b11.grid()

    #create the button for the frame
    second_back_btn=Button(second_frame,text='Back',font=2,bg='gray',command=call_first_frame)
    second_back_btn.grid(column=0,row=3,pady=10,stick=N)
    second_next_btn=Button(second_frame,text="Next",font=2,bg='blue',command=call_third_frame)
    second_next_btn.grid(column=2,row=3,pady=10,sticky=N)

def create_third_frame():
    label3= Label(third_frame, text="Step 3", width=10, font=('bold', 30))
    label3.place(x=80, y=-100)

    a = Label(third_frame, text='Your business name',font=5)
    a.grid()
    a = Entry(third_frame, textvar=aa,font=5)
    a.grid(row=0, column=1, pady=10, padx=20, sticky=N)

    y = Label(third_frame, text='Company Type',font=5)
    y.grid()
    list2 = ['Pvt.', 'Ltd.', 'Proprietor']
    droplist = OptionMenu(third_frame, n, *list2)
    droplist.config(width=20)
    n.set("Select Your Company")
    droplist.place(x=175, y=40)

    #create the button for the frame
    third_back_btn=Button(third_frame,text="Back",font=2,bg='gray',command=call_second_frame)
    third_back_btn.place(x=20,y=100)
    third_next_btn=Button(third_frame,text="Next",font=2,bg='blue',command=call_fourth_frame)
    third_next_btn.place(x=350,y=100)


def create_fourth_frame():
    label4 = Label(fourth_frame, text="Step 4", width=10, font=('bold', 30))
    label4.place(x=160, y=-100)

    x = Label(fourth_frame, text='What location you want to start?', font=5)
    x.grid()
    list3=['Noida','Delhi','Lucknow','Bangluru','Pune']
    droplist=OptionMenu(fourth_frame,xx,*list3)
    droplist.config(width=20)
    xx.set('Select location')
    droplist.grid(row=0,column=1,pady=10,padx=20,sticky=N)

    labe=Label(fourth_frame,text='which area you want to heir employees for you business?',font=5)
    labe.grid()
    list5=['IT','Sales & Marketing','Accountant','Operator','Data Entry']
    droplist=OptionMenu(fourth_frame,mm,*list5)
    droplist.config(width=20)
    mm.set('Select Area')
    droplist.grid(row=1,column=1,pady=10,padx=20,sticky=N)

    y = Label(fourth_frame, text='How many employee you need?', font=5)
    y.grid()
    list4=['1','2','3','4','5','6','7','8','9']
    droplist=OptionMenu(fourth_frame,yy,*list4)
    droplist.config(width=20)
    yy.set('Select Option')
    droplist.grid(row=2,column=1,pady=10,padx=20,sticky=N)

    z = Label(fourth_frame, text='What work you want to do?', font=5)
    z.grid()
    list6=['Developer','Designer','Accountant','E-commerce','sales & Management']
    droplist=OptionMenu(fourth_frame,zz,*list6)
    droplist.config(width=20)
    zz.set('Select work')
    droplist.grid(row=3, column=1, pady=10, padx=20, sticky=N)

    #create button for the frame
    fourth_back_btn=Button(fourth_frame,text='Back',font=2,bg='gray',command=call_third_frame)
    fourth_back_btn.place(x=30,y=230)
    fourth_next_btn=Button(fourth_frame,text="Next",font=2,bg='blue',command=call_fifth_frame)
    fourth_next_btn.place(x=520,y=230)

def create_fifth_frame():
    label5= Label(fifth_frame, text="Step 5", width=10, font=('bold', 30))
    label5.place(x=70, y=-100)

    domain = Label(fifth_frame, text='Domain Name',font=5)
    domain.grid()
    domain = Entry(fifth_frame, textvar=dname,font=5)
    domain.grid(row=0, column=1, pady=10, padx=20, sticky=N)

    #create button for the frame
    fifth_back_bnt=Button(fifth_frame,text="Back",font=2,bg='gray',command=call_fourth_frame)
    fifth_back_bnt.grid(column=0,row=3,pady=10,sticky=N)
    fifth_submit_btn=Button(fifth_frame,text='Submit',font=2,bg='green',command=database)
    fifth_submit_btn.grid(column=1,row=3,pady=10,sticky=N)
    fifth_quite_btn=Button(fifth_frame,text='Quit',font=2,bg='red',command=quite_program)
    fifth_quite_btn.grid(column=3,row=3,pady=10,sticky=N)


def call_first_frame():
    second_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

def call_second_frame():
    first_frame.grid_forget()
    third_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

def call_third_frame():
    second_frame.grid_forget()
    fourth_frame.grid_forget()
    third_frame.grid(column=0,row=0,padx=20,pady=5,sticky=(W,N,E))

def call_fourth_frame():
    third_frame.grid_forget()
    fifth_frame.grid_forget()
    fourth_frame.grid(column=0,row=0,padx=20,pady=5,sticky=(W,N,E))

def call_fifth_frame():
    fourth_frame.grid_forget()
    fifth_frame.grid(column=0,row=0,padx=20,pady=5,sticky=(W,N,E))

def quite_program():
    root.destroy()

def fileDialog():
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                            filetypes=(("jpeg", "*.jpg"), ("All Files", "*.*")))
    label=Label(third_frame,text=" ")
    label.place(x=-50,y=40)
    label.config(text=filename)

def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.


def database():
    name1=Fullname.get()
    mobile=Mobilenumber.get()
    email=Emailid.get()
    id = c.get()
    businessname = aa.get()
    companyname = n.get()
    location=xx.get()
    area=mm.get()
    eneed=yy.get()
    warea=zz.get()
    domainname=dname.get()
    conn=sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Business (Fullname TEXT, MobileNumber TEXT, Email TEXT, id TEXT, bname TEXT, cname TEXT, loc TEXT, area TEXT, eneed TEXT, warea TEXT, dname TEXT)')
    cursor.execute('INSERT INTO Business(Fullname, MobileNumber, id, bname, cname, Email, loc, area, eneed, warea, dname) VALUES(?,?,?,?,?,?,?,?,?,?)',(name1,mobile,email,location,area,eneed,warea,id,businessname,companyname,domainname))
    conn.commit()
    messagebox.showinfo("ShineNetCore Says","Record Inserted Successfully")
#####################################
########## main program :)###########
#####################################

#create root GUI window
root = Tk()

#define size
window_width=400
window_height=400

Fullname=StringVar()
Mobilenumber=IntVar()
Emailid=StringVar()
c=StringVar()
aa=StringVar()
n=StringVar()
xx=StringVar()
mm=StringVar()
yy=StringVar()
zz=StringVar()
dname=StringVar()

#create frames
first_frame= Frame(root,width=window_width, height=window_height)
first_frame['borderwidth'] = 200
first_frame['relief'] = 'sunken'
first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

second_frame= Frame(root, width=window_width, height=window_height)
second_frame['borderwidth'] = 100
second_frame['relief'] = 'sunken'
second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

third_frame= Frame(root, width=window_width, height=window_height)
third_frame['borderwidth'] = 200
third_frame['relief'] = 'sunken'
third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

fourth_frame=Frame(root, width=window_width, height=window_height)
fourth_frame['borderwidth'] = 200
fourth_frame['relief'] = 'sunken'
fourth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))

fifth_frame=Frame(root, width=window_width, height=window_height)
fifth_frame['borderwidth'] = 200
fifth_frame['relief'] = 'sunken'
fifth_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(W, N, E))


# Create all widgets to all frames
create_fifth_frame()
create_fourth_frame()
create_third_frame()
create_second_frame()
create_first_frame()

# Hide all frames in reverse order, but leave first frame visible (unhidden).
fifth_frame.grid_forget()
fourth_frame.grid_forget()
third_frame.grid_forget()
second_frame.grid_forget()



# Start tkinter event - loop
root.mainloop()