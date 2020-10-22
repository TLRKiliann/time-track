#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


fen=Tk()
fen.title("Results of Medical Visit")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(fen, bg='cyan')
bottom = Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Results of Medical Visit for : ",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

# To display name in Entry widget
with open('./newpatient/entryfile15.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
text_name.set(line1)
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='cyan')
labelallergy.pack(padx=5, pady=5)

# To display allergy in Entry widget
with open('./allergy/allergyfile15.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()
    lineA6=allerfile.readline()
    lineA7=allerfile.readline()

text_aller=StringVar()
text_aller.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
Entryall=Entry(fen, textvariable=text_aller, width=60)
Entryall.pack(padx=10, pady=5)

def importationFile(fichier, encodage="Utf-8"):
    with open(fichier, 'r', encoding=encodage) as filer:
        content = filer.readlines()
        for li in content:
            textBox.insert(END, li)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='cyan', bg='navy', highlightbackground='grey17',
    activebackground='dark turquoise', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./vmed/doc_vmed15/resultvmed15.txt'):
        importationFile('./vmed/doc_vmed15/resultvmed15.txt',
            encodage="Utf-8")
except FileNotFoundError as err_file:
    print("+ File not found !", err_file)
    messagebox.showwarning("WARNING", "File does not exist or "
        "file not found !")

fen.mainloop()
