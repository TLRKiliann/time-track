#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import time
import matplotlib.pyplot as plt


file = open('./calBmi/doc_BMI2/file_kg.json')
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

# or seaborn-darkgrid
show_grid = True
with plt.style.context(('dark_background')):
    plt.plot(list1, list2)
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg per date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)
    plt.show()
