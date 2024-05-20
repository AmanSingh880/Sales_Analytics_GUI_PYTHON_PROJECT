from tkinter import *
import pickle
import os
from tkinter import messagebox
import sqlite3

# Database connection
mydb = sqlite3.connect('Sales_pass.db')
mycursor = mydb.cursor()

# Create table if it doesn't exist
mycursor.execute('''
CREATE TABLE IF NOT EXISTS Sales_pass (
    Password TEXT
)
''')
mydb.commit()
def main_call():
    root.destroy()
    os.system("main.py")
def add_password(password):
    mycursor.execute("INSERT INTO Sales_pass (Password) VALUES (?)", (password,))
    mydb.commit()

def reset_password(password):
    def validate_password_reset(password):
        Upper_case=Num=Spec_char=False
        if(len(password)<8):
            messagebox.showwarning("Sales Analytic","Password must have 8 characters")
            return False
        for i in password:
            if(i.isupper()):
                Upper_case=True
            elif(not(i.isalnum())):
                Spec_char=True
            elif(i.isdigit()):
                Num=True
        if(Upper_case and Num and Spec_char):
            return True
        else:
            if(Upper_case):
                if(Num):
                    messagebox.showwarning("Sales Analytic","Password must have special character")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have digits(0-9)")
            elif(Num):
                if(Upper_case):
                    messagebox.showwarning("Sales Analytic","Password must have special character(@-#)")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have Uppercase character(A-Z)")
            else:
                if(Num):
                    messagebox.showwarning("Sales Analytic","Password must have Uppercase character(A-Z)")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have digits(0-9)")
            return False

    
    if(validate_password_reset(password)):
        add_password(password)
        messagebox.showwarning("Sales Analytic","Password Changed")
        return True
    else:
        messagebox.showwarning("Sales Analytic","Retry ")
        return False
root=Tk()
root.title("Sales analytic")
root.geometry('1200x800')
root.configure(bg='#51007d')
l=Label(root,text="Welcome to Sales Analytics",font="Airtel 34",bg="blue", fg="white")
l.place(x=300,y=100)
def f2():
    messagebox.showwarning("Sales Analytic","Enter New Password in Password feild then reclick on Reset Button\n if Already entered please ignore")
    password=var.get()
    reset_password(password)


l1=Label(root,text="Enter the password",font="Airtel 15",bg="white",fg="black")
l1.place(x=100,y=300)
var=StringVar()
l2=Entry(root,text=var,bg="sky blue",fg="dark blue",font="Airtel 15")
l2.place(x=300,y=300)
l4=Button(root,text="Reset" ,bg="blue",fg="white",font="Airtel 15",command=f2)
l4.place(x=200,y=400)
a=Button(root,text="Back",bg="blue",fg="White",font="Arial 20",command=main_call)
a.place(x=20,y=700)
root.mainloop()
