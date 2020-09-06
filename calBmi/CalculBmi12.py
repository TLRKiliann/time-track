#!/usr/bin/python3
#!-*-encoding:utf-8-*-

"""
Interface pour calculer le BMI
Avec indication si trop haut ou
trop bas
"""

from tkinter import *
import tkinter
from functools import partial
from tkinter import messagebox
import time
import os
import subprocess
import json
import io
import shutil


def call_result(textBox, number1, number2):
    num1 = float((number1.get()))
    num2 = float((number2.get()))
    result = (num1)/(num2*num2)
    if result<=18.5:
        textBox.config(text="Vous êtes en souspoids.\n"
                                 "Votre BMI (IMC) est de : %d" % result)
        return
    elif result >= 18.5 and result <= 25:
        textBox.config(text="Votre BMI est dans les normes.\n"
                                 "Votre BMI (IMC) est de : %d" % result)
        return
    elif result >= 18.5 and result <= 25:
        textBox.config(text="Votre BMI est dans les normes.\n"
                                 "Votre BMI (IMC) est de : %d" % result)
        return
    else:
        textBox.config(text="Vous êtes en surpoids.\n"
                                 "Votre BMI (IMC) est de : %d" % result)  
        return

def buttRecord():
    """
    Pour rentrer le BMI
    """
    num1 = float((number1.get()))
    num2 = float((number2.get()))
    result = (num1)/(num2*num2)

    with open('./calBmi/bmi12.txt', 'a+') as file:
        file.write(str("Date : "))
        file.write(textDate.get() + "\n")
        file.write(str("Heure : "))
        file.write(textHour.get() + "\n")
        file.write(str("Prenom et Nom : "))
        file.write(textName.get())
        file.write(str("Poids : "))
        file.write(number1.get() + "\n")
        file.write(str("Taille : "))
        file.write(number2.get() + "\n")
        file.write(str("BMI : "))
        file.write(str(result))
        file.write("\n\n")
        file.close()

    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_bmi.json'):
            print("+ File 'BMI' exist !")
            with open('./calBmi/doc_BMI12/file_bmi.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataBmi = datastore
            dataBmi['data'].append({'Date' : textDate.get(), 'BMI' : result})
            with open('./calBmi/doc_BMI12/file_bmi.json', 'w') as datafile2:
                json.dump(dataBmi, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file file_bmi.json not exist !')
        print(str(outcom))
        print("+ File file_bmi.json created !")
        dataBmi = {}
        dataBmi['data'] = []
        dataBmi['data'].append({'Date' : textDate.get(), 'BMI' : result})
        with open('./calBmi/doc_BMI12/file_bmi.json', 'w') as datafile:
            json.dump(dataBmi, datafile, indent=4)

    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_kg.json'):
            print("+ File 'Kg' exist !")
            with open('./calBmi/doc_BMI12/file_kg.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataBmi = datastore
            dataBmi['data'].append({'Date' : textDate.get(), 'Kg' : number1.get()})
            with open('./calBmi/doc_BMI12/file_kg.json', 'w') as datafile2:
                json.dump(dataBmi, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file file_kg.json not exist !')
        print(str(outcom))
        print("+ File file_kg.json created !")
        dataBmi = {}
        dataBmi['data'] = []
        dataBmi['data'].append({'Date' : textDate.get(), 'Kg' : number1.get()})
        with open('./calBmi/doc_BMI12/file_kg.json', 'w') as datafile:
            json.dump(dataBmi, datafile, indent=4)

    messagebox.showinfo('Record', 'Data saved')

def viewGraphicBmi():
    subprocess.call('./calBmi/doc_BMI12/convert_bmilist.py')

def viewGraphicKilo():
    subprocess.call('./calBmi/doc_BMI12/convert_kg.py')

def readBmi():
    subprocess.call('./calBmi/bmi_read12.py')

def buttdel():
    """
    To earase last line 
    of tensor.json
    """
    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_bmi.json'):
            with open('./calBmi/doc_BMI12/file_bmi.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of bmi deleted")
                print(value[-1])
                del value[-1]
            with open('./calBmi/doc_BMI12/file_bmi.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            print("Last value of 'file_bmi.json' has been deleted !")
    except FileNotFoundError:
        print('+ Sorry, file asked not exist !')

    try:
        if os.path.getsize('./calBmi/doc_BMI12/file_kg.json'):
            with open('./calBmi/doc_BMI12/file_kg.json', 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                print("Last value of weight deleted")
                print(value[-1])
                del value[-1]
            with open('./calBmi/doc_BMI12/file_kg.json', 'w') as file:
                data = json.dump(data, file, indent=4)
            print("Last value of 'file_kg.json' has been deleted !")
    except FileNotFoundError:
        print('+ Sorry, file asked not exist !')

# To read name of patient for entry widget
with open('./newpatient/entryfile12.txt', 'r') as filename:
    line1=filename.readline()

gui = Tk()
gui.title('Simple BMI calculator')
gui.configure(background='RoyalBlue4')

labelTitle = Label(gui, text="Simple BMI", font='Arial 18 bold', 
    fg='aquamarine', bg='RoyalBlue4')
labelTitle.grid(row=0, column=1, columnspan=2, pady=10)

number1 = StringVar()
number2 = StringVar()

textDate = Label(gui, text="Date : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
textDate.grid(row=1, column=1)

textHour = Label(gui, text="Heure : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
textHour.grid(row=2, column=1)

textName = Label(gui, text="Nom du patient : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
textName.grid(row=3, column=1)

labelNum1 = Label(gui, text="Entrez le poids en Kg : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
labelNum1.grid(row=4, column=1)

labelNum2 = Label(gui, text="Entrez la taille en M : ",
    font=18, width=20, fg='cyan', bg='RoyalBlue4', anchor='e')
labelNum2.grid(row=5, column=1)

textDate = Entry(gui)
time_string = IntVar() 
textDate = Entry(textvariable=time_string, highlightbackground='gray', bd=4)
time_string.set(time.strftime("%d/%m/%Y"))
textDate.grid(row=1, column=2)

textHour = Entry(gui)
time_Htring = IntVar()
textHour = Entry(textvariable=time_Htring, highlightbackground='gray', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=2, column=2)

textName = Entry(gui)
name_text = StringVar()
textName = Entry(textvariable=name_text, highlightbackground='gray', bd=4)
name_text.set(line1)
textName.grid(row=3, column=2)

entryNum1 = Entry(gui)
number1 = StringVar()
entryNum1 = Entry(gui, textvariable=number1, highlightbackground='gray', bd=4)
entryNum1.grid(row=4, column=2)

entryNum2 = Entry(gui)
number2 = StringVar()
entryNum2 = Entry(gui, textvariable=number2, highlightbackground='gray', bd=4)
entryNum2.grid(row=5, column=2)

textBox = Label(gui, height=3, width=40, font=12, relief=SUNKEN)
textBox.grid(row=6, column=1, columnspan=2, pady=10)

call_result = partial(call_result, textBox, number1, number2)

buttonCal = Button(gui, text="1-Calcul", width=12, fg='yellow',
    bg='turquoise4', activeforeground='gray40',
    activebackground='turquoise2', command=call_result)
buttonCal.grid(sticky='w', row=10, column=1)

buttonCal = Button(gui, text="2-Save", width=12, fg='yellow',
    bg='turquoise4', activeforeground='gray40',
    activebackground='turquoise2', command=buttRecord)
buttonCal.grid(sticky='w', row=11, column=1)

buttonCal = Button(gui, text="Cancel last check", width=12, fg='yellow',
    bg='coral', activeforeground='white',
    activebackground='red', command=buttdel)
buttonCal.grid(row=11, column=1, columnspan=2)

buttonCal2 = Button(gui, text="Read", width=12, fg='light blue',
    bg='turquoise4', activebackground='dark turquoise',
    command=readBmi)
buttonCal2.grid(sticky='w', row=12, column=1)

buttonCal = Button(gui, text="Graph BMI", width=12, fg='blue2',
    bg='turquoise3', activeforeground='gray30',
    activebackground='turquoise', command=viewGraphicBmi)
buttonCal.grid(sticky='e', row=10, column=2)

buttonCal = Button(gui, text="Graph Weight", width=12, fg='blue2',
    bg='turquoise3', activeforeground='gray30',
    activebackground='turquoise', command=viewGraphicKilo)
buttonCal.grid(sticky='e', row=11, column=2)

buttonCal2 = Button(gui, text="Quit", width=12, fg='cyan',
    bg='gray30', activebackground='dark turquoise',
    command=quit)
buttonCal2.grid(sticky='e', row=12, column=2)

gui.mainloop()
