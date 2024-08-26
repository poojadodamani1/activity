# -*- coding: utf-8 -*-
"""activity

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q7-yrGRX8sB1R4KLX-0OSRWkqvW3pM74

import tkinter as tk from tkinter import messagebox import mysql.connector

def submit(): name = name_entry.get() reg = reg_entry.get()

if name and reg: try: db_config = { "host": "localhost", "user": "root", "password": "BVVS", "database": "pooja" } conn = mysql.connector.connect(**db_config) cursor = conn.cursor()

    query = "INSERT INTO library (name, reg) VALUES (%s, %s)"
    values = (name, reg)
    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Data submitted successfully!")
    clear_fields()

except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Database error: {err}")
else: messagebox.showwarning("Error", "Please fill in all fields.") def clear_fields(): name_entry.delete(0, tk.END) reg_entry.delete(0, tk.END)

def delete(): reg = reg_entry.get()

if reg: try: db_config = { "host": "localhost", "user": "root", "password": "BVVS", "database": "pooja" } conn = mysql.connector.connect(**db_config) cursor = conn.cursor()

    query = "DELETE FROM library WHERE reg = %s"
    values = (reg,)
    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Data deleted successfully!")
    clear_fields()

except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Database error: {err}")
else: messagebox.showwarning("Error", "Please enter the registration number.") def alter(): name = name_entry.get() reg = reg_entry.get()

if name and reg: try: db_config = { "host": "localhost", "user": "root", "password": "BVVS", "database": "pooja" } conn = mysql.connector.connect(**db_config) cursor = conn.cursor()

    query = "UPDATE library SET name = %s WHERE reg = %s"
    values = (name, reg)
    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

    messagebox.showinfo("Success", "Data updated successfully!")
    clear_fields()

except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Database error: {err}")
else: messagebox.showwarning("Error", "Please fill in all fields.") root = tk.Tk() root.title("Database GUI")

name_label = tk.Label(root, text="name:") reg_label = tk.Label(root, text="Registration:")

name_entry = tk.Entry(root) reg_entry = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=submit) clear_button = tk.Button(root, text="Clear", command=clear_fields) delete_button = tk.Button(root, text="Delete", command=delete) alter_button = tk.Button(root, text="Update", command=alter)

name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W) reg_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

name_entry.grid(row=0, column=1, padx=10, pady=10) reg_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button.grid(row=2, column=0, columnspan=1, pady=10) clear_button.grid(row=2, column=1, columnspan=1, pady=10) delete_button.grid(row=3, column=0, columnspan=1, pady=10) alter_button.grid(row=3, column=1, columnspan=1, pady=10)

root.mainloop()
"""

import pandas as pd
data=pd.read_csv('/content/tipps1.csv')
print(data)

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('/content/tipps1.csv')
plt.hist(data['day'],color='blue',alpha=0.7)
plt.xlabel('day')
plt.ylabel('Frequency')
plt.title('histplot')
plt.show()

plt.hist(data['day'],bins=10)
plt.hist(data['sex'],bins=10)
plt.show()

plt.scatter(x='day',y='tip',data=data)
plt.xlabel('day')
plt.ylabel('tip')
plt.show()

import matplotlib.pyplot as plt
plt.boxplot(data['tip'])
plt.show()

import matplotlib.pyplot as plt
x=data['tip']
y=data['day']
plt.bar(x,y,width=5)
plt.show()

import pandas as pd
data=pd.read_csv('/content/auto-mpg (1).csv')
print(data)

plt.hist(data['mpg'],color='blue',alpha=0.7)
plt.xlabel('mpg')
plt.ylabel('Frequency')
plt.title('histplot')
plt.show()

plt.hist(data['model-year'],bins=10)
plt.hist(data['mpg'],bins=10)
plt.show()

plt.scatter(x='cylinders',y='model-year',data=data)
plt.xlabel('mpg')
plt.ylabel('cylinders')
plt.show()

import matplotlib.pyplot as plt
plt.boxplot(data['mpg'])
plt.show()

import matplotlib.pyplot as plt
x=data['mpg']
y=data['weight']
plt.bar(x,y,width=5)
plt.show()

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('/content/auto-mpg.csv')
print(data)

mean=data['cylinders'].mean()
median=data['displacement'].median()
mode=stats.mode(data['mpg'])
print(" weight ")
print(mean)
print(median)
print(mode)

data_range = np.ptp(data['mpg'])
variance = np.var(data['mpg'])
std_deviation = np.std(data['mpg'])
iqr=np.percentile(data['mpg'],75)-np.percentile(data['mpg'],25)
print(" dispersion")
print("data_range",data_range)
print("variance",variance)
print("std_deviation",std_deviation)
print("iqr",iqr)

import seaborn as sns
plt.figure(figsize=(15, 5))
# Histogram
plt.subplot(131)
sns.histplot(data['mpg'], kde=True)
plt.title("Histogram of hp")
# Box plot
plt.subplot(132)
sns.boxplot(x='cylinders', data=data)
plt.title("Box Plot of hp")
plt.show()

import numpy as np
import pandas as pd
data=pd.read_csv('/content/tips.csv')
data.head()

missing_values=data.isnull().sum()
print("missing values:\n",missing_values)

from scipy import stats
import pandas as pd
df=pd.read_csv('/content/tips.csv')
df.describe()
zscore=stats.zscore(df['tip'])
threshold=2
outlier=abs(zscore)>threshold
print(outlier)

import matplotlib.pyplot as plt
import pandas as pd
data={
    'tips':[10,20,30,40,50,60,70,80,90,100],
}
data=pd.DataFrame(data)
z_score=(data['tips']-data['tips'].mean())/data['tips'].std()
threshold=3
outlier=data[(z_score>threshold)|(z_score<-threshold)]
plt.figure(figsize=(10,6))
plt.plot(data.index,data['tips'],'bo',label='data points')
plt.plot(outlier.index,outlier['tips'],'ro',label='outliers')
plt.xlabel("index")
plt.ylabel("tips")
plt.legend()
plt.show()

import pandas as pd
data=pd.read_csv('/content/tips.csv')
import matplotlib.pyplot as plt
plt.scatter(data['total_bill'],data['tip'])
plt.xlabel('total_bill')
plt.ylabel('tip')
plt.show()