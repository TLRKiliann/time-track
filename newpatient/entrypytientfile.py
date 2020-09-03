#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='#82193e')
#gui.geometry('300x200')

def get(Nompatient, entree, Birthvalue, Birth_entree):
    """
    Test at first time and
    after when file was earased
    """
    MsgBox = messagebox.askyesno('Save data', 'Do you want to save ?')
    if MsgBox == 1:
        Nompatient = entree.get()
        Birthvalue = Birth_entree.get()
        print(Nompatient)
        print(Birthvalue)

        if os.path.getsize('./newpatient/entryfile.txt'):
            print("+ File 'entryfile.txt' exist !")
            #searchLine1(Nompatient, Birthvalue) 

        if os.path.getsize('./newpatient/entryfile2.txt'):
            print("+ File 'entryfile2.txt' exist !")
            #searchLine2(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile3.txt'):
            print("+ File 'entryfile3.txt' exist !")
            #searchLine3(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile4.txt'):
            print("+ File 'entryfile4.txt' exist !")
            #searchLine4(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile5.txt'):
            print("+ File 'entryfile5.txt' exist !")
            #searchLine5(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile6.txt'):
            print("+ File 'entryfile6.txt' exist !")
            #searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile7.txt'):
            print("+ File 'entryfile7.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile8.txt'):
            print("+ File 'entryfile8.txt' exist !")
            #searchLine1(Nompatient, Birthvalue) 

        if os.path.getsize('./newpatient/entryfile9.txt'):
            print("+ File 'entryfile9.txt' exist !")
            #searchLine2(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile10.txt'):
            print("+ File 'entryfile10.txt' exist !")
            #searchLine3(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile11.txt'):
            print("+ File 'entryfile11.txt' exist !")
            #searchLine4(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile12.txt'):
            print("+ File 'entryfile12.txt' exist !")
            #searchLine5(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile13.txt'):
            print("+ File 'entryfile13.txt' exist !")
            #searchLine6(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile14.txt'):
            print("+ File 'entryfile14.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile15.txt'):
            print("+ File 'entryfile15.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile16.txt'):
            print("+ File 'entryfile16.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile17.txt'):
            print("+ File 'entryfile17.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile18.txt'):
            print("+ File 'entryfile18.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)
            
        if os.path.getsize('./newpatient/entryfile19.txt'):
            print("+ File 'entryfile19.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)

        if os.path.getsize('./newpatient/entryfile20.txt'):
            print("+ File 'entryfile20.txt' exist !")
            #searchLine7(Nompatient, Birthvalue)

    gui.destroy()

labelName = Label(gui)
labelName = Label(text='Enter Name and Surname : ', font="Times 14 bold", 
    fg='cyan', bg='#82193e')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient, highlightbackground='#82193e', bd=4)
entree.pack()

labelBirth = Label(gui)
labelBirth = Label(text='Birth Date : ', font="Times 14 bold",
    fg='cyan', bg='#82193e')
labelBirth.pack(pady=10)

Birthvalue=StringVar()
Birthvalue.set('Format: 00/00/0000')
Birth_entree = Entry(gui, textvariable=Birthvalue, highlightbackground='#82193e', bd=4)
Birth_entree.pack()

bouton1 = Button(gui, text="Enter", width=8, bd=3,
    fg='yellow', bg='RoyalBlue3', highlightbackground='#82193e',
    activebackground='dark turquoise',
    command = lambda: get(Nompatient, entree, Birthvalue, Birth_entree))
bouton1.pack(side=LEFT, padx=30, pady=10)

buttQuit=Button(gui, text="Quit", width=8, bd=3,
    fg='white', bg='RoyalBlue3', highlightbackground='#82193e',
    activebackground='dark turquoise', command=quit)
buttQuit.pack(side=LEFT, padx=15, pady=10)

gui.mainloop()
