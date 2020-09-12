#!/usr/bin/python3
# -*- coding:utf-8 -*-


from tkinter import *
from tkinter import messagebox


gui = Tk()
gui.title("Intolerances")
gui.configure(bg='RoyalBlue4')

def saveCheck():
    MSB = messagebox.askyesno('Save Data', 'Data saved !')
    if MSB == 1:
        print("Ok, data")
        recordOption()
        confRec()
        gui.destroy()
    else:
        NoforQ = messagebox.showinfo('Return', 'Data not saved')

def recordOption():
    """
    To save checkbox option
    """
    print(CheckVar1.get())
    if CheckVar1.get()==1:
        print("Gluten intolerance")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Gluten intolerance\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar2.get())
    if CheckVar2.get()==1:
        print("Lactose intolerance")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Lactose intolerance\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar3.get())
    if CheckVar3.get()==1:
        print("Saccharose intolerance")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Saccharose intolerance\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar4.get())
    if CheckVar4.get()==1:
        print("Fructose intolerance")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Fructose intolerance\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar5.get())
    if CheckVar5.get()==1:
        print("Eggs")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Eggs\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar6.get())
    if CheckVar6.get()==1:
        print("Fish")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Fish\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")


    print(CheckVar7.get())
    if CheckVar7.get()==1:
        print("Shellfish")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Shellfish\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar8.get())
    if CheckVar8.get()==1:
        print("Molluscs")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Molluscs\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar9.get())
    if CheckVar9.get()==1:
        print("Groundnut")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Groundnut\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar10.get())
    if CheckVar10.get()==1:
        print("Oleaginous")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Oleaginous\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar11.get())
    if CheckVar11.get()==1:
        print("Sesame")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Sesame\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar12.get())
    if CheckVar12.get()==1:
        print("Soya")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Soya\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar13.get())
    if CheckVar13.get()==1:
        print("Cereals")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Cereals\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar14.get())
    if CheckVar14.get()==1:
        print("Latex")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Latex\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar15.get())
    if CheckVar15.get()==1:
        print("Rosacea")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Rosacea\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

    print(CheckVar16.get())
    if CheckVar16.get()==1:
        print("Umbellifers")
        with open('./allergy/allergyfile19.txt', 'a+') as file:
            file.write("Umbellifers\n")
            file.write(str('----------------\n'))
    else:
        print("Nothing to do")

def confRec():
    MsgBox2 = messagebox.showinfo("Confirmation", "Record confirmed and finished !")

Intolabel = Label(gui, text="Intolerances : ", font="Times 18 bold",
    width=14, fg='aquamarine', bg='RoyalBlue4')
Intolabel.grid(sticky='w', row=0, column=0, pady=10)

# To read name in Entry widget
with open('./newpatient/entryfile19.txt', 'r') as filename:
    line1=filename.readline()

text_entry = StringVar()
text_entry.set(line1)
entryName = Entry(gui, textvariable=text_entry)
entryName.grid(sticky='e', row=0, column=0, padx=10, pady=10)

CheckVar1 = IntVar()
C1 = Checkbutton(gui, text="Gluten", fg='navy', 
    bg='dark turquoise', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C1.grid(row=2, column=0)

CheckVar2 = IntVar()
C2 = Checkbutton(gui, text="Lactose", fg='navy', 
    bg='dark turquoise', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C2.grid(row=3, column=0)

CheckVar3 = IntVar()
C3 = Checkbutton(gui, text="Saccharose", fg='navy', 
    bg='dark turquoise', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C3.grid(row=4, column=0)

CheckVar4 = IntVar()
C4 = Checkbutton(gui, text="Fructose", fg='navy', 
    bg='dark turquoise', variable=CheckVar4, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C4.grid(row=5, column=0)

#Les allergies d’origine animale : 
animallabel = Label(gui, text="Animal allergy", font="Times 18 bold",
    fg='aquamarine', bg='RoyalBlue4')
animallabel.grid(row=6, column=0, pady=10)  

CheckVar5 = IntVar()
C5 = Checkbutton(gui, text="Eggs", fg='navy', 
    bg='dark turquoise', variable=CheckVar5, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C5.grid(row=7, column=0)

CheckVar6 = IntVar()
C6 = Checkbutton(gui, text="Fish", fg='navy', 
    bg='dark turquoise', variable=CheckVar6, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C6.grid(row=8, column=0)


CheckVar7 = IntVar()
C7 = Checkbutton(gui, text="Shellfish", fg='navy', 
    bg='dark turquoise', variable=CheckVar7, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C7.grid(row=9, column=0)

CheckVar8 = IntVar()
C8 = Checkbutton(gui, text="Molluscs", fg='navy', 
    bg='dark turquoise', variable=CheckVar8, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C8.grid(row=10, column=0)

#Les allergies d’origine végétale : 
vegetallabel = Label(gui, text="Vegetable allergy",
    font="Times 18 bold", fg='aquamarine', bg='RoyalBlue4')
vegetallabel.grid(row=11, column=0, pady=10)  

CheckVar9 = IntVar()
C9 = Checkbutton(gui, text="Groundnut", fg='navy', 
    bg='dark turquoise', variable=CheckVar9, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C9.grid(row=12, column=0)

CheckVar10 = IntVar()
C10 = Checkbutton(gui, text="Oleaginous fruits", fg='navy', 
    bg='dark turquoise', variable=CheckVar10, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C10.grid(row=13, column=0)

CheckVar11 = IntVar()
C11 = Checkbutton(gui, text="Sesame", fg='navy', 
    bg='dark turquoise', variable=CheckVar11, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C11.grid(row=14, column=0)

CheckVar12 = IntVar()
C12 = Checkbutton(gui, text="Soya", fg='navy', 
    bg='dark turquoise', variable=CheckVar12, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C12.grid(row=15, column=0)

CheckVar13 = IntVar()
C13 = Checkbutton(gui, text="Cereals (wheat, rye)", fg='navy', 
    bg='dark turquoise', variable=CheckVar13, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C13.grid(row=16, column=0)

CheckVar14 = IntVar()
C14 = Checkbutton(gui, text="Latex fruits", fg='navy', 
    bg='dark turquoise', variable=CheckVar14, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C14.grid(row=17, column=0)

latexlabel = Label(gui, text="Latex fruits = avocado, banana, kiwi,"
    " fig, chestnut...", font="Times 12", fg='aquamarine',
    bg='RoyalBlue4')
latexlabel.grid(row=18, column=0, pady=10)  

CheckVar15 = IntVar()
C15 = Checkbutton(gui, text="Rosacea",
    fg='navy', bg='dark turquoise', variable=CheckVar15, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C15.grid(row=19, column=0)

rosaclabel = Label(gui, text="Rosacea = apricot, cherry, strawberry...",
    font="Times 12", fg='aquamarine', bg='RoyalBlue4')
rosaclabel.grid(row=20, column=0, pady=10)  

CheckVar16 = IntVar()
C16 = Checkbutton(gui, text="Umbellifers", fg='navy', 
    bg='dark turquoise', variable=CheckVar16, 
    onvalue=1, offvalue=0, height=1, 
    width=40, anchor="w")
C16.grid(row=21, column=0)

ombellabel = Label(gui, text="Umbellifers = dill, carrot, celery,"
    " fennel, parsley...",
    font="Times 12", fg='aquamarine', bg='RoyalBlue4')
ombellabel.grid(row=22, column=0, pady=10)  

buttSave = Button(gui, text="Save", width=10, fg='yellow',
    bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4',
    activebackground='dark turquoise', command=saveCheck)
buttSave.grid(sticky='w', row=23, column=0, padx=20, pady=10)

buttQuit = Button(gui, text='Quit', width=10, fg='white',
    bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4',
    activebackground='dark turquoise', command=quit)
buttQuit.grid(sticky='e', row=23, column=0, padx=20, pady=10)

gui.mainloop()
