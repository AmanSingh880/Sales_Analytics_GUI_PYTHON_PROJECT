import pickle
from tkinter import messagebox
from tkinter import messagebox
import mysql.connector
from datetime import datetime as z

def Validate_password(password):
    try:
        file=open("binary.bin","rb")
        original_password=pickle.load(file)
        if(original_password==password):
            file.close()
            return True
        else:
            messagebox.showwarning("Sales Analytic","Incorrect Password")
            file.close()
            return False
    except:
        messagebox.showwarning("Sales Analytic","Data not Found")
    finally:
        return False
        
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
        file=open("binary.bin","wb")
        pickle.dump(password,file)
        file.close()
        messagebox.showwarning("Sales Analytic","Password Changed")
        return True
    else:
        return False
###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################
#Product Name	Product_Model	category	MRP	product_sold
class data_entry_class():
    def __init__(self):
        self.Product_ID=None
        self.Date=None
        self.Product_Name=None
        self.Product_Model=None
        self.Category=None
        self.MRP=None
        self.Product_sold=None
    #provide getter and setter method in it or pass it 
    
a=data_entry_class()



###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="sales_report"
)
mycursor = mydb.cursor()

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



###########################################################################################################################################
###########################################################################################################################################
###########################################################################################################################################

def show_dates():
    mycursor.execute("Select date_of_sale from boat")
    d=[]
    for x in mycursor:
        d.append(x[0])
    dates = [date.day for date in d]
    return list(set(dates))


def show_categories():
    mycursor.execute("Select Distinct category from boat")
    cat=[]
    for x in mycursor:
        cat.append(x[0])
    return cat
    
    ####################################\


import tkinter as tk
from tkinter import messagebox

def on_menu_select(value):
    messagebox.showinfo("Selected Option", f"You selected: {value}")

root = tk.Tk()
root.title("Dropdown Menu Example")

selected_option = tk.StringVar()
selected_option.set("Option 1")  # Set default selected option

options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create dropdown menu
dropdown = tk.OptionMenu(root, selected_option, *options, command=on_menu_select)
dropdown.pack(padx=20, pady=20)

root.mainloop()

    
    
  





















