#!/usr/bin/python3
#!-*-encoding:utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def importationFile2(fichier2, encodage="Utf-8"):
    file2 = open(fichier2, 'r', encoding=encodage)
    content=file2.readlines()
    file2.close()
    for li2 in content:
        textBox.insert(END, li2)

fen=Tk()
fen.title("Historic of ttt")
fen.configure(background='RoyalBlue4')

# To place side by side labelo + entrylab
top = Frame(fen, bg='RoyalBlue4')
bottom = Frame(fen, bg='RoyalBlue4')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Historic of ttt : ", width=15,
    font='Times 18 bold', fg='cyan', bg='RoyalBlue4')
labelo.pack(in_=top, side=LEFT, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='RoyalBlue4')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile22.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
text_name.set(line1)
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, pady=20)

# To read allergy in Entry widget
with open('./allergy/allergyfile22.txt', 'r') as allerfile:
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

buttonClose=Button(fen, text="Quit", width=10, bd=3, fg='white', 
    bg='RoyalBlue3', highlightbackground='RoyalBlue4',
    activebackground='dark turquoise', 
    activeforeground='navy', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    if os.path.getsize('./ttt/doc_ttt22/intro_ttt.txt'):
        importationFile('./ttt/doc_ttt22/intro_ttt.txt', encodage="Utf-8")
except FileNotFoundError as no_file:
    print("+ File intro_ttt not found !")
    messagebox.showinfo('INFO', 'File intro_ttt not found !')

try:
    if os.path.getsize('./ttt/doc_ttt22/intro_res.txt'):
        importationFile2('./ttt/doc_ttt22/intro_res.txt', encodage="Utf-8")
except FileNotFoundError as no_file:
    print("+ File intro_res not found !")
    messagebox.showinfo('INFO', 'File intro_res not found !')

fen.mainloop()
