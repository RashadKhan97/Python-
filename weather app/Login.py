from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk


# ______  > Functionality Part for Forget Password < _____#

def forget_password():
    if entryemail.get() == '':
        messagebox.showerror('Error', 'To Reset enter Email then click on Forget Password')

    else:
        con = pymysql.connect(host='localhost', user='root', password='9730', database='register')
        cur = con.cursor()
        cur.execute('select * from regtable where email=%s', entryemail.get())
        row = cur.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Enter a Valid Email Address')
        else:
            con.close()

            # __________ New Password setting and connecting with SQL  ____#

            def Change_password():
                if securityquesCombo.get() == 'Select' or entryAns.get() == '' or entryNewPass.get() == '':
                    messagebox.showerror('Error', 'All Fields are Required')

                else:
                    con = pymysql.connect(host='localhost', user='root', password='9730', database='register')
                    cur = con.cursor()
                    cur.execute('select * from regtable where email=%s and question=%s and answer=%s',
                                (entryemail.get(), securityquesCombo.get(), entryAns.get()))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror('Error', 'Security Question or Answer is Incorrect', parent=root2)

                    else:
                        cur.execute('update regtable set password=%s where email=%s',
                                    (entryNewPass.get(), entryemail.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success', 'Password Successfully reset, Login with new password',
                                            parent=root2)

                        # ______ After successfully reset, Qus box, Answer box, pass box will be null
                        # ______  on Forget Password Frame and cut to Log in box  ____#
                        securityquesCombo.current(0)
                        entryAns.delete(0, END)
                        entryNewPass.delete(0, END)
                        root2.destroy()

            # ___ Forget Password Windows/Frame and Title ___#

            root2 = Toplevel()
            root2.geometry('470x560+500+160')
            root2.title('Forget Password')
            root2.config(bg='white')
            root2.focus_force()
            root2.grab_set()  # Not to minimize
            forgetLabel = Label(root2, text='Forget', font=('times new roman', 20, 'bold'), bg='white')
            forgetLabel.place(x=140, y=10)

            forgetpassLabel = Label(root2, text='Password', font=('times new roman', 20, 'bold'), bg='white',
                                    fg='Forest Green')
            forgetpassLabel.place(x=230, y=10)

            # __________ Forget Password Icon  ______________#

            passwordimage = PhotoImage(file='ForgetPassword.png')
            passwordimageLabel = Label(root2, image=passwordimage, bg='white')
            passwordimageLabel.place(x=113, y=50)

            # __________ Security Question Box  ______________#

            securityquesLabel = Label(root2, text='Security Questions', font=('times new roman', 14, 'bold'),
                                      bg='white')
            securityquesLabel.place(x=90, y=250)
            securityquesCombo = ttk.Combobox(root2, font=('times new roman', 13), state='readonly', width=30)
            securityquesCombo['values'] = ('Select', 'Your Nick name?', 'Your Best Friend Name?',
                                           'Your Favourite Hobby?', 'Your Loved person name?')
            securityquesCombo.place(x=90, y=282)
            securityquesCombo.current(0)

            # __________ Security Answer Box  ______________#

            AnsLabel = Label(root2, text='Your Answer', font=('times new roman', 14, 'bold'),
                             bg='white')
            AnsLabel.place(x=90, y=317)
            entryAns = Entry(root2, font=('times new roman', 14), bg='gray97', width=32)
            entryAns.place(x=90, y=349)

            # __________ New Password Box  ______________#

            NewPassLabel = Label(root2, text='New Password', font=('times new roman', 14, 'bold'), bg='white')
            NewPassLabel.place(x=90, y=380)
            entryNewPass = Entry(root2, font=('times new roman', 14), bg='gray97', width=32)
            entryNewPass.place(x=90, y=412)

            # __________ Change Password Button _________#
            changePasswordbutton = Button(root2, text='Change Password', font=('times new roman', 14, 'bold'),
                                          fg='white', bg='forest green', cursor='hand2', activebackground='black',
                                          activeforeground='white', bd=0, width=20, command=Change_password)
            changePasswordbutton.place(x=130, y=460)

            root2.mainloop()


# __________ > Functionality Part for Login < ___________#
# __________ Create New Account and Closing Login ___#

def register_window():
    window.destroy()
    import Registration


# ___ Show Error if Email & Pass not Given in Login ___#

def signin():
    if entryemail.get() == '' or entryPass.get() == '':
        messagebox.showerror('error', 'Please Enter Your email and Password')

    # __________ Login with correct Email & Pass __________#

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='9730', database='register')
            cur = con.cursor()
            cur.execute('select * from regtable where email=%s and password=%s', (entryemail.get(), entryPass.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror('error', 'Invalid Email and Password! Check Again')
            else:
                messagebox.showinfo('Successful', 'Welcome!')
            con.close()

        except Exception as e:
            messagebox.showerror('error', f'Error is due to {e}')

        # __________ After Login it will take to Weather App _______________#
        window.destroy()
        import weather

# __________ GUI ____________________________________#
window = Tk()
window.geometry('1486x780+15+25')
window.title('Login Page')

# __________ Background Image Setting _______________#
bgloginimage = PhotoImage(file='BbImage.png')
bgloginLabel = Label(window, image=bgloginimage)
bgloginLabel.place(x=0, y=0)

# __________ Login Frame ____________________________#
loginFrame = Frame(window, width=360, height=480)
loginFrame.place(x=560, y=155)

# __________ Login Title Name _______________________#
title1Label = Label(loginFrame, text='Login', font=('Bembo', 25, 'bold'), fg='black')
title1Label.place(x=135, y=35)

# __________ User Icon placement ____________________#
UserImage = PhotoImage(file='UserTrans.png')
UserImageLabel = Label(loginFrame, image=UserImage, bd=0)
UserImageLabel.place(x=150, y=108)

# __________ Email Entry Box ________________________#
emailLabel = Label(loginFrame, text='Email Address', font=('times new roman', 14, 'normal'), fg='Black')
emailLabel.place(x=40, y=200)
entryemail = Entry(loginFrame, font=('times new roman', 12), bg='white', width=34)
entryemail.place(x=40, y=230)

# __________ Password Entry Box _____________________#
PassLabel = Label(loginFrame, text='Password', font=('times new roman', 14, 'normal'), fg='Black')
PassLabel.place(x=40, y=260)
entryPass = Entry(loginFrame, font=('times new roman', 12), bg='white', show='*', width=34)
entryPass.place(x=40, y=290)  # line 69 show='*' indicates password will be invisible

# __________ Forget Password Title __________________#
Forgetbutton = Button(loginFrame, text='Forget Password?', font=('arial', 11,), bd=0, fg='red',
                      cursor='hand2', command=forget_password, activebackground='white', activeforeground='gray20')
Forgetbutton.place(x=180, y=318)

# __________ Login Button Title __________________#
Lbutton2 = Button(loginFrame, text='Login', font=('times new roman', 15, 'bold'), fg='white', bg='teal', cursor='hand2',
                  activebackground='black', activeforeground='white', bd=0, width=20, command=signin)
Lbutton2.place(x=52, y=362)

# __________ Register New Account Title _____________#
Regbutton = Button(loginFrame, text='New Here! Create an Account?', font=('times new roman', 12, 'bold'), bd=0,
                   fg='gray18',
                   cursor='hand2', activeforeground='blue', command=register_window)
Regbutton.place(x=40, y=410)

window.mainloop()
