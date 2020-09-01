#!/usr/bin/python3
#!-*-encoding:Utf-8-*-

from tkinter import *


def importationFile(fichier):
    file = open(fichier, 'r')
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def saveData():         
    with open('./patient_agenda/events7/doc_events/fix_agenda/modifrdv.txt', 'w') as textfile2:
        textfile2.writelines(textBox.get('0.0', '12.0'))

with open('./newpatient/entryfile7.txt', 'r') as filename:
    line1=filename.readline()

fen=Tk()
fen.title("RDV have changed")
fen.configure(background='#82193e')

# To place side by side labelo + entrylab
top=Frame(fen, bg='#82193e')
bottom=Frame(fen, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="RDV have changed",
    font='Arial 18 bold', fg='turquoise', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

textname=StringVar()
entryName=Entry(fen, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

textBox=Text(fen, height=15, width=60, font=18)
textBox.pack(padx=30, pady=30)

buttonSave=Button(fen, text="Save", width=8, bd=3,
    fg='yellow', bg='navy',
    activebackground='dark turquoise', 
    highlightbackground='#82193e', command=saveData)
buttonSave.pack(side='left', padx=10, pady=10)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='navy', activebackground='dark turquoise',
    highlightbackground='#82193e', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./patient_agenda/events7/doc_events/fix_agenda/modifrdv.txt')

fen.mainloop()
