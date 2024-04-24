import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="sales_report"
  )

mycursor = mydb.cursor()

mycursor.execute("Select date_of_sale,product_sold from boat")
l=[]
d=[]
for x in mycursor:
  l.append(x[1])
  d.append(x[0])
import datetime
l+=[34,36,26]

# Assuming your list is defined as follows
date_list = d

# Extract date and month separately
dates = [12,13,14,15,16,17]
months = [date.month for date in date_list]

import numpy as np
import matplotlib.pyplot as plt
y=np.array(l)
x=np.array(dates)
plt.plot(x,y)
plt.ylabel("No of products")
plt.xlabel("date")
plt.show()
