#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import subprocess
import time
from tkinter import messagebox


def saveData():
    """
    No need to test if file
    exist or not. Already test
    it before.
    """
    with open('./vmed/doc_vmed24/resultvmed.txt', 'a+') as filerecord:
        filerecord.write(textBox.get("1.0", "end-1c"))
        filerecord.write(str('\n\n'))

def messFromSafeButt():
    """
    Message of confirmation
    with messagebox.
    """
    MsgBox = messagebox.askquestion("Confirm","Are you sure ?\n"
        "It will save all data !")
    if MsgBox == 'yes':
        saveData()
        textBox.insert(INSERT, "\n---Data saved !---")
        print("+ Data saved !")
    else:
        textBox.insert(INSERT, "Nothing has been saved !")
        print("+ Nothing has been saved !")

def readerFile():
    """
    To read into the txt file.
    """
    with open('./vmed/doc_vmed24/resultvmed.txt', 'r') as filereader:
        print(filereader.read())
    subprocess.call('./vmed/doc_vmed24/vmed_read.py')

def addText():
    """
    Display text into widget Text
    before to add comment.
    """
    textBox.delete('1.0', END)
    textBox.insert(INSERT, "En date du : ")
    textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :") + '\n')
    textBox.update()

def importationFile(fichier, encodage="Utf-8"):
    """
    First display of txt file
    when the user start app.
    """
    file = open(fichier, 'r', encoding=encodage)
    content=file.readlines()
    file.close()
    for li in content:
        textBox.insert(END, li)

# To read name in Entry widget
with open('./newpatient/entryfile24.txt', 'r') as filename:
    line1=filename.readline()

# To read allergy in Entry widget
with open('./allergy/allergyfile24.txt', 'r') as allerfile:
    lineA1=allerfile.readline()
    lineA2=allerfile.readline()
    lineA3=allerfile.readline()
    lineA4=allerfile.readline()
    lineA5=allerfile.readline()
    lineA6=allerfile.readline()
    lineA7=allerfile.readline()

root=Tk()
root.title("Results of Medical Visit")
root.configure(background='cyan')

# To place side by side labelo + entrylab
top = Frame(root, bg='cyan')
bottom = Frame(root, bg='cyan')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

labelo=Label(root, text="Results of Medical Visit for : ",
    font='Arial 18 bold', fg='navy', bg='cyan')
labelo.pack(in_=top, side=LEFT, padx=5, pady=20)

text_name=StringVar()
Entryname=Entry(root, textvariable=text_name)
text_name.set(line1)
Entryname.pack(in_=top, side=LEFT, padx=10, pady=20)

labelallergy=Label(root, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='cyan')
labelallergy.pack(padx=5, pady=5)

text_all=StringVar()
text_all.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
Entryaller=Entry(root, textvariable=text_all, width=60)
Entryaller.pack(padx=10, pady=5)

textBox=Text(root, height=15, width=60, font=18, relief=SUNKEN)
textBox.insert(INSERT, "\nEn date du : ")
textBox.insert(END, time.strftime("%d/%m/%Y à %H:%M:%S :\n"))
textBox.pack(padx=30, pady=30)

buttonLire=Button(root, text="Read", width=8, bd=3,
    fg='cyan', bg='navy', highlightbackground='grey17',
    activebackground='dark turquoise', command=readerFile)
buttonLire.pack(side='left', padx=10, pady=10)

buttonEffacer=Button(root, text="1-Add", width=8, bd=3,
    fg='yellow', bg='navy', highlightbackground='grey17',
    activebackground='dark turquoise', command=addText)
buttonEffacer.pack(side='left', padx=10, pady=10)

buttonEnter=Button(root, text="2-Save", width=8, bd=3,
    fg='yellow', bg='navy', highlightbackground='grey17',
    activebackground='dark turquoise',
    command=messFromSafeButt)
buttonEnter.pack(side='left', padx=10, pady=10)

buttonQuitter=Button(root, text="Quit", width=8, bd=3,
    fg='white', bg='navy', highlightbackground='grey17',
    activebackground='red', command=quit)
buttonQuitter.pack(side='right', padx=10, pady=10)

importationFile('./vmed/doc_vmed24/resultvmed.txt',
    encodage="Utf-8")

mainloop()
