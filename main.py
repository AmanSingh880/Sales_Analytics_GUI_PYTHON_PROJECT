from tkinter import *
import os
from tkinter import messagebox
import mysql.connector
from datetime import datetime as z
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="sales_report"
)
mycursor = mydb.cursor()
class data_entry_class():
    def __init__(self):
        self.Product_ID = None
        self.Date = None
        self.Product_Name = None
        self.Product_Model = None
        self.Category = None
        self.MRP = None
        self.Product_sold = None

def graph_show():
    l12.destroy()
    l11.destroy()
    l.destroy()
    l1.destroy()
    b2.destroy()
    h1=Label(root,text="Sales Analytics",font="Airtel 30",bg="blue", fg="white").pack()
    mycursor.execute("Select date_of_sale,product_sold from boat")
    y=[]
    d=[]
    for i in mycursor:
        y.append(i[1])
        d.append(i[0])
    import datetime
    date_list = d
    x = [date.day for date in date_list]
    di={}
    dl=[]
    for i in range(len(d)):
        if x[i] in di:
            di[x[i]]+=y[i]
        else:
            di[x[i]]=0
    n=[]
    for i in di:
        n.append(i)
        count=x.count(i)
        di[i]=di[i]/count
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


def passed(a):
    b = a.Product_ID
    given_date=z.now().date()
    year = given_date.year
    month = given_date.month
    day = given_date.day
    c= str(year)+"/"+str(month)+"/"+str(day)
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

def entry():
    l12.destroy()
    l11.destroy()
    l.destroy()
    l1.destroy()
    def get_values():
        a=data_entry_class()
        a.Product_ID=Poduct_ID.get()
        a.Product_Model=Poduct_Model.get()
        a.Product_Name=Poduct_Name.get()
        a.Category=ctegory.get()
        a.MRP=mp.get()
        a.Product_sold=poduct_sold.get()
        c=passed(a)
        if(c==True):
            messagebox.showwarning("Sales Analytic","Data Saved")
        else:
            messagebox.showwarning("Sales Analytic","Failed \n Try again")

    def exitf():
        root.destroy()
        os.system("main.py")

    l2=Label(root,text="Sales Analytics Entry Data",font="Airtel 34",bg="blue", fg="white")
    l2.place(x=300,y=50)
    # Product Name	Product_Model	category	MRP	product_sold
    l3=Label(root,text="Product ID : ",font="Airtel 14",bg="red",fg="white")
    l3.place(x=100,y=150)
    l4=Label(text="Product Name :",font="Airtel 14",bg="red",fg="white")
    l4.place(x=100,y=200)
    l5=Label(text="Product Model :",font="Airtel 14",bg="red",fg="white")
    l5.place(x=100,y=250)
    l6=Label(text="Category :",font="Airtel 14",bg="red",fg="white")
    l6.place(x=100,y=300)
    l7=Label(text="MRP :",font="Airtel 14",bg="red",fg="white")
    l7.place(x=100,y=350)
    l7=Label(text="Product sold :",font="Airtel 14",bg="red",fg="white")
    l7.place(x=100,y=400)
    Poduct_ID=StringVar()
    Poduct_Name=StringVar()
    Poduct_Model=StringVar()
    ctegory=StringVar()
    mp=StringVar()
    poduct_sold=StringVar()
    e1=Entry(text=Poduct_ID,font="Airtel 12")
    e1.place(x=250,y=150)
    e2=Entry(text=Poduct_Name,font="Airtel 12")
    e2.place(x=250,y=200)
    e3=Entry(text=Poduct_Model,font="Airtel 12")
    e3.place(x=250,y=250)
    e4=Entry(text=ctegory,font="Airtel 12")
    e4.place(x=250,y=300)
    e5=Entry(text=mp,font="Airtel 12")
    e5.place(x=250,y=350)
    e6=Entry(text=poduct_sold,font="Airtel 12")
    e6.place(x=250,y=400)
    b1=Button(text="Submit",bg="dark blue",fg="white",font="Airtel 19",command=get_values)
    b1.place(x=180,y=450)
    b2=Button(text="Back",bg="blue",fg="white",font="Airtel 15",command=exitf)
    b2.place(x=50,y=650)
    root.mainloop()
def reset_pass():
    root.destroy()
    os.system("reset.py")
root=Tk()
root.title("Sales analytic")
root.geometry('1200x750')
root.config(bg="red")
l=Label(root,text="Welcome to Sales Analytics",font="Airtel 34",bg="blue", fg="white")
l.place(x=300,y=100)
l1=Button(text="Enter Data",bg="dark blue",fg="white",font="Airtel 20",command=entry)
l1.place(x=100,y=250)
l12=Button(text="Reset_Password",bg="dark blue",fg="white",font="Airtel 20",command=reset_pass)
l12.place(x=100,y=400)
l11=Button(text="Analysis",bg="dark blue",fg="white",font="Airtel 20",command=graph_show)
l11.place(x=650,y=250)
b2=Button(text="Exit",bg="blue",fg="white",font="Airtel 15",command=root.destroy)
b2.place(x=50,y=650)

root.mainloop()
