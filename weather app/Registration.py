from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import pymysql


# __________ Functional Part for Resetting Reg. Form __________#
# _________ Click Login on Reg. form and it will take to Log in _#

def login_window():
    root.destroy()


# __________ Reset after a successful registration ____________#

def clear():
    entryfname.delete(0, END)
    entrylname.delete(0, END)
    entryemail.delete(0, END)
    entrynumber.delete(0, END)
    entrypass.delete(0, END)
    entrycpass.delete(0, END)
    entryAnswer.delete(0, END)
    comboquestion.current(0)
    check.set(0)


# __________ Functional Part for Register __________#

def register():
    if entryfname.get() == '' or entrylname.get() == '' or entryemail.get() == '' \
            or entrynumber.get() == '' or entrypass.get() == '' or entrycpass.get() == '' \
            or comboquestion.get() == 'Select' or entryAnswer.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')

    # __________ Check pass & cpass are same or not _____#
    elif entrypass.get() != entrycpass.get():
        messagebox.showerror('Error', 'Password Does not Match')

    # __________ Check click the agree or not _______#
    elif check.get() == 0:
        messagebox.showerror('Error', 'Click Agree - "The terms & Conditions"')

    # __________ Connecting to MYSQL ________________#
    else:
        con = pymysql.connect(host='localhost', user='root', password='9730', database='register')
        cur = con.cursor()
        cur.execute("select * from regtable where email=%s", entryemail.get())
        row = cur.fetchone()
        if row != None:
            messagebox.showerror('Error', 'User Already Exists')

        else:
            cur.execute(
                'insert into regtable(f_name,l_name,email,contact,question,answer,password) value(%s,%s,%s,%s,%s,%s,%s)',
                (entryfname.get(), entrylname.get(), entryemail.get(), entrynumber.get(),
                 comboquestion.get(), entryAnswer.get(), entrypass.get()))
            con.commit()
            con.close()

            messagebox.showinfo('Success', 'Registration Successful')
            clear()

        # ___ After Succfully Reg. it will take u to login  ___#
        root.destroy()
        import Login


# __________ GUI ____________________________________#

root = Tk()
root.geometry('1486x780+15+25')
root.title('Registration Form')

# __________ Background Image Setting _______________#

BgImage = PhotoImage(file='BbImage.png')
BgLabel = Label(root, image=BgImage)
BgLabel.place(x=0, y=0)

# __________ Registration Frame _____________________#

registerFrame = Frame(root, width=500, height=700)
registerFrame.place(x=510, y=50)

# __________ Registration Title Name ________________#

titleLabel = Label(registerFrame, text='Registration Form', font=('Bembo', 20, 'bold'), fg='teal')
titleLabel.place(x=145, y=20)

# __________ First Name _____________________________#

fnameLabel = Label(registerFrame, text='First Name', font=('times new roman', 15, 'normal'), fg='gray20')
fnameLabel.place(x=30, y=80)
entryfname = Entry(registerFrame, font=('times new roman', 12), bg='white', width=25)
entryfname.place(x=200, y=80)

# __________ Last Name _____________________________#

lnameLabel = Label(registerFrame, text='Last Name', font=('times new roman', 15, 'normal'), fg='gray20')
lnameLabel.place(x=30, y=140)
entrylname = Entry(registerFrame, font=('times new roman', 12), bg='white', width=25)
entrylname.place(x=200, y=140)

# __________ Email Address __________________________#

emailLabel = Label(registerFrame, text='Email Address', font=('times new roman', 15, 'normal'), fg='gray20')
emailLabel.place(x=30, y=200)
entryemail = Entry(registerFrame, font=('times new roman', 12), bg='white', width=25)
entryemail.place(x=200, y=200)

# __________ Contact Number __________________________#

numberLabel = Label(registerFrame, text='Contact Number', font=('times new roman', 15, 'normal'), fg='gray20')
numberLabel.place(x=30, y=260)
entrynumber = Entry(registerFrame, font=('times new roman', 12), bg='white', width=25)
entrynumber.place(x=200, y=260)

# __________ Security Questions ______________________#

questionLabel = Label(registerFrame, text='Security Question', font=('times new roman', 15, 'normal'), fg='gray20')
questionLabel.place(x=30, y=320)

comboquestion = ttk.Combobox(registerFrame, font=('times new roman', 12, 'normal'), width=23, state='readonly')
comboquestion['values'] = ('Select', 'Your Nick name?', 'Your Best Friend Name?',
                           'Your Favourite Hobby?', 'Your Loved person name?')
comboquestion.place(x=200, y=320)
comboquestion.current(0)  # it will show select on the Security Question Box

# __________ Security Question Answer _________________#

AnswerLabel = Label(registerFrame, text='Your Answer', font=('times new roman', 15, 'normal'), fg='gray20')
AnswerLabel.place(x=30, y=380)
entryAnswer = Entry(registerFrame, font=('times new roman', 12), bg='white', width=25)
entryAnswer.place(x=200, y=380)

# __________ Enter Your Password ______________________#

passLabel = Label(registerFrame, text='Enter Password', font=('times new roman', 15, 'normal'), fg='gray20')
passLabel.place(x=30, y=440)
entrypass = Entry(registerFrame, font=('times new roman', 12), bg='white', show='*', width=25)
entrypass.place(x=200, y=440)

# __________ Confirm Password _________________________#

cpassLabel = Label(registerFrame, text='Confirm Password', font=('times new roman', 15, 'normal'), fg='gray20')
cpassLabel.place(x=30, y=500)
entrycpass = Entry(registerFrame, font=('times new roman', 12), bg='white', show='*', width=25)
entrycpass.place(x=200, y=500)

# __________ I Agree Terms and Conditions _____________#

check = IntVar()  # Crating a variable and making it IntVar() for checking click in registration form or not
checkButton = Checkbutton(registerFrame, text='I Agree All The terms & Conditions', onvalue=1, offvalue=0,
                          variable=check, font=('times new roman', 14, 'bold'), fg='gray20')
checkButton.place(x=40, y=560)

# __________ Registration Button  _____________________#

ButtonImage = PhotoImage(file='registration image.png')
registerButton = Button(registerFrame, image=ButtonImage, bd=0, cursor='hand2', command=register)
registerButton.place(x=80, y=610)

# __________ Login Button  ____________________________#

LoginImage = PhotoImage(file='login image.png')
loginButton = Button(registerFrame, image=LoginImage, bd=0, cursor='hand2', command=login_window)
loginButton.place(x=260, y=610)

root.mainloop()
