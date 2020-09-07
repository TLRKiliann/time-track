#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *


def importationFile(fichier, encodage="Utf-8"):
    with open(fichier, 'r', encoding=encodage) as filer:
        content = filer.readlines()
        for li in content:
            textBox.insert(END, li)

# To display name in Entry widget
with open('./newpatient/entryfile10.txt', 'r') as filename:
    line1=filename.readline()

# To display allergy in Entry widget
with open('./allergy/allergyfile10.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()
    lineA6=allerfile.readline()
    lineA7=allerfile.readline()

fen=Tk()
fen.title("Results of Medical Visit")
fen.configure(background='#82193e')

# To place side by side labelo + entrylab
top = Frame(fen, bg='#82193e')
bottom = Frame(fen, bg='#82193e')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Results of Medical Visit for : ",
    font='Arial 18 bold', fg='cyan', bg='#82193e')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

text_name=StringVar()
text_name.set(line1)
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='#82193e')
labelallergy.pack(padx=5, pady=5)

text_aller=StringVar()
text_aller.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
Entryall=Entry(fen, textvariable=text_aller, width=60)
Entryall.pack(padx=10, pady=5)

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", width=8, bd=3,
    fg='cyan', bg='navy', highlightbackground='grey17',
    activebackground='dark turquoise', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

importationFile('./vmed/doc_vmed10/resultvmed.txt',
    encodage="Utf-8")

fen.mainloop()
