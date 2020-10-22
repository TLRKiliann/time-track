#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


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
        self.can.create_window((4, 4), window=self.frame, anchor=NW,
            tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class de la barre des menus
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='cyan', padx=0)
        But2=Button(self, text ="Close", fg='cyan', bg='RoyalBlue4', relief=GROOVE,
            activebackground='aquamarine', command=boss.quit).pack(side=LEFT, padx=3)

# Application principale
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title('ANGEL-VISION - Developed by ko@l@tr33 - 2020')
        mBar=MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=1)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can=Canvas(self, width=600, height=400, bg='RoyalBlue3')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
            tags="self.frame")
        # Insertion du texte
        self.can.create_text(300, 150, anchor=CENTER, text="Medical Visit",
            font=('Times New Roman', 28), fill='aquamarine')
        self.can.create_text(590, 375, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='white') 
        self.can.pack(side=LEFT, fill=BOTH, expand=1)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # Button to add
        self.x2, self.y2 = 200, 250
        self.b2=Button(self.can, width=10, font=16, bg='RoyalBlue2', fg='white',
            activebackground='aquamarine', bd=3, highlightbackground='cyan',
            text="Add", command=self.lienDirect)
        self.fb2=self.can.create_window(self.x2, self.y2, window=self.b2)
        # Button to read
        self.x3, self.y3 = 400, 250
        self.b3=Button(self.can, width=10, font=16, bg='RoyalBlue2', fg='white',
            activebackground='aquamarine', bd=3, highlightbackground='cyan',
            text="Read", command=self.lectureFic)
        self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)
        self.pack()

    # Method to reconfigure scrollbar everytime
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def lienDirect(self):
        """
        To verify and write in VM file
        """
        try:
            if os.path.getsize('./vmed/doc_vmed4/resultvmed4.txt'):
                print("+ File 'VMED' exist (add)!")
                subprocess.run('./vmed/doc_vmed4/vmed_write.py', check=True)
        except FileNotFoundError as outmsg:
            print("+ Sorry, file 'VMED' not exist !", outmsg)
            print("+ File VMED created !!!")
            with open('./vmed/doc_vmed4/resultvmed4.txt', 'w') as file:
                file.write("--- MEDICAL VISIT ---\n")
            self.confRec()

    def lectureFic(self):
        """
        To verify and read diag file
        """
        try:
            if os.path.getsize('./vmed/doc_vmed4/resultvmed4.txt'):
                print("+ File 'VMED' exist (read)!")
                subprocess.run('./vmed/doc_vmed4/vmed_read.py', check=True)
        except FileNotFoundError as outcom:
            print("+ Sorry, file 'VMED' not exist !", outcom)
            self.confRec()

    def confRec(self):
        self.MsgBox2msg = messagebox.showinfo("Warning", "File 'VMED' "
            "was created, but no Medical Visit has been checked !")
        subprocess.run('./vmed/doc_vmed4/vmed_write.py', check=True)

if __name__=='__main__':
    app = Application()
    app.mainloop()
