#!/usr/bin/python3
# -*- coding:utf-8 -*-


import tkinter
from tkinter import *
import subprocess
import time
from tkinter import messagebox


def importationFile(fichier):
    file = open(fichier, 'r')
    content = file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)
        textBox.insert(END, '\n')
        textBox.delete('2.0')
        textBox.delete('end-3c')
        textBox.update()

def retrieve_input():
    inputValue = textBox.get("1.0","end-1c" + '\n')
    print(inputValue)
    file = open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'a+')
    file.write(textBox.get("1.0","end-1c") + '\n\n')
    file.close()
    
def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        retrieve_input()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def lectureFic():
    file = open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'r')
    print(file.read())
    file.close()
    subprocess.call('./patient_agenda/events/doc_events/fix_agenda/read_file.py')

def changeText():
    subprocess.call('./patient_agenda/events/doc_events/fix_agenda/main.py')

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1=filename.readline()

fen=Tk()
fen.title("Agenda")
fen.configure(background='#82193e')

# To place side by side labelo + entrylab
top=Frame(fen, bg='#82193e')
bottom=Frame(fen, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Agenda",
    font='Arial 18 bold',
    fg='turquoise', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

textname=StringVar()
entryName=Entry(fen, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(fen, height=15, width=60, font=18)
textBox.insert(INSERT, "Current date : ")
textBox.insert(END, time.strftime("%d/%m/%Y, %H:%M:%S") + ' :\n')
textBox.pack(padx=30, pady=30)

buttonEnter=Button(fen, text="Save", width=8, bd=3,
    fg='yellow', bg='navy',activebackground='dark turquoise',
    highlightbackground='#82193e', command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonLire=Button(fen, text="Read", width=8, bd=3,
    fg='cyan', bg='navy', activebackground='dark turquoise',
    highlightbackground='#82193e', command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEffacer=Button(fen, text="Change RDV", width=10, bd=3,
    fg='cyan', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command=changeText)
buttonEffacer.pack(side='left', padx=10, pady=10)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./patient_agenda/events/doc_events/fix_agenda/patient_value.json')

fen.mainloop()
