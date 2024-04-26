import mysql.connector
from datetime import datetime as z

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

class data_entry_class():
    def __init__(self):
        self.Product_ID = None
        self.Date = None
        self.Product_Name = None
        self.Product_Model = None
        self.Category = None
        self.MRP = None
        self.Product_sold = None

a = data_entry_class()
a.Product_ID = "1004"
given_date=z.now().date()
year = given_date.year
month = given_date.month
day = given_date.day
a.Date = str(year)+"/"+str(month)+"/"+str(day)
a.Product_Name = "Rockerz"
a.Product_Model = "280"
a.Category = "Earbud"
a.MRP = 1500
a.Product_sold = 28

# passed(a)
