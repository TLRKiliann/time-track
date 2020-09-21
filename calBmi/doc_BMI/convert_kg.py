#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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

"""
# To test for deleting 0 befor number
print("\n+ To retrieve value from list1 !!!")
print(data_list1[0][0:2] + '\n')

data_perf = data_list1[0][0:2]
xcd = int(data_perf)
print(xcd)

print("\n+ To retrieve value from list1 !!!")
print(data_list1[0][0:2] + '\n')
"""

for (key, value) in data.items():
    print(key, value)
    print("\n")

data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Kg'])

dicolist = {}

for data_list1, data_list2 in zip(data_list1, data_list2):
    dicolist[data_list1] = data_list2

print("\nAffichage du dictionnaire :")
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

# Visual order of lists
print("La liste 1 correspond à : ", list1)
print("La liste 2 correspond à : ", list2)

print(list1[0])
print(list1[1])

#list3 = [int(list1) for list1 in list1]
list1 = list(map(float, list1))
list2 = list(map(float, list2))

print(list1)
# or seaborn-darkgrid
show_grid = True
with plt.style.context(('dark_background')):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(list1, list2, 'bo-')
    ax.set(title='Kg per date', ylabel='Kg', xlabel='Dates')
    #ax.xticks(rotation=45)
    ax.grid(show_grid)
    ax.xaxis_date()
    fig.autofmt_xdate()
    plt.show()
