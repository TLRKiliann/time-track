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
fen.title("Care and monitoring")
fen.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(fen, bg='cyan')
bottom = Frame(fen, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(fen, text="Care and monitoring : ",
    font='Times 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

labelallergy=Label(fen, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='cyan')
labelallergy.pack(padx=5, pady=5)

# To read name in Entry widget
with open('./newpatient/entryfile21.txt', 'r') as filename:
    line1=filename.readline()

text_name=StringVar()
text_name.set(line1)
Entryname=Entry(fen, textvariable=text_name)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

# To read allergy in Entry widget
with open('./allergy/allergyfile21.txt', 'r') as allerfile:
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

textBox=Text(fen, height=15, width=60, font=18, relief=SUNKEN)
textBox.pack(padx=30, pady=30)

buttonClose=Button(fen, text="Quit", fg='white', width=10, bd=3,
    bg='navy', activebackground='dark turquoise', activeforeground='navy', 
    highlightbackground='grey17', command=quit)
buttonClose.pack(side='right', padx=10, pady=10)

try:
    importationFile('./14besoins/doc_suivi21/main_14b.txt',
        encodage="Utf-8")
except FileNotFoundError as filereach:
    print("File main_14b.txt not exist", filereach)

fen.mainloop()
