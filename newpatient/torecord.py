#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='#82193e')
#gui.geometry('300x200')

def get(Nompatient, entree, Birthvalue, Birthentree):
    """
    Test at first time and
    after when file was earased
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        mot = "-"
        mot2 = "--"
        mot3 = "---"
        mot4 = "----"
        mot5 = "-----"
        mot6 = "------"
        mot7 = "-------"
        mot8 = "--------"
        mot9 = "---------"
        mot10 = "---------"
        mot11 = "----------"
        mot12 = "-----------"
        mot13 = "------------"
        mot14 = "-------------"
        mot15 = "--------------"
        mot16 = "---------------"
        mot17 = "----------------"
        mot18 = "-----------------"
        mot19 = "------------------"
        mot20 = "-------------------"
        Nompatient = entree.get()
        Birthvalue = Birthentree.get()
        print(Nompatient)
        print(Birthvalue)

        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot in line:
                        searchLine1(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot2 in line:
                        searchLine2(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot3 in line:
                        searchLine3(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot4 in line:
                        searchLine4(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile5.txt'):
            with open('./newpatient/entryfile5.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        searchLine5(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile6.txt'):
            with open('./newpatient/entryfile6.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile7.txt'):
            with open('./newpatient/entryfile7.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile8.txt'):
            with open('./newpatient/entryfile8.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot4 in line:
                        searchLine4(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile9.txt'):
            with open('./newpatient/entryfile9.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        searchLine5(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile10.txt'):
            with open('./newpatient/entryfile10.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile11.txt'):
            with open('./newpatient/entryfile11.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile12.txt'):
            with open('./newpatient/entryfile12.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        searchLine5(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile13.txt'):
            with open('./newpatient/entryfile13.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile14.txt'):
            with open('./newpatient/entryfile14.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile15.txt'):
            with open('./newpatient/entryfile15.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile16.txt'):
            with open('./newpatient/entryfile16.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot5 in line:
                        searchLine5(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile17.txt'):
            with open('./newpatient/entryfile17.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile18.txt'):
            with open('./newpatient/entryfile18.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile19.txt'):
            with open('./newpatient/entryfile19.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot6 in line:
                        searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if mot7 in line:
                        searchLine7(Nompatient, Birthvalue)
        gui.destroy()

def searchLine1(Nompatient, Birthvalue):
    with open('./newpatient/entryfile.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine2(Nompatient, Birthvalue):
    with open('./newpatient/entryfile2.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine3(Nompatient, Birthvalue):
    with open('./newpatient/entryfile3.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine4(Nompatient, Birthvalue):
    with open('./newpatient/entryfile4.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine5(Nompatient, Birthvalue):
    with open('./newpatient/entryfile5.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine6(Nompatient, Birthvalue):
    with open('./newpatient/entryfile6.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine7(Nompatient, Birthvalue):
    with open('./newpatient/entryfile7.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine8(Nompatient, Birthvalue):
    with open('./newpatient/entryfile8.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine9(Nompatient, Birthvalue):
    with open('./newpatient/entryfile9.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

def searchLine10(Nompatient, Birthvalue):
    with open('./newpatient/entryfile10.txt', 'w') as file:
        file.write(Nompatient + '\n')
        file.write(Birthvalue + '\n')

labelName = Label(gui)
labelName = Label(text='Enter Name and Surname : ', font="Times 14 bold", 
    fg='cyan', bg='#82193e')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient, highlightbackground='gray', bd=4)
entree.pack()

labelBirth = Label(gui)
labelBirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='cyan', bg='#82193e')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birthvalue.set('Format: 00/00/0000')
Birthentree = Entry(gui, textvariable=Birthvalue, highlightbackground='gray', bd=4)
Birthentree.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='#82193e',
    activebackground='dark turquoise',
    command = lambda: get(Nompatient, entree, Birthvalue, Birthentree))
bouton1.pack(side=LEFT, padx=30, pady=10)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='#82193e',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=15, pady=10)

gui.mainloop()
