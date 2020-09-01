#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *


def importationFile(fichier, encodage="Utf-8"):
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

fen=Tk()
fen.title("Diagnostics and ATCD")
fen.configure(background='#82193e')

# To place side by side labelo + entrylab
top = Frame(fen, bg='#82193e')
bottom = Frame(fen, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Diagnostics and ATCD for : ",
    font='Arial 18 bold', fg='cyan', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

with open('./newpatient/entryfile3.txt', 'r') as filename:
	line1=filename.readline()

entrytext=StringVar()
entrytext.set(line1)
entryName=Entry(fen, textvariable=entrytext)
entryName.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='#82193e')
labelallergy.pack(padx=5, pady=10)

with open('./allergy/allergyfile3.txt', 'r') as filename:
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

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", fg='white', width=10, bd=3,
    bg='navy', activebackground='dark turquoise', activeforeground='navy', 
    highlightbackground='grey17', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./diag/doc_diag3/diagrecap3.txt',
    encodage="Utf-8")

fen.mainloop()
