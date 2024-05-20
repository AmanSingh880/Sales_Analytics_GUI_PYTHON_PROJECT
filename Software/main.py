from tkinter import *
import os
from tkinter import messagebox
import mysql.connector
from datetime import datetime as z
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="sales_report"
)
mycursor = mydb.cursor()

# Data entry class
class data_entry_class():
    def __init__(self):
        self.Product_ID = None
        self.Date = None
        self.Product_Name = None
        self.Product_Model = None
        self.Category = None
        self.MRP = None
        self.Product_sold = None

# Function to show graph
def graph_show():
    global l6, l7, l8, l9, l10
    l6.destroy()
    l7.destroy()
    l8.destroy()
    l9.destroy()
    l10.destroy()
    h1=Label(root,text="Sales Analytics",font="Airtel 30",bg="blue", fg="white").pack()
    mycursor.execute("SELECT date_of_sale, product_sold FROM boat")
    y=[]
    d=[]
    for i in mycursor:
        y.append(i[1])
        d.append(i[0])
    import datetime
    date_list = d
    x = [date.day for date in date_list]
    di = {}
    dl = []
    for i in range(len(d)):
        if x[i] in di:
            di[x[i]] += y[i]
        else:
            di[x[i]] = y[i]
    n = []
    for i in di:
        n.append(i)
        count = x.count(i)
        di[i] = di[i] / count
        dl.append(di[i])
    
    fig = Figure(figsize=(6, 5), dpi=110)
    plot1 = fig.add_subplot(111)
    plot1.plot(n, dl, marker='*', color='blue', linestyle='-.')
    plot1.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    def back_graph():
        root.destroy()
        os.system("main.py")
    def catage_gra():
        root.destroy()
        os.system("catage_grap.py")
    def date_gra():
        root.destroy()
        os.system("date_grap.py")
    bu=Button(text="Categry Wise",bg="dark blue",fg="white",font="Airtel 14",command=catage_gra)
    bu.pack()
    bu=Button(text="Today Data",bg="dark blue",fg="white",font="Airtel 14",command=date_gra)
    bu.pack()
    bu=Button(text="back",bg="dark blue",fg="white",font="Airtel 14",command=back_graph)
    bu.pack()
    toolbar = NavigationToolbar2Tk(canvas, root) 
    toolbar.update() 
    canvas.get_tk_widget().pack()
    root.mainloop()

# Function to save data
def passed(a):
    b = a.Product_ID
    given_date = z.now().date()
    year = given_date.year
    month = given_date.month
    day = given_date.day
    c = str(year) + "/" + str(month) + "/" + str(day)
    d = a.Product_Name
    e = a.Product_Model
    f = a.Category
    g = int(a.MRP)
    h = int(a.Product_sold)
    sql = "INSERT INTO boat (Product_ID, Date_of_sale, Product_Name, Product_Model, Category, MRP, Product_sold) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (b, c, d, e, f, g, h)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.rowcount != 0

# Function to handle data entry
def entry():
    global l6, l7, l8, l9
    l6.destroy()
    l7.destroy()
    l8.destroy()
    l9.destroy()
    def get_values():
        a = data_entry_class()
        a.Product_ID = Poduct_ID.get()
        a.Product_Model = Poduct_Model.get()
        a.Product_Name = Poduct_Name.get()
        a.Category = ctegory.get()
        a.MRP = mp.get()
        a.Product_sold = poduct_sold.get()
        c = passed(a)
        if c == True:
            messagebox.showwarning("Sales Analytic", "Data Saved")
        else:
            messagebox.showwarning("Sales Analytic", "Failed \n Try again")

    def exitf():
        root.destroy()
        os.system("main.py")

    l2 = Label(root, text="Sales Analytics Entry Data", font="Airtel 34", bg="blue", fg="white")
    l2.place(x=300, y=50)
    l3 = Label(root, text="Product ID : ",bg='#51007d', font="Airtel 14" , fg="white")
    l3.place(x=100, y=150)
    l4 = Label(root, text="Product Name :",bg='#51007d', font="Airtel 14" , fg="white")
    l4.place(x=100, y=200)
    l5 = Label(root, text="Product Model :",bg='#51007d', font="Airtel 14" , fg="white")
    l5.place(x=100, y=250)
    l6 = Label(root, text="Category :",bg='#51007d', font="Airtel 14" , fg="white")
    l6.place(x=100, y=300)
    l7 = Label(root, text="MRP :",bg='#51007d', font="Airtel 14" , fg="white")
    l7.place(x=100, y=350)
    l8 = Label(root, text="Product sold :",bg='#51007d', font="Airtel 14", fg="white")
    l8.place(x=100, y=400)
    Poduct_ID = StringVar()
    Poduct_Name = StringVar()
    Poduct_Model = StringVar()
    ctegory = StringVar()
    mp = StringVar()
    poduct_sold = StringVar()
    e1 = Entry(root, textvariable=Poduct_ID, font="Airtel 12")
    e1.place(x=250, y=150)
    e2 = Entry(root, textvariable=Poduct_Name, font="Airtel 12")
    e2.place(x=250, y=200)
    e3 = Entry(root, textvariable=Poduct_Model, font="Airtel 12")
    e3.place(x=250, y=250)
    e4 = Entry(root, textvariable=ctegory, font="Airtel 12")
    e4.place(x=250, y=300)
    e5 = Entry(root, textvariable=mp, font="Airtel 12")
    e5.place(x=250, y=350)
    e6 = Entry(root, textvariable=poduct_sold, font="Airtel 12")
    e6.place(x=250, y=400)
    b1 = Button(root, text="Submit", bg="dark blue", fg="white", font="Airtel 19", command=get_values)
    b1.place(x=180, y=450)
    b2 = Button(root, text="Back", bg="blue", fg="white", font="Airtel 15", command=exitf)
    b2.place(x=50, y=650)
    root.mainloop()

# Function to reset password
def reset_pass():
    root.destroy()
    os.system("reset.py")

# Main application
root = Tk()
root.title("Sales analytic")
root.geometry('1200x750')
root.configure(bg='#51007d')

l6 = Label(root, text="Welcome to Sales Analytics", font="Airtel 34", bg="blue", fg="white")
l6.place(x=300, y=100)
l7 = Button(root, text="Enter Data", bg="dark blue", fg="white", font="Airtel 20", command=entry)
l7.place(x=100, y=250)
l8 = Button(root, text="Reset_Password", bg="dark blue", fg="white", font="Airtel 20", command=reset_pass)
l8.place(x=100, y=400)
l9 = Button(root, text="Analysis", bg="dark blue", fg="white", font="Airtel 20", command=graph_show)
l9.place(x=650, y=250)
l10 = Button(root, text="Exit", bg="blue", fg="white", font="Airtel 15", command=root.destroy)
l10.place(x=50, y=650)

root.mainloop()
