#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import subprocess
import time
from tkinter import messagebox


def retrieve_input():
    file = open('./diag/doc_diag6/diagrecap6.txt', 'a+')
    file.write(textBox.get("1.0", "end-1c"))
    file.write(str('\n\n'))
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
    file = open('./diag/doc_diag6/diagrecap6.txt', 'r')
    print(file.read())
    file.close()
    subprocess.call('./diag/doc_diag6/diag_read.py')

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

root=Tk()
root.title("Diagnostics and ATCD")
root.configure(background='#82193e')

# To place side by side labelo + entrylab
top = Frame(root, bg='#82193e')
bottom = Frame(root, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='cyan', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile6.txt', 'r') as filename:
    line1=filename.readline()

textname=StringVar()
entryName=Entry(root, textvariable=textname)
textname.set(line1)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='#82193e')
labelallergy.pack(padx=5, pady=10)

with open('./allergy/allergyfile6.txt', 'r') as filename:
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

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.insert(INSERT, "\nEn date du : ")
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

importationFile('./diag/doc_diag6/diagrecap6.txt',
    encodage="Utf-8")

mainloop()
