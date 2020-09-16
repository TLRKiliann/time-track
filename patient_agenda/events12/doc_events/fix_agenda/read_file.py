#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox


with open('./newpatient/entryfile12.txt', 'r') as filename:
    line1=filename.readline()

def importationFile(fichier):
    file = open(fichier, 'r')
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def msgBox():
    messagebox.showwarning('WARNING',
        'No fixed_rdv.txt file exist for : ' + line1)

fen=Tk()
fen.title("RDV set up")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(fen, bg='cyan')
bottom = Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="RDV set up",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

textentry=StringVar()
textentry.set(line1)
entrylab=Entry(fen, textvariable=textentry)
entrylab.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='navy', highlightbackground='light sky blue',
    activebackground='dark turquoise', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    importationFile('./patient_agenda/events12/doc_events/fix_agenda/fixed_rdv.txt')
except FileNotFoundError as fixed:
    print("+ No fixed_rdv.txt file exist !", fixed)
    msgBox()

fen.mainloop()
