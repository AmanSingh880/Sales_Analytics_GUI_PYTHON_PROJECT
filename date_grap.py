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

def show_dates():
    mycursor.execute("Select date_of_sale from boat")
    d=[]
    for x in mycursor:
        d.append(x[0])
    dat = [date.strftime("%x") for date in d]
    dates=[]
    #04/25/24
    for i in dat:
        s=""
        s="20"+i[-2]+i[-1]+"/"+i[:2]+i[2:5]
        dates.append(s)
    return list(set(dates))
def on_menu_select(value):
    mycursor.execute("Select product_id,product_sold from boat where date_of_sale='{}'".format(value))
    y=[]
    d=[]
    for i in mycursor:
        y.append(i[1])
        d.append(i[0])
    di={}
    dl=[]
    for i in range(len(d)):
        if d[i] in di:
            di[d[i]]+=y[i]
        else:
            di[d[i]]=0
    n=[]
    for i in di:
        n.append(i)
        count=d.count(i)
        di[i]=di[i]/count
        dl.append(di[i])
        fig = Figure(figsize=(6, 5), dpi=110)
    plot1 = fig.add_subplot(111)
    plot1.plot(n, dl, marker='*', color='blue', linestyle='-.')
    plot1.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()



root=Tk()
root.title("Sales analytic")
root.geometry('1200x750')
root.config(bg="red")
l=Label(root,text="Sales Analytics",font="Airtel 34",bg="blue", fg="white")
l.pack()
selected_option = StringVar()
selected_option.set("Date")
options =show_dates();
dropdown = OptionMenu(root, selected_option, *options,command=on_menu_select)
dropdown.place(x=100,y=200)
root.mainloop()
