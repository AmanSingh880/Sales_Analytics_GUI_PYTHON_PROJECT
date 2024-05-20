from tkinter import *
import os
import sqlite3
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

# Database connection
mydb = sqlite3.connect('sales_report.db')
mycursor = mydb.cursor()

# Create table if it doesn't exist
mycursor.execute('''
CREATE TABLE IF NOT EXISTS boat (
    Product_ID TEXT,
    Date_of_sale TEXT,
    Product_Name TEXT,
    Product_Model TEXT,
    Category TEXT,
    MRP INTEGER,
    Product_sold INTEGER
)
''')
mydb.commit()

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
    mycursor.execute("SELECT DISTINCT Category FROM boat")
    categories = [row[0] for row in mycursor.fetchall()]
    return categories

def back_sh():
    root.destroy()
    os.system("main.py")

def on_menu_select(value):
    mycursor.execute("SELECT Date_of_sale, Product_sold FROM boat WHERE Category = ?", (value,))
    rows = mycursor.fetchall()

    dates = [row[0] for row in rows]
    sales = [row[1] for row in rows]

    # Data processing and visualization
    fig = Figure(figsize=(6, 5), dpi=110)
    plot1 = fig.add_subplot(111)
    plot1.plot(dates, sales, marker='*', color='blue', linestyle='-.')
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
options = show_categories()
dropdown = OptionMenu(root, selected_option, *options, command=on_menu_select)
dropdown.place(x=100,y=200)

b2=Button(text="back",bg="blue",fg="white",font="Airtel 15",command=back_sh)
b2.place(x=50,y=650)

root.mainloop()
