#!/usr/bin/python3
# -*- coding:utf-8 -*-


import tkinter
from tkinter import *
import time
#import re
import json
import subprocess
from tkinter import messagebox
from itertools import *


def searchExpress():
    """
    To read in 2 files simultaneously
    """
    mot = regexpi_var.get()
    with open('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt', 'r') as textfile1:
        lines = textfile1.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if mot in line:
                print("Nous y voici !") 
                print(lines[i])
                print(lines[i+1])
                textBox.insert(INSERT, lines[i])
                textBox.insert(INSERT, lines[i+1])
                textBox.insert(INSERT, lines[i+2])
                    
    with open('./patient_agenda/events6/doc_events/fix_agenda/modifrdv.txt', 'r') as textfile2:
        lines = textfile2.readlines()
        for a in range(len(lines)):
            line = lines[a]
            if mot in line:
                print(lines[a])
                print(lines[a+1])
                textBox.insert(INSERT, "With modification of date :\n")
                textBox.insert(INSERT, lines[a])
                textBox.insert(INSERT, lines[a+1])
                textBox.insert(INSERT, lines[a+2])

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        save_input()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def save_input():
    """
    Save data from modification rdv textbox !
    To copy in 2 txt file simultaneously 
    since a read file and from text widget
    by lines ;) !
    """
    magicword = regexpi_var.get()
    with open('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt', 'r') as fr:
        with open('./patient_agenda/events6/doc_events/fix_agenda/modifrdv.txt', 'a+') as fw1:
            with open('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt', 'a+') as fw2:
                for line in fr.readlines():
                    if magicword in line:
                        fw1.writelines(str("\n+++ Changes about rdv +++\n"))
                        fw1.writelines(textBox.get('0.0', '12.0'))
                        fw2.writelines(str("\n+++ Changes about rdv +++\n"))
                        fw2.writelines(textBox.get('0.0', '12.0'))
                        print("Modification finish")
                        break
                    else:
                        print("None file has been writted")

def modifList():
    """
    To read file modifrdv.txt
    """
    subprocess.call('./patient_agenda/events6/doc_events/fix_agenda/read_filemodif.py')

def deleteTextbox():
    textBox.delete('0.0', '12.0')

def reorderFile():
    """
    To order list of dates
    and extract next line
    to rebuild a correct
    file in order
    """
    magicword = regexpi_var.get()            
    with open('./patient_agenda/events6/doc_events/fix_agenda/modifrdv.txt', 'r') as textfile2:
        lines = textfile2.readlines()
        for a in range(len(lines)):
            line = lines[a]
            if magicword in line:
                print(lines[a])
                print(lines[a+1])
                textBox.insert(INSERT, "With modification of date :\n")
                textBox.insert(INSERT, lines[a])
                textBox.insert(INSERT, lines[a+1])
                textBox.insert(INSERT, lines[a+2])

with open('./newpatient/entryfile6.txt', 'r') as filename:
    line1 = filename.readline()

gui = Tk()

gui.title("Save changes !")
gui.configure(bg='#82193e')

labelTit = Label(gui)
labelTit = Label(text="Save changes !", font=("Arial 16 bold"),
    fg='turquoise', bg='#82193e')
labelTit.grid(sticky='e', row=0, column=1, pady=10)

labelDate = Label(gui)
labelDate = Label(text='Search date to modify : ', font='12', 
    fg='cyan', bg='#82193e')
labelDate.grid(sticky='e', row=1, column=1)

textname = StringVar()
entryName = Entry(gui, textvariable=textname)
textname.set(line1)
entryName.grid(row=0, column=2, pady=10)

reachDate = Entry(gui)
regexpi_var = StringVar()
reachDate = Entry(textvariable=regexpi_var, highlightbackground='gray')
reachDate.grid(row=1, column=2, padx=5, pady=10)

buttonSearch = Button(gui)
buttonSearch = Button(text='Search', width=8, bd=3,
    fg='yellow', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command=searchExpress)
buttonSearch.grid(row=1, column=3, padx=5)

textBox = Text(gui, height=15, width=60, font=18)
textBox.grid(row=4, column=1, columnspan=3, padx=30, pady=30)

buttonSave = Button(gui, text="1-Save", width=8, bd=3,
    fg='yellow', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command = messFromSafeButt)
buttonSave.grid(sticky='w', row=5, column=1, padx=10, pady=10)

buttonModif = Button(gui, text="2-Read changes", width=12, bd=3,
    fg='yellow', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command = modifList)
buttonModif.grid(sticky='e', row=5, column=1, padx=10, pady=10)

buttonDelete = Button(gui, text="Clear", width=8, bd=3,
    fg='cyan', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command = deleteTextbox)
buttonDelete.grid(sticky='w', row=5, column=2, padx=10, pady=10)

buttonEnter = Button(gui, text="Add changes", width=10, bd=3,
    fg='cyan', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command = reorderFile)
buttonEnter.grid(sticky='e', row=5, column=2, pady=10)

buttonQuit = Button(gui)
buttonQuit = Button(text='Quit', width=8, bd=3,
    fg='white', bg='navy', highlightbackground='#82193e',
    activebackground='dark turquoise', command=quit)
buttonQuit.grid(sticky='e', row=5, column=3, padx=10, pady=10)

gui.mainloop()
