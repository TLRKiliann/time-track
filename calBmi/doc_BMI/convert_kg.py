#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib.dates import date2num
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import AutoDateFormatter
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

list2 = list(map(float, list2))
list1 = list(map(str, list1))

converted_dates = list(map(datetime.datetime.strptime, list1, len(list1)*['%d-%m-%Y']))
x_axis = converted_dates
formatter = dates.DateFormatter('%d-%m-%Y')
y_axis = list2

"""
A revoir et à corriger.
Il s'agit là d'un algo 
pour une année^d'affichage.
"""

show_grid = True
with plt.style.context('dark_background'):
    figure, axes = plt.subplots()
    # apply autoformatter for displaying of dates 
    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    ax = plt.gcf().axes[0]
    ax.xaxis.set_major_formatter(formatter)
    #axes.xaxis.set_major_formatter(AutoDateFormatter(locator))
    min_date = date2num(datetime.datetime.strptime('01-01-2020', "%d-%m-%Y"))
    max_date = date2num(datetime.datetime.strptime('31-12-2020', "%d-%m-%Y"))
    axes.set_xlim([min_date, max_date])
    #figure.autofmt_xdate()

    plt.plot(x_axis, y_axis, 'ro-')
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg/Date for 1 year')
    #plt.xticks(rotation=45)
    plt.legend(['kg/date'])
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()

"""
figure, axes = plt.subplots()
axes.bar(int_date, list2, label ="", color ="cyan")
"""
#ax=fig.add_subplot(111)

# or seaborn-darkgrid
show_grid = True
with plt.style.context('dark_background'):
    figure, axes = plt.subplots()

    locator = AutoDateLocator()
    axes.xaxis.set_major_locator(locator)
    ax = plt.gcf().axes[0]
    ax.xaxis.set_major_formatter(formatter)
    min_date = date2num(datetime.datetime.strptime('01-08-2020', "%d-%m-%Y"))
    max_date = date2num(datetime.datetime.strptime('30-08-2020', "%d-%m-%Y"))
    axes.set_xlim([min_date, max_date])

    plt.plot(x_axis, y_axis, 'cyan')
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg/Date for 1 month')
    #plt.xticks(rotation=45)
    plt.legend(['kg/date'])
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=45)
    plt.show()
