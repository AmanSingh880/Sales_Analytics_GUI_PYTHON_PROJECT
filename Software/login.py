from tkinter import *
import pickle
import os
from tkinter import messagebox
import webbrowser
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

def get_latest_password():
    mycursor.execute("SELECT Password FROM Sales_pass")
    passwords = mycursor.fetchall()
    if passwords:
        return passwords[-1][0]
    else:
        # Insert the default password if the table is empty
        default_password = "Aman@123"
        mycursor.execute("INSERT INTO Sales_pass (Password) VALUES (?)", (default_password,))
        mydb.commit()
        return default_password


def main_call():
    os.system("main.py")

def browse():
    webbrowser.open("https://amansingh880.github.io/4th-sem-project/index.html")

root = Tk()
root.title("Sales Analytics")
root.geometry('1200x800')
root.configure(bg='#1c1c1c')
root.iconbitmap("logo.jpg")  # Add this line to set the window icon
canvas = Canvas(root, width=1200, height=800)
canvas.pack(fill='both', expand=True)

# Gradient background function
def create_gradient(canvas, color1, color2):
    for i in range(800):
        r, g, b = (
            int(color1[1:3], 16) * (800 - i) // 800 + int(color2[1:3], 16) * i // 800,
            int(color1[3:5], 16) * (800 - i) // 800 + int(color2[3:5], 16) * i // 800,
            int(color1[5:7], 16) * (800 - i) // 800 + int(color2[5:7], 16) * i // 800,
        )
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, 1200, i, fill=color)

create_gradient(canvas, "#2e2e2e", "#1c1c1c")

l1 = Label(root, text=" Login ", font=("Helvetica", 40, "bold"), bg='#1c1c1c', fg="#f1c40f")
l1.place(x=300, y=100,width=200)

def Validate_password(password):
    valid = False
    try:
            original_password=get_latest_password()
            if original_password == password:
                valid = True
                return True
            else:
                messagebox.showwarning("Sales Analytics", "Incorrect Password click on websupport and contact to Sales Analytics to recover your password")
                return False
    except:
        messagebox.showwarning("Sales Analytics", "Data not Found")
    return valid

def f1():
    password = var.get()
    if Validate_password(password):
        print("Successful")
        root.destroy()
        main_call()
    else:
        print("Failed")

l2 = Label(root, text="Enter the password", font=("Helvetica", 18, "bold"), bg="#1c1c1c", fg="white")
l2.place(x=100, y=300)

var = StringVar()
l3 = Entry(root, textvariable=var, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 15), show="x")
l3.place(x=350, y=300, width=300, height=30)

def create_button(text, command, x, y):
    return Button(root, text=text, bg="#3498db", fg="white", font=("Helvetica", 18, "bold"), command=command, relief=FLAT, activebackground="#2980b9", activeforeground="white").place(x=x, y=y, width=200, height=50)

create_button("Submit", f1, 200, 400)
create_button("WEB SUPPORT", browse, 450, 400)
create_button("Back", root.destroy, 20, 700)

root.mainloop()
