#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import time
import os
import subprocess


root=Tk()
root.title("Diagnostics and ATCD")
root.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(root, bg='cyan')
bottom = Frame(root, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile15.txt', 'r') as filename:
    line1=filename.readline()

textname=StringVar()
entryName=Entry(root, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='cyan')
labelallergy.pack(padx=5, pady=10)

with open('./allergy/allergyfile15.txt', 'r') as filename:
    lineA1=filename.readline()
    lineA2=filename.readline()
    lineA3=filename.readline()
    lineA4=filename.readline()
    lineA5=filename.readline()
    lineA6=filename.readline()
    lineA7=filename.readline()

entrytext=StringVar()
entrytext.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
entryName=Entry(root, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

def retrieve_input():
    file = open('./diag/doc_diag15/diagrecap15.txt', 'a+')
    file.write(textBox.get("1.0","end-1c") + "\n\n")
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
    file = open('./diag/doc_diag15/diagrecap15.txt', 'r')
    print(file.read())
    file.close()
    subprocess.call('./diag/doc_diag15/diag_read.py')

def ajouterText():
    textBox.delete('1.0', END)
    textBox.insert(INSERT, "En date du : ")
    textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :") + '\n')
    textBox.update()

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
#textBox.insert(INSERT, "En date du : ")
#textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", fg='cyan', bg='navy',
    activebackground='dark turquoise', activeforeground='navy',
    bd=3, highlightbackground='grey17', command=lectureFic)
buttonLire.pack(side='left', padx=10, pady=10)

buttonAjouter=Button(root, text="1-Add", fg='yellow', bg='navy',
    activebackground='dark turquoise', activeforeground='navy',
    bd=3, highlightbackground='grey17', command=ajouterText)
buttonAjouter.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="2-Save", fg='yellow', bg='navy',
    activebackground='dark turquoise', activeforeground='navy',
    bd=3, highlightbackground='grey17', command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", fg='white', bg='navy',
    width=10, activebackground='cyan', activeforeground='navy',
    bd=3, highlightbackground='grey17', command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./diag/doc_diag15/diagrecap15.txt'):
        importationFile('./diag/doc_diag15/diagrecap15.txt', 
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print("+ File not found !", err_file)
    messagebox.showwarning("WARNING", "File does not exist or " 
        "file not found !")

mainloop()
