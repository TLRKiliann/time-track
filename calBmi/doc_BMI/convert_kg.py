#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime
import time


file = open('./calBmi/doc_BMI/file_kg.json')
data = json.load(file)
#file.close

for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))
    print("\nTo represent the data_get:\n")
    print(data.get("data"))
    print("\n")
    print("Valeur: " + str(value[0]))
    print("Valeur: " + str(value[1]))
    print("\n")
    print("Date: " + str(value[0]["Date"]))
    print("Kg: " + str(value[0]["Kg"]))
    print("\n")
    print("Date: " + str(value[1]["Date"]))
    print("Kg: " + str(value[1]["Kg"]))
    
data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Date'])

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList of weight\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Kg'])

dicolist = {}

for data_list1, data_list2 in zip(data_list1, data_list2):
    dicolist[data_list1] = data_list2

print("\nDisplay dictionary :")
print("---------------------------")
print(dicolist)

list1 = []
list2 = []

for key, value in dicolist.items():
    list1.append(key)
    list2.append(value)
    
print("\nList of dates :")
print("----------------------------------")
print(list1)

print("\nList of weight :")
print("------------------------")
print(list2)

#list3 = [int(list2) for list2 in list2]
list2 = list(map(float, list2))
list1 = list(map(str, list1))
#list1.sort(key=lambda date: datetime.strptime(date, "%d-%m-%y"))
"""
converted_dates = list(map(datetime.datetime.strptime, list1, len(list1)*['%d-%m-%Y']))
x_axis = converted_dates
formatter = dates.DateFormatter('%d-%m-%Y')
y_axis = list2
show_grid = True
with plt.style.context('dark_background'):
    plt.plot(x_axis, y_axis, '-')
    ax = plt.gcf().axes[0] 
    ax.xaxis.set_major_formatter(formatter)
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg per date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=25)

    plt.show()



"""
# second example
print(list1[0])

list_data=str(list1[0])

list_convert = datetime.datetime.strptime(list_data, "%d-%m-%Y")
int_date = date2num(list_convert)

print(int_date)

figure, axes = plt.subplots() 
axes.bar(int_date, list2, label ="", color ="cyan") 

locator = AutoDateLocator() 
axes.xaxis.set_major_locator(locator) 
axes.xaxis.set_major_formatter(AutoDateFormatter(locator))

# apply autoformatter for displaying of dates 
min_date = date2num(datetime.datetime.strptime('01-01-20', "%d-%m-%Y")) 
max_date = date2num(datetime.datetime.strptime('28-12-20', "%d-%m-%Y")) 
axes.set_xlim([min_date, max_date]) 
figure.autofmt_xdate() 
  
# show plot:  
plt.show() 

#fig=Figure()
#ax=fig.add_subplot(111)
# or seaborn-darkgrid
show_grid = True
with plt.style.context('dark_background'):
    plt.plot_date(list1, list2, '-')
    ax.xaxis.set_major_formatter(DateFormatter("%d-%m-%y"))
    fig.autofmt_xdate()
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg per date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)
    plt.show()
