#!/usr/bin/python3
#!-*-encoding:utf-8-*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def msgBox():
    MSB=messagebox.showinfo('Info', 'File bmi10.txt does not exist')

fen=Tk()
fen.title("BMI results")
fen.configure(background='RoyalBlue4')

# To place side by side labelo + entrylab
top = Frame(fen, bg='RoyalBlue4')
bottom = Frame(fen, bg='RoyalBlue4')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="BMI results : ", width=15,
    font='Times 18 bold', fg='cyan', bg='RoyalBlue4')
labelo.pack(in_=top, side=LEFT, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='RoyalBlue4')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile10.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
text_name.set(line1)
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, pady=20)

# To read allergy in Entry widget
with open('./allergy/allergyfile10.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()
    lineA6=allerfile.readline()
    lineA7=allerfile.readline()

text_all=StringVar()
text_all.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
Entryall=Entry(fen, textvariable=text_all, width=60)
Entryall.pack(padx=10, pady=5)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=10, fg='cyan', 
    bg='gray30', activebackground='dark turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    importationFile('./calBmi/bmi10.txt', encodage="Utf-8")
except FileNotFoundError as error_call:
    print("+ importationFile bmi10.txt " + line1 + " failed !")
    msgBox()

fen.mainloop()
