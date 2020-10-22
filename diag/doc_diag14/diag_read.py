#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


fen=Tk()
fen.title("Diagnostics and ATCD")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(fen, bg='cyan')
bottom = Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile14.txt', 'r') as filename:
    line1=filename.readline()

entrytext=StringVar()
entrytext.set(line1)
entryName=Entry(fen, textvariable=entrytext)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='cyan')
labelallergy.pack(padx=5, pady=10)

with open('./allergy/allergyfile14.txt', 'r') as filename:
    lineA1=filename.readline()
    lineA2=filename.readline()
    lineA3=filename.readline()
    lineA4=filename.readline()
    lineA5=filename.readline()
    lineA6=filename.readline()
    lineA7=filename.readline()

entrytext=StringVar()
entrytext.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
entryName=Entry(fen, textvariable=entrytext, width=60)
entryName.pack(padx=10, pady=10)

def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", fg='white', width=10, bd=3,
    bg='navy', activebackground='dark turquoise', activeforeground='navy', 
    highlightbackground='grey17', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./diag/doc_diag14/diagrecap14.txt'):
        importationFile('./diag/doc_diag14/diagrecap14.txt',
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print("+ File not found !", err_file)
    messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

fen.mainloop()
