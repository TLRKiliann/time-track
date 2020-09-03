#!/usr/bin/python3
# -*-encoding:Utf-8-*-


import tkinter
from tkinter import *
import subprocess
import os
import time
from tkinter import messagebox


def saveData():
    """
    To record data from result18.txt
    and from patient18_14b.txt into 
    txt main file
    """
    try:        
        if os.path.getsize('./14besoins/doc_suivi18/main_14b.txt'):
            print("+ File 'main_14b.txt' exist !")
            with open('./14besoins/doc_suivi18/main_14b.txt', 'a+') as namefile:
                namefile.write(textBox.get("1.0", "end-1c" + '\n\n'))
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'main_14b.txt' not exist !")
        print(str(outcom))
        print("+ File 'main_14b.txt' created !")
        with open('./14besoins/doc_suivi18/main_14b.txt', 'a+') as namefile:
            namefile.write(textBox.get("1.0", "end-1c" + '\n\n'))

def messFromSafeButt():
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "\n---Nothing has been saved !---")
        print("+ Nothing has been saved !")

def lectureFic():
    with open('./14besoins/doc_suivi18/patient18_14b.txt', 'r') as f1read:
        with open('./labo/doc_labo/result18.txt', 'r') as f2read:
            print(f1read.read())
            print(f2read.read())
    subprocess.call('./14besoins/doc_suivi18/patient18_read.py')

def ajouterText():
    """
    To retrieve data 
    from initial textBox() 
    """
    textBox.delete('1.0', END)
    textBox.insert(INSERT, "En date du : ")
    textBox.insert(END, time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
    textBox.update()

def importationFile(fichier, encodage="Utf-8"):
    """
    To test if txt
    patient exist
    """
    try:        
        if os.path.getsize(fichier):
            print("+ File 'patient18_14b.txt' exist !")
            with open(fichier, 'r', encoding=encodage) as fileneeds:
                content=fileneeds.readlines()
                for li in content:
                    textBox.insert(END, li)
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'patient18_14b.txt' not exist !", outcom)

def importationLabo(fichier2, encodage="Utf-8"):
    """
    To test if txt
    patient exist
    """
    try:        
        if os.path.getsize(fichier2):
            print("+ File 'result18.txt' exist !")
            with open(fichier2, 'r', encoding=encodage) as filelab:
                content2=filelab.readlines()
                for li in content2:
                    textBox.insert(END, li)
    except FileNotFoundError as outcom:
        print("+ Sorry, file 'result18.txt' not exist !")
        print(str(outcom))

root=Tk()
root.title("Care and monitoring")
root.configure(background='#82193e')

# To place side by side labelo + entrylab
top = Frame(root, bg='#82193e')
bottom = Frame(root, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Care and monitoring : ",
    font='Times 18 bold', fg='cyan', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='#82193e')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile18.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
Entryname=Entry(root, textvariable=text_name)
text_name.set(line1)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

# To read allergy in Entry widget
with open('./allergy/allergyfile18.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()
    lineA6=allerfile.readline()
    lineA7=allerfile.readline()

text_aller=StringVar()
text_aller.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
Entryaller=Entry(root, textvariable=text_aller, width=60)
Entryaller.pack(padx=10, pady=5)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.insert(INSERT, "En date du : ")
textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
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

importationFile('./14besoins/doc_suivi18/patient18_14b.txt', encodage='Utf-8')

importationLabo('./labo/doc_labo/result18.txt', encodage='Utf-8')

mainloop()
