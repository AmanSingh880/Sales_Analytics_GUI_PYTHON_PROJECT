from tkinter import *
import os
from tkinter import messagebox
import sqlite3
from datetime import datetime as z
from matplotlib.figure import Figure 
from datetime import datetime
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

def show_dates():
    mycursor.execute("SELECT DISTINCT date_of_sale FROM boat")
    dates = [datetime.strptime(row[0], '%Y-%m-%d').strftime("%x") for row in mycursor.fetchall()]
    return dates
def on_menu_select(value):
    mycursor.execute("SELECT product_id, product_sold FROM boat WHERE date_of_sale = ?", (value,))
    data = mycursor.fetchall()
    product_ids = [row[0] for row in data]
    sales = [row[1] for row in data]

    # Data processing and visualization
    fig = Figure(figsize=(6, 5), dpi=110)
    plot1 = fig.add_subplot(111)
    # Add your plot code here

    # Update canvas with new figure
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Since we're updating the canvas dynamically, destroy the old one if exists
    if hasattr(root, 'canvas'):
        root.canvas.get_tk_widget().destroy()
    root.canvas = canvas

    return fig  # Return fig to access it outside the function

# Remove this line from your code:
# plot1 = fig.add_subplot(111)

# Add this line to create a global fig variable that can be accessed from other functions
fig = None


def back_sh():
    root.destroy()
    os.system("main.py")

root=Tk()
root.title("Sales analytic")
root.geometry('1200x750')
root.configure(bg='#51007d')
l=Label(root,text="Sales Analytics",font="Airtel 34",bg="blue", fg="white")
l.pack()
selected_option = StringVar()
selected_option.set("Date")
options =show_dates();
dropdown = OptionMenu(root, selected_option, *options,command=on_menu_select)
dropdown.place(x=100,y=200)
b2=Button(text="back",bg="blue",fg="white",font="Airtel 15",command=back_sh)
b2.place(x=50,y=650)
root.mainloop()
