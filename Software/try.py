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


import sqlite3

# Database connection
mydb = sqlite3.connect('sales_report.db')
mycursor = mydb.cursor()

# Function to read all data
def read_all_data():
    mycursor.execute("select *from boat")
    a=mycursor.fetchall()
    for i in a:
        print(i)

# Main function to execute the read operation
if __name__ == "__main__":
    read_all_data()

# import sqlite3

# # Database connection
# mydb = sqlite3.connect('Sales_pass.db')
# mycursor = mydb.cursor()

# Create table if it doesn't exist
# mycursor.execute('''
# CREATE TABLE IF NOT EXISTS Sales_pass (
#     Password TEXT
# )
# ''')
# mydb.commit()

# def get_latest_password():
#     mycursor.execute("SELECT Password FROM Sales_pass")
#     passwords = mycursor.fetchall()
#     if passwords:
#         return passwords[-1][0]
#     else:
#         # Insert the default password if the table is empty
#         default_password = "Aman@123"
#         mycursor.execute("INSERT INTO Sales_pass (Password) VALUES (?)", (default_password,))
#         mydb.commit()
#         return default_password

# def add_password(password):
#     mycursor.execute("INSERT INTO Sales_pass (Password) VALUES (?)", (password,))
#     mydb.commit()
# # Print the latest password
# latest_password = get_latest_password()
# print(f"The latest password is: {latest_password}")
# print(type(latest_password))
import sqlite3

# def insert_row(product_id, date_of_sale, product_name, product_model, category, mrp, product_sold):
#     try:
#         # Connect to the SQLite database
#         mydb = sqlite3.connect('sales_report.db')
#         mycursor = mydb.cursor()

#         # SQL query to insert a row into the "boat" table
#         sql = '''INSERT INTO boat (Product_ID, Date_of_sale, Product_Name, Product_Model, Category, MRP, Product_sold)
#                  VALUES (?, ?, ?, ?, ?, ?, ?)'''

#         # Data to be inserted into the table
#         data = (product_id, date_of_sale, product_name, product_model, category, mrp, product_sold)

#         # Execute the SQL query
#         mycursor.execute(sql, data)

#         # Commit the changes to the database
#         mydb.commit()

#         # Close the database connection
#         mydb.close()

#         print("Row inserted successfully.")
#     except sqlite3.Error as e:
#         print("Error inserting row:", e)

# # Example usage:
# insert_row("1001", "2024-05-19", "Rokerz", "255", "Neckband", 1500, 18)
# insert_row("1002", "2024-05-19", "Rokerz", "255+", "Neckband", 1100, 19)
# insert_row("1003", "2024-05-19", "Rokerz", "255 pro", "Neckband", 1800, 20)
# insert_row("1004", "2024-05-19", "AirBuds", "155", "AirBuds", 2100, 10)
# insert_row("1005", "2024-05-19", "AirBuds", "155", "AirBuds", 2200, 21)


