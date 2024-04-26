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


# Assuming your list is defined as follows
date_list = d

# Extract date and month separately
dates = [date.day for date in date_list]
months = [date.month for date in date_list]
di={}
dl=[]
for i in range(len(d)):
  di[dates[i]]+=list(l[i])


import numpy as np
import matplotlib.pyplot as plt
y=np.array(l)
x=np.array(dates)
plt.plot(x,y)
plt.ylabel("No of products")
plt.xlabel("date")
plt.show()

