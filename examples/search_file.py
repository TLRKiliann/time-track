#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import json
import os
import time
import datetime


"""
2 methods to search a line which content a word in a file
"""
# In a txt file
try:
    with open('./newpatient/entryfile3.txt', 'r') as namefile:
        line3=namefile.readline()
        ttt_text3=line3
except FileNotFoundError as fileout3:
    print("No file entryfile3.txt exist", fileout3)

try:
    word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
    initword = "Date of end : "
    with open('./ttt/doc_ttt3/intro_ttt.txt', 'r') as filedate:
        lines = filedate.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            if initword in line:
                print(line)
                if word_treattostop in line:
                    print(line)
                    MSBTTT2 = messagebox.showwarning('Info',
                        'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text3 + \
                        lines[i] + lines[i-6] + lines[i-5])
except FileNotFoundError as info_ttt3:
    print("No date of end has been found for ttt into file intro_ttt.txt (patient 3)", info_ttt3)
else:
    ("Error unknow 3")

# In a json file
try:
    word_ttstop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
    file = open('./ttt/doc_ttt/convdose.json')
    data=json.load(file)
    for (key, value) in data.items():
        data_x = [0 , 1 , 2 , 3 , 4 , 5 , 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for x in data_x:
            print(str(value[x]["Date of end"]))
            date_end = (str(value[x]["Date of end"]))
            if date_end == word_ttstop:
                print(date_end)
                name_treat = (str(value[x]["Treatment"]))
                print(name_treat)
                dose_ttt = (str(value[x]["Dosage"]))
                print(dose_ttt)
                MSBTTT2 = messagebox.showwarning('Warning',
                    'Look at TTT, there is a ttt to stop at' + " " + word_ttstop + " " + \
                    'for : ' + "\n" + line_text1 + "Date of end : " + date_end + "\n" + name_treat + \
                    "\n" + dose_ttt) 
except IndexError as error_ttt:
    print("No date of end has been found for ttt into file intro_ttt.txt (patient 1)", error_ttt)
except FileNotFoundError as info_ttt:
    print("No date of end has been found for ttt into file intro_ttt.txt (patient 1)", info_ttt)
else:
    ("Error unknow 1")
