#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


gui=Tk()
gui.title("Enter Allergy")
gui.configure(bg='#82193e')
#gui.geometry('250x200')

def get(Allpatient, entryall):
    MsgBox = messagebox.askyesno('Save data', 'Data saved !')
    if MsgBox == 1:
        Allpatient = entryall.get()
        print(Allpatient)
        print(entryall.get())
        try:
            if os.path.getsize('./allergy/allergyfile6.txt'):
                print("+ File 'allergyfile6.txt' exist !")
                with open('./allergy/allergyfile6.txt', 'a+') as namefile:
                    namefile.write(entryall.get() + '\n')
                    namefile.write(str('----------------\n'))
                    gui.destroy()
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'allergyfile6.txt' not exist !")
            print(str(outcom))
            print("+ File 'allergyfile6.txt' created !")
            with open('./allergy/allergyfile6.txt', 'a+') as namefile:
                namefile.write(entryall.get() + '\n')
                namefile.write(str('----------------\n'))
                gui.destroy()
    else:           
        NoforQ = messagebox.showinfo('Return', 'Data not saved')

labelName = Label(gui)
labelName = Label(text='Enter Allergy', font="Times 16 bold", 
    fg='cyan', bg='#82193e')
labelName.pack(pady=10)

Allpatient=StringVar()
Allpatient.set('Allergy no-food')
entryall = Entry(gui, textvariable=Allpatient, highlightbackground='gray', bd=4)
entryall.pack(pady=10)

bouton1 = Button(gui, text="Save", width=8, bd=3, fg='yellow', bg='RoyalBlue3',
    highlightbackground='#82193e', activebackground='dark turquoise',
    command = lambda: get(Allpatient, entryall))
bouton1.pack(side=LEFT, padx=10, pady=10)

buttQuit=Button(gui, text="Quit", width=8, bd=3, fg='white', bg='RoyalBlue3', 
    highlightbackground='#82193e', activebackground='dark turquoise',
    command=quit)
buttQuit.pack(padx=10, pady=10)

gui.mainloop()
