#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox


with open('./newpatient/entryfile16.txt', 'r') as filename:
    line1=filename.readline()

def importationFile(fichier):
    file = open(fichier, 'r')
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

def saveData():         
    with open('./patient_agenda/events16/doc_events/fix_agenda/modifrdv.txt', 'w') as textfile2:
        textfile2.writelines(textBox.get("0.0", "end-1c") + "\n")

def msgBox2():
    messagebox.showwarning('WARNING',
        'No modifrdv.txt file exist for : ' + line1)

fen=Tk()
fen.title("RDV have changed")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top=Frame(fen, bg='cyan')
bottom=Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="RDV have changed",
    font='Arial 18 bold', fg='navy', bg='cyan')
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
    highlightbackground='light sky blue', command=saveData)
buttonSave.pack(side='left', padx=10, pady=10)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='white', bg='navy', activebackground='dark turquoise',
    highlightbackground='light sky blue', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    importationFile('./patient_agenda/events16/doc_events/fix_agenda/modifrdv.txt')
except FileNotFoundError as mod_file:
    print("+ No modifrdv.txt file has been found !", mod_file)
    msgBox2()

fen.mainloop()
