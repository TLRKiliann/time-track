#!/usr/bin/python3
# -*- coding:utf-8 -*-


from tkinter import *
from tkinter import messagebox
import time


fen = Tk()
fen.title("14 needs")
fen.configure(bg='cyan')

def recordTofile():
    MsgBox = messagebox.askyesno('Record', 'Results will be saved into Care and Monitoring, ok ?')

    if MsgBox == 1:
        print("Ok data saved")
        recordOption()
        confRec()
        fen.destroy()
    else:
        messagebox.showinfo('Return', 'You will return back')

def recordOption():
    print("+ Date : " + time.strftime("%d/%m/%Y"))
    print("+ Nom du patient : ", entryName.get())
    with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
        file.write("\nDate : ")
        file.write(time.strftime("%d/%m/%Y") + '\n')
        file.write("Patient name : ")
        file.write(entryName.get())
    print(CheckVar1.get())
    if CheckVar1.get()==1:
        print("Surveillance respiratoire requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance respiratoire requise\n")
    else:
        print("Nothing to do")

    print(CheckVar2.get())
    if CheckVar2.get()==1:
        print("Surveillance de la température requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance de la température requise\n")
    else:
        print("Nothing to do")

    print(CheckVar3.get())
    if CheckVar3.get()==1:
        print("Surveillance alimentaire et/ou hydratation requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance alimentaire et/ou hydratation requise\n")
    else:
        print("Nothing to do")

    print(CheckVar4.get())
    if CheckVar4.get()==1:
        print("Surveillance urinaire et/ou fécale requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance urinaire et/ou fécale requise requise\n")
    else:
        print("Nothing to do")

    print(CheckVar5.get())
    if CheckVar5.get()==1:
        print("Surveillance du sommeil requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance du sommeil requise\n")
    else:
        print("Nothing to do")

    print(CheckVar6.get())
    if CheckVar6.get()==1:
        print("Surveillance posturale et/ou des déplacements requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance posturale et/ou des déplacements requise\n")
    else:
        print("Nothing to do")

    print(CheckVar7.get())
    if CheckVar7.get()==1:
        print("Surveillance pour éviter les dangers requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance pour éviter les dangers requise\n")
    else:
        print("Nothing to do")

    print(CheckVar8.get())
    if CheckVar8.get()==1:
        print("Surveillance propreté et/ou téguments requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance propreté et/ou téguments requise\n")
    else:
        print("Nothing to do")

    print(CheckVar9.get())
    if CheckVar9.get()==1:
        print("Surveillance ou aide pour l'habillage/déshabillage requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Surveillance ou aide pour l'habillage/déshabillage requise\n")
    else:
        print("Nothing to do")

    print(CheckVar10.get())
    if CheckVar10.get()==1:
        print("Stimulation ou aide pour la communication requise en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Stimulation ou aide pour la communication requise\n")
    else:
        print("Nothing to do")

    print(CheckVar11.get())
    if CheckVar11.get()==1:
        print("Agir pour aider la personne dans ses valeurs et croyances en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Agir pour aider la personne dans ses valeurs et croyances\n")
    else:
        print("Nothing to do")

    print(CheckVar12.get())
    if CheckVar12.get()==1:
        print("Accompagner ou aider la personne à se réaliser en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Accompagner ou aider la personne à se réaliser\n")
    else:
        print("Nothing to do")

    print(CheckVar13.get())
    if CheckVar13.get()==1:
        print("Accompagnement ou aide dans se recréer requis en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Accompagnement ou aide dans se recréer requis\n")
    else:
        print("Nothing to do")

    print(CheckVar14.get())
    if CheckVar14.get()==1:
        print("Accompagnement ou aide dans l'apprentissage requis en ajout")
        with open('./14besoins/doc_suivi23/patient23_14b.txt', 'a+') as file:
            file.write("+ Accompagnement ou aide dans l'apprentissage requis\n")
    else:
        print("Nothing to do")

def confRec():
    MsgBox2msg = messagebox.showinfo("Confirmation", "Record confirmed and finished !")

labeltite=Label(fen, text='14 NEEDS', 
    font="Times 16 bold", width=10,
    height=3, bg='cyan', fg='navy')
labeltite.grid(sticky='w', row=0, column=0, padx=20)

with open('./newpatient/entryfile23.txt', 'r') as filename:
    line1=filename.readline()

textname=StringVar()
entryName=Entry(fen, textvariable=textname)
textname.set(line1)
entryName.grid(sticky='e', row=0, column=0, padx=30, pady=20)

CheckVar1 = IntVar()
C1 = Checkbutton(fen, text="Respirer", fg='navy', 
    bg='cyan', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C1.grid(row=1, column=0)

CheckVar2 = IntVar()
C2 = Checkbutton(fen, text="Température", fg='navy', 
    bg='cyan', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C2.grid(row=2, column=0)

CheckVar3 = IntVar()
C3 = Checkbutton(fen, text="Boire et manger", fg='navy', 
    bg='cyan', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C3.grid(row=3, column=0)

CheckVar4 = IntVar()
C4 = Checkbutton(fen, text="Eliminer", fg='navy', 
    bg='cyan', variable=CheckVar4, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C4.grid(row=4, column=0)

CheckVar5 = IntVar()
C5 = Checkbutton(fen, text="Dormir, se reposer", fg='navy', 
    bg='cyan', variable=CheckVar5, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C5.grid(row=5, column=0)

CheckVar6 = IntVar()
C6 = Checkbutton(fen, text="Se mouvoir, maintenir une bonne posture", 
    fg='navy', bg='cyan', variable=CheckVar6, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C6.grid(row=6, column=0)

CheckVar7 = IntVar()
C7 = Checkbutton(fen, text="Eviter les dangers", fg='navy', 
    bg='cyan', variable=CheckVar7, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C7.grid(row=7, column=0)

CheckVar8 = IntVar()
C8 = Checkbutton(fen, text="Etre propre, protéger ses téguments", 
    fg='navy', bg='cyan', variable=CheckVar8, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C8.grid(row=8, column=0)

CheckVar9 = IntVar()
C9 = Checkbutton(fen, text="Se vêtir et se dévêtir", 
    fg='navy', bg='cyan', variable=CheckVar9, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C9.grid(row=9, column=0)

CheckVar10 = IntVar()
C10 = Checkbutton(fen, text="Communiquer avec ses semblables", 
    fg='navy', bg='cyan', variable=CheckVar10, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C10.grid(row=10, column=0)

CheckVar11 = IntVar()
C11 = Checkbutton(fen, text="Agir selon ses valeurs et croyances", 
    fg='navy', bg='cyan', variable=CheckVar11, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C11.grid(row=11, column=0)

CheckVar12 = IntVar()
C12 = Checkbutton(fen, text="S'occuper en vue de se réaliser", 
    fg='navy', bg='cyan', variable=CheckVar12, 
    onvalue=1, offvalue=0, 
    height=1, width=40, anchor="w")
C12.grid(row=12, column=0)

CheckVar13 = IntVar()
C13 = Checkbutton(fen, text="Se recréer", 
    fg='navy', bg='cyan', variable=CheckVar13, 
    onvalue=1, offvalue=0, height=1, width=40,
    anchor="w")
C13.grid(row=13, column=0)

CheckVar14 = IntVar()
C14 = Checkbutton(fen, text="Apprendre", fg='navy', 
    bg='cyan', variable=CheckVar14, 
    onvalue=1, offvalue=0, height=1,
    width=40, anchor="w")
C14.grid(row=14, column=0)

buttonTocheck=Button(fen, text="Save", width=10, fg='yellow',
    bg='blue', bd=3, highlightbackground='cyan',
    activebackground='dark turquoise', command=recordTofile)
buttonTocheck.grid(sticky='w', row=15, column=0, padx=20, pady=10)

buttonQuit=Button(fen, text='Quit', width=10, fg='white',
    bg='blue', bd=3, highlightbackground='cyan',
    activebackground='dark turquoise', command=quit)
buttonQuit.grid(sticky='e',row=15, column=0, padx=20, pady=10)

fen.mainloop()
