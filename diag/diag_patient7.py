#!/usr/bin/python3
#!-*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import subprocess
import os


# La ScrollBar en class! Préparation pour l'application.
class ScrollCanvas(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can=Canvas(self, width=width, height=height, bd=bd, bg=bg,
            relief=relief)
        self.frame = Frame(self.can)

        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, 
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='RoyalBlue3', padx=0)
        # Menu fichier
        But=Button(self, text ="Close", fg='white', bg='blue',
            activebackground='cyan', command=boss.quit).pack(side=LEFT,
            padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('TIME-TRACK - Developed by ko@l@tr33 - 2020')
        mBar=MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can=Canvas(self, width=600, height=400, bg='cyan')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, 
                                  tags="self.frame")
        # Insertion du texte
        self.can.create_text(300, 140, anchor=CENTER, text="Diagnostics and ATCD",
                    font=('Times New Roman', 28), fill='cyan')
        self.can.create_text(590, 380, anchor=NE, text="TIME-TRACK",
                    font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Création des boutons
        self.x2, self.y2 = 200, 250
        self.b2=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='gold',
            activebackground='dark turquoise', bd=3, 
            highlightbackground='light sky blue', 
            text="Add", command=self.Frame_Ap1)
        self.fb2=self.can.create_window(self.x2, self.y2, window=self.b2)

        self.x3, self.y3 = 400, 250
        self.b3=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='gold',
            activebackground='dark turquoise', bd=3, 
            highlightbackground='light sky blue', 
            text="Read", command=self.Frame_Ap2)
        self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)
        self.pack()

    # Méthode pour reconfigurer la scrollbar à chaque fois
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def Frame_Ap1(self):
        """
        To verify and write in diag file
        """
        try:
            if os.path.getsize('./diag/doc_diag7/diagrecap7.txt'):
                print("+ File 'Diag' exist (add)!")
                subprocess.call('./diag/doc_diag7/diag_write.py')
        except FileNotFoundError as outmsg:
            print("+ Sorry, file 'Diag' not exist !", outmsg)
            print("+ File diag.txt created !")
            with open('./diag/doc_diag7/diagrecap7.txt', 'w') as file:
                file.write(".")
            self.confRec()
            subprocess.call('./diag/doc_diag7/diag_write.py')

    def Frame_Ap2(self):
        """
        To verify and read diag file
        """
        try:
            if os.path.getsize('./diag/doc_diag7/diagrecap7.txt'):
                print("+ File 'Diag' exist (read)!")
                subprocess.call('./diag/doc_diag7/diag_read.py')
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'Diag' not exist !", outcom)
            self.confRec()

    def confRec(self):
        self.MsgBox2msg = messagebox.showinfo("Warning", "File 'Diag'"
            "was created, but no Diagnosis has been checked !")

if __name__=='__main__':
    app = Application()
    app.mainloop()
    