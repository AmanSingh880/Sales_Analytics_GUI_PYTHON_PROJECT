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

def show_categories():
    mycursor.execute("Select Distinct category from boat")
    cat=[]
    for x in mycursor:
        cat.append(x[0])
    return cat
def back_sh():
    root.destroy()
    os.system("main.py")
def on_menu_select(value):
   # canvas.get_tk_widget().destroy()
    mycursor.execute("Select date_of_sale,product_sold from boat where category='{}'".format(value))
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

root=Tk()
root.title("Sales analytic")
root.geometry('1200x750')
root.configure(bg='#51007d')
l=Label(root,text="Sales Analytics",font="Airtel 34",bg="blue", fg="white")
l.pack()
selected_option = StringVar()
selected_option.set("Categories")
options =show_categories();
dropdown = OptionMenu(root, selected_option, *options,command=on_menu_select)
dropdown.place(x=100,y=200)
b2=Button(text="back",bg="blue",fg="white",font="Airtel 15",command=back_sh)
b2.place(x=50,y=650)
root.mainloop()
