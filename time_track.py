#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import time
import datetime
import os
import itertools
import subprocess
from boxapp import callBox
from agendapp import displayDates


# ScrollBar in class and preparing for main application !
class ScrollCanvas(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=borderwidth, relief=relief)
        self.can = Canvas(self, width=width, height=height, bd=bd,
            bg=bg, relief=relief)
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW,
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

# Class to menubar
class MenuBar(Frame):
    """Barre menu déroulant"""
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='dim grey', padx=0)
        # 1st menu
        fileMenu = Menubutton(self, text='Menu', fg='white',
            font=("Times 14"), bg='grey30', relief=GROOVE)
        new_text=StringVar()
        new_text2=StringVar()
        new_text3=StringVar()
        new_text4=StringVar()
        new_text5=StringVar()
        new_text6=StringVar()
        new_text7=StringVar()

        fileMenu.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 1st
        me1 = Menu(fileMenu, tearoff=0)
        me1.add_command(label='Accueil', underline=0, font=("Times 14 bold"),
            background='black',activebackground='aquamarine',
            foreground='aquamarine', activeforeground='black',
            command=boss.secondPage)
        me1.add_command(label="Synopsis", underline=0, font=("Times 14 bold"),
            background='black', activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.showsynopsis)
        me1.add_command(label="Psychotabs", underline=0, font=("Times 14 bold"),
            background='black',  activebackground='cyan',
            foreground='aquamarine', activeforeground='black',
            command=boss.launchPsycho)
        me1.add_command(label='MapApp', font=("Times 14 bold"),
            background='black', activebackground='aquamarine',
            foreground='yellow', activeforeground='black',
            command=boss.instalpy)
        me1.add_command(label='Quit', font=("Times 14 bold"),
            background='black', activebackground='red',
            foreground='red', activeforeground='white',
            command=boss.msgExit)
        # Integration of 1st menu
        fileMenu.configure(activeforeground='black', activebackground='cyan',
            menu=me1)
        
        # For label below (in me2.add_command)
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1=namefile.readline()
                new_text=line1
        except FileNotFoundError as fileout:
            print("No file entryfile.txt exist", fileout)

        try:
            with open('./newpatient/entryfile2.txt', 'r') as namefile:
                line2=namefile.readline()
                new_text2=line2
        except FileNotFoundError as fileout2:
            print("No file entryfile2.txt exist", fileout2)

        try:
            with open('./newpatient/entryfile3.txt', 'r') as namefile:
                line3=namefile.readline()
                new_text3=line3
        except FileNotFoundError as fileout3:
            print("No file entryfile3.txt exist", fileout3)

        try:
            with open('./newpatient/entryfile4.txt', 'r') as namefile:
                line4=namefile.readline()
                new_text4=line4
        except FileNotFoundError as fileout4:
            print("No file entryfile4.txt exist", fileout4)

        try:
            with open('./newpatient/entryfile5.txt', 'r') as namefile:
                line5=namefile.readline()
                new_text5=line5
        except FileNotFoundError as fileout5:
            print("No file entryfile5.txt exist", fileout5)

        try:
            with open('./newpatient/entryfile6.txt', 'r') as namefile:
                line6=namefile.readline()
                new_text6=line6
        except FileNotFoundError as fileout6:
            print("No file entryfile6.txt exist", fileout6)

        try:
            with open('./newpatient/entryfile7.txt', 'r') as namefile:
                line7=namefile.readline()
                new_text7=line7
        except FileNotFoundError as fileout7:
            print("No file entryfile7.txt exist", fileout7)

        # Agenda menu
        self.cmd_agenda=Menubutton(self, text='Agenda', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_agenda.pack(side=LEFT, padx=3)
        me3 = Menu(self.cmd_agenda)
        # Partie déroulante du menu agenda
        me3.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda)
        me3.add_separator()
        me3.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda2)
        me3.add_separator()
        me3.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda3)
        me3.add_separator()
        me3.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda4)
        me3.add_separator()
        me3.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda5)
        me3.add_separator()
        me3.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda6)
        me3.add_separator()
        me3.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda7)
        # Integration of agenda menu
        self.cmd_agenda.configure(activeforeground='black', activebackground='cyan', 
            menu=me3)

        # 14 besoins menu
        self.cmd_Besoins=Menubutton(self, text='14 Needs', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Besoins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 14b
        me4 = Menu(self.cmd_Besoins)
        me4.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoinsCoche)
        me4.add_separator()
        me4.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins2Coche)
        me4.add_separator()
        me4.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins3Coche)
        me4.add_separator()
        me4.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins4Coche)
        me4.add_separator()
        me4.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins5Coche)
        me4.add_separator()
        me4.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins6Coche)
        me4.add_separator()
        me4.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins7Coche)
        # Integration of 14b menu
        self.cmd_Besoins.configure(activeforeground='black', activebackground='cyan',
            menu=me4)

        # Helth and care menu
        self.cmd_Soins=Menubutton(self, text='Care and monitoring', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Soins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meSoins = Menu(self.cmd_Soins)
        meSoins.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins1)
        meSoins.add_separator()
        meSoins.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins2)
        meSoins.add_separator()
        meSoins.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins3)
        meSoins.add_separator()
        meSoins.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins4)
        meSoins.add_separator()
        meSoins.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins5)
        meSoins.add_separator()
        meSoins.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins6)
        meSoins.add_separator()
        meSoins.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins7)
        # Integration of health and care menu
        self.cmd_Soins.configure(activeforeground='black', activebackground='cyan',
            menu=meSoins)

        # Treatments
        self.cmd_ttt=Menubutton(self, text='Treatments', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_ttt.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meTtt = Menu(self.cmd_ttt)
        meTtt.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed1)
        meTtt.add_separator()
        meTtt.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed2)
        meTtt.add_separator()
        meTtt.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed3)
        meTtt.add_separator()
        meTtt.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed4)
        meTtt.add_separator()
        meTtt.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed5)
        meTtt.add_separator()
        meTtt.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed6)
        meTtt.add_separator()
        meTtt.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed7)
        # Integration of health and care menu
        self.cmd_ttt.configure(activeforeground='black', activebackground='cyan',
            menu=meTtt)

        # BMI menu
        self.cmd_BMI=Menubutton(self, text='Body Mass Indice', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_BMI.pack(side=LEFT, padx=3)
        # drop-down portion of BMI menu
        meBmi = Menu(self.cmd_BMI)
        meBmi.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB)
        meBmi.add_separator()
        meBmi.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB2)
        meBmi.add_separator()
        meBmi.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB3)
        meBmi.add_separator()
        meBmi.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB4)
        meBmi.add_separator()
        meBmi.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB5)
        meBmi.add_separator()
        meBmi.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB6)
        meBmi.add_separator()
        meBmi.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB7)
        # Integration of 3rd menu
        self.cmd_BMI.configure(activeforeground='black', activebackground='cyan',
            menu=meBmi)

        # Medical Visite
        self.cmd_Vmed=Menubutton(self, text='Medical Visit', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Vmed.pack(side=LEFT, padx=3)
        # drop-down portion of vmed
        meVmed = Menu(self.cmd_Vmed)
        meVmed.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed)
        meVmed.add_separator()
        meVmed.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed2)
        meVmed.add_separator()
        meVmed.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed3)
        meVmed.add_separator()
        meVmed.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed4)
        meVmed.add_separator()
        meVmed.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed5)
        meVmed.add_separator()
        meVmed.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed6)
        meVmed.add_separator()
        meVmed.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.visitMed7)
        # Integration of 3rd menu
        self.cmd_Vmed.configure(activeforeground='black', activebackground='cyan',
            menu=meVmed)

        # Nutrition menu for intolerance and hate meals
        self.cmd_Print=Menubutton(self, text='Intolerance All.', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Print.pack(side=LEFT, padx=3)
        # drop-down portion of nutrition
        mePrint = Menu(self.cmd_Print)
        mePrint.add_command(label=new_text, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu)
        mePrint.add_separator()
        mePrint.add_command(label=new_text2, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu2)
        mePrint.add_separator()
        mePrint.add_command(label=new_text3, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu3)
        mePrint.add_separator()
        mePrint.add_command(label=new_text4, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu4)
        mePrint.add_separator()
        mePrint.add_command(label=new_text5, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu5)
        mePrint.add_separator()
        mePrint.add_command(label=new_text6, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu6)
        mePrint.add_separator()
        mePrint.add_command(label=new_text7, font=('Times 14'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.nutritionMenu7)
        # Integration of nutrition menu
        self.cmd_Print.configure(activeforeground='black', activebackground='cyan',
            menu=mePrint)

        # Menu for showing all Graphs togather per patient 
        self.cmd_Graph=Menubutton(self, text='Global', font=("Times 14"), fg='cyan',
            bg='grey30', relief=GROOVE)
        self.cmd_Graph.pack(side=LEFT, padx=3)
        # drop-down portion of Graphics menu
        me1 = Menu(self.cmd_Graph)
        me2=Menu(me1)
        me2.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup)
        me1.add_cascade(label=new_text, underline=0, font=('Times 14'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me2)
        me1.add_separator()
        me3=Menu(me1)
        me3.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup2)
        me1.add_cascade(label=new_text2, underline=0, font=('Times 14'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me3)
        me1.add_separator()
        me4=Menu(me1)
        me4.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup3)
        me1.add_cascade(label=new_text3, underline=0, font=('Times 14'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me4)
        me1.add_separator()
        me5=Menu(me1)
        me5.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup4)
        me1.add_cascade(label=new_text4, underline=0, font=('Times 14'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me5)
        me1.add_separator()
        me6=Menu(me1)
        me6.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup5)
        me1.add_cascade(label=new_text5, underline=0, font=('Times 14'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me6)
        me1.add_separator()
        me7=Menu(me1)
        me7.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup6)
        me1.add_cascade(label=new_text6, underline=0, font=('Times 14'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me7)
        me1.add_separator()
        # Menu cascade extraordinaire !!!
        me8=Menu(me1)
        me8.add_command(label='All Files.txt', underline=0, font=('Times 14'),
            background='black', activebackground='cyan',
            foreground='cyan', activeforeground='black', command=boss.allFilesBackup7)
        # Integration of sub-menu
        me1.add_cascade(label=new_text7, underline=0, font=('Times 14'),
            background='black', foreground='cyan', 
            activeforeground='black', activebackground='cyan', menu=me8)
        # Integration of Graph menu
        self.cmd_Graph.configure(activeforeground='black', activebackground='cyan', menu=me1)

        # Manuals Nurse
        self.cmd_Intext=Menubutton(self, text='Manuals', font=('Times 14'), fg='cyan',
            bg='grey30', relief=GROOVE)
        self.cmd_Intext.pack(side=LEFT, padx=3)
        # drop-down portion of Manuals Nurse
        meIntext = Menu(self.cmd_Intext)
        meIntext.add_command(label='Click on it', font=('Times 14'), 
            background='black', activebackground='cyan', foreground='cyan',
            activeforeground='black', command=boss.manualFile)
        # Integration of Manuals Nurse
        self.cmd_Intext.configure(activeforeground='black', activebackground='cyan',
            menu=meIntext)

# Application principale (Main app)
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='grey22', padx=20, pady=20, relief=GROOVE)
        self.master.title('Time-Track- Developed by ko@l@tr33 - 2020')
        mBar = MenuBar(self)
        mBar.pack(side=TOP, fill=X, expand=YES)
        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='grey18')
        self.frame = Frame(self.can)
        self.vsb = Scrollbar(self, orient=VERTICAL, command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        # Insertion of picture
        self.photo = PhotoImage(file='./syno_gif/fondcolorbg.png')
        self.item = self.can.create_image(625, 400, image=self.photo)
        # Insertion of text
        self.can.create_text(625, 420, anchor=CENTER, 
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18, 'bold'), fill='turquoise')
        self.can.create_text(1240, 770, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # 3 buttons on welcome page.
        # Info button
        self.button1 = Button(self, text="Info", font=('Times 14 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=CENTER,
            window=self.button1)
        # Synopsis button
        self.button2 = Button(self, text="SYNOPSIS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.showsynopsis)
        self.button2.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button2_window = self.can.create_window(450, 550, anchor=CENTER,
            window=self.button2)
        # Psychotabs button
        self.button3 = Button(self, text="PSYCHOTABS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.launchPsycho)
        self.button3.configure(width=15, bd=3, highlightbackground='#82193e', 
            activebackground='dark turquoise')
        self.button3_window = self.can.create_window(790, 550, anchor=CENTER,
            window=self.button3)
        self.pack()
        
        # To check onto agenda if an appointment exist.
        self.agendaDateSearch()
        # To check onto ttt if a ttt is stopped today.
        self.tttDataSearch()
        # To check onto ttt if a reserve (ttt) is stopped today.
        self.reserveDataSearch()

    # Method to reconfigure scrollbar every time.
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.can.configure(scrollregion=self.can.bbox(ALL))

    def effacer(self):
        '''Reinitialize canvas when we pass through another'''
        self.can.delete(ALL)

    # Second page intro (a copy from the main app juste above)
    def secondPage(self):
        self.can.delete(ALL)
        # Insertion d'une image
        self.photo=PhotoImage(file='./syno_gif/fondcolor2.png')
        self.item=self.can.create_image(625, 400, image=self.photo)
        # Insertion du texte
        self.can.create_text(625, 420, anchor=CENTER,
            text="Python 3.6 - Tkinter 8.6 - GIMP 2.8",
            font=('Times New Roman', 18), fill='turquoise')
        self.can.create_text(1240, 770, anchor=NE, text="ko@l@tr33",
            font=('Times', 12), fill='turquoise')
        self.can.pack(side=RIGHT, fill=BOTH, expand=YES)
        # Configuration de la Scrollbar sur le Frame
        self.frame.bind("<Configure>", self.onFrameConfigure)
        # 3 buttons on welcome page.
        # Info button
        self.button1 = Button(self, text="Info", font=('Times 14 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.frameInfo)
        self.button1.configure(width=10, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=CENTER,
            window=self.button1)
        # Synopsis button
        self.button2 = Button(self, text="SYNOPSIS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.showsynopsis)
        self.button2.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button2_window = self.can.create_window(450, 550, anchor=CENTER,
            window=self.button2)
        # Statistics button
        self.button3 = Button(self, text="PSYCHOTABS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.launchPsycho)
        self.button3.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button3_window = self.can.create_window(790, 550, anchor=CENTER,
            window=self.button3)

        self.can.configure(scrollregion=self.can.bbox(ALL)) 

    def msgExit(self):
        MsgBox = messagebox.askyesno('Quit system', 'Do you want to quit ?')
        if MsgBox == 1:
            self.master.destroy()
        else:
            NoforQ = messagebox.showinfo('Return', 'You will now return to the'
                'application screen')

    # Installation of python and tkinter page
    def instalpy(self):
        self.can.delete(ALL)
        self.photo=PhotoImage(file='./syno_gif/pyt.gif')
        self.item=self.can.create_image(700, 400, image=self.photo)
        self.can.create_text(500, 20, anchor=NW,
            text="- MAPAPP -\n\n"

            "BACKUP and AGENDA :\n"
            "--------------------------------\n"
            "---> Backup has been programed for every first day of each month\n"
            "---> Agenda is verified every day and pop-up\n"
            "to show you if an appointment is fixed for tomorrow.\n\n"

            "SYNOPSIS\n\n"
            "Entry + Add patient ---> Allergy + Intolerance ---> 14 Needs ---> Care and Monitoring :\n"
            "---------------------------------------------------------------------------------------------------------\n"
            "Use 'Entry' button to enter for first time new patient. Use 'Add "
            "patient' once time all patients were enter \n"
            "(button to replace a patient who's left with delete button).\n"
            "Once time, patient had added use 'allergy' button to enter an allaergy "
            "if none, enter none!\n"
            "You can also use 'Intolerance' in the Menu Bar to complete 'allergy'.\n"
            "After it, Care and Monitoring is available only if you have entered one "
            "or more needs of patient.\n"
            "1 ---> 14 Needs\n"
            "2 ---> Care and monitoring\n\n"

            "Care and monitoring retrieve all data from :\n"
            "----------------------------------------------------\n"
            "+ Labo + Comburtest (urinary stix)\n"
            "+ ttt and R\n"
            "+ 14 Needs\n"
            "+ Externals Stackeholders\n\n"

            "Global :\n"
            "----------\n"
            "---> All txt files are consultable and accessibles\n"
            "---> Graphics : all Graphics open them-self to show you "
            "BMI, Weight(kg), TA, Puls, SaO2, FR, T°C,\n" 
            "and level of Pain\n"
            "---> Angel Eye : tetra vision about : BMI, Vital parameters, Visit "
            "Medical and Care and Monitoring.\n"
            "---> Global Vision : tetra vision about : Diagnosis, Agenda, Auxiliary "
            "resources and Story Life.\n\n"
            "PSYCHOTABS\n\n"
            "Psychotabs is an application only for consulting neurleptics treatments.\n\n"
            "\nDevelopped on Linux Xubuntu (xfce4) Voyager 18.04 by Cédric Kuchen - alias ko@l@tr33\n",
            font=('Times', 13), fill='aquamarine')
        self.can.configure(scrollregion=self.can.bbox(ALL))

        # call func in boxapp.py
    def showsynopsis(self):
        callBox(self)

    def agendaDateSearch(self):
        displayDates(self)

    def tttDataSearch(self):
        """
        To search the end date into the intro_ttt.txt 
        and display alert to stop ttt !
        """
        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt/convdose.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 1 which is stopped today!')
        except FileNotFoundError as info_ttt:
            print("No date of end has been found for ttt into file convdose.json (patient 1)", info_ttt)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt2/convdose.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 2 which is stopped today!')
        except FileNotFoundError as info_ttt2:
            print("No date of end has been found for ttt into file convdose.json (patient 2)", info_ttt2)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt3/convdose.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 3 which is stopped today!')
        except FileNotFoundError as info_ttt3:
            print("No date of end has been found for ttt into file convdose.json (patient 3)", info_ttt3)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt4/convdose.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 4 which is stopped today!')
        except FileNotFoundError as info_ttt4:
            print("No date of end has been found for ttt into file convdose.json (patient 4)", info_ttt4)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt5/convdose.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 5 which is stopped today!')
        except FileNotFoundError as info_ttt5:
            print("No date of end has been found for ttt into file convdose.json (patient 5)", info_ttt5)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt6/convdose.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 6 which is stopped today!')
        except FileNotFoundError as info_ttt6:
            print("No date of end has been found for ttt into file convdose.json (patient 6)", info_ttt6)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            initword = "Date of end : "
            with open('./ttt/doc_ttt7/convdose.json', 'r') as filedate:
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBTTT2 = messagebox.showwarning('Info',
                                'Look at TTT, there is a ttt for patient \
                                 7 which is stopped today!')
        except FileNotFoundError as info_ttt7:
            print("No date of end has been found for ttt into file convdose.json (patient 7)", info_ttt7)
        else:
            ("Error unknow")

    def reserveDataSearch(self):
        """
        To search the end date into the intro_res.txt 
        and display alert to stop reserve !
        """
        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            res_initword = "Date of end : "
            with open('./ttt/doc_ttt/conv_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if res_initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBRES2 = messagebox.showwarning('Info',
                                'Look at RESERVE onto TTT, there is a RESERVE \
                                 for patient 1 which is stopped today!')
        except FileNotFoundError as info_res1:
            print("No date of end has been found for reserve into file convres.json (patient 1)", info_res1)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            res_initword = "Date of end : "
            with open('./ttt/doc_ttt2/conv_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if res_initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBRES2 = messagebox.showwarning('Info',
                                'Look at RESERVE onto TTT, there is a RESERVE \
                                 for patient 2 which is stopped today!')
        except FileNotFoundError as info_res2:
            print("No date of end has been found for reserve into file convres.json (patient 2)", info_res2)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            res_initword = "Date of end : "
            with open('./ttt/doc_ttt3/conv_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if res_initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBRES2 = messagebox.showwarning('Info',
                                'Look at RESERVE onto TTT, there is a RESERVE \
                                 for patient 3 which is stopped today!')
        except FileNotFoundError as info_res3:
            print("No date of end has been found for reserve into file convres.json (patient 3)", info_res3)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            res_initword = "Date of end : "
            with open('./ttt/doc_ttt4/conv_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if res_initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBRES2 = messagebox.showwarning('Info',
                                'Look at RESERVE onto TTT, there is a RESERVE \
                                 for patient 4 which is stopped today!')
        except FileNotFoundError as info_res4:
            print("No date of end has been found for reserve into file convres.json (patient 4)", info_res4)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            res_initword = "Date of end : "
            with open('./ttt/doc_ttt5/conv_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if res_initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBRES2 = messagebox.showwarning('Info',
                                'Look at RESERVE onto TTT, there is a RESERVE \
                                 for patient 5 which is stopped today!')
        except FileNotFoundError as info_res5:
            print("No date of end has been found for reserve into file convres.json (patient 5)", info_res5)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            res_initword = "Date of end : "
            with open('./ttt/doc_ttt6/conv_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if res_initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBRES2 = messagebox.showwarning('Info',
                                'Look at RESERVE onto TTT, there is a RESERVE \
                                 for patient 6 which is stopped today!')
        except FileNotFoundError as info_res6:
            print("No date of end has been found for reserve into file convres.json (patient 6)", info_res6)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
            res_initword = "Date of end : "
            with open('./ttt/doc_ttt7/conv_res.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if res_initword in line:
                        print(line)
                        if dateagenda in line:
                            print(line)
                            MSBRES2 = messagebox.showwarning('Info',
                                'Look at RESERVE onto TTT, there is a RESERVE \
                                 for patient 7 which is stopped today!')
        except FileNotFoundError as info_res7:
            print("No date of end has been found for reserve into file convres.json (patient 7)", info_res7)
        else:
            ("Error unknow")

    def frameInfo(self):
        """
        Info for button on first page
        """
        self.lab=Tk()
        self.lab.title("ATCD")
        self.lab.configure(bg="grey22")

        self.labFra=LabelFrame(self.lab, text="\nWelcome !",
            font=("Arial 12"),fg='cyan', bg='grey22')
        self.labFra.pack(padx=5, pady=5)
        self.separator = Frame(self.labFra, height=2, bd=1,
            relief=SUNKEN)

        self.lab4=Label(self.labFra, text="\nInfo",
            font=('Times 16 bold'), fg='cyan', bg='grey22').pack()
        self.separator = Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=100, pady=3)

        self.lab5=Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="\nMenu Bar and Synopsis are the most usefull skills\n"
            "to perform onto this app ! If you need help, you\n" 
            "can go to MapApp to access map of this app and\n" 
            "understand how the app is used.\n\n"
            "Enjoy it ! ;)\n").pack(padx=10)
        self.separator = Frame(self.labFra, height=2, bd=1, relief=SUNKEN)
        self.separator.pack(fill=X, padx=30, pady=3)
        self.lab6=Label(self.labFra, justify=LEFT, fg='cyan',
            bg='grey22', font=('Times', 14),
            text="Path : Menu Bar --> Menu --> MapApp").pack(padx=10, pady=10)

    # For new entry
    def callPatient1(self):
        subprocess.call('./newpatient/entrypytientfile.py')

    def delEverPat(self):
        subprocess.call('./deletepatient/deleverything.py')

    def addPatientAfter(self):
        messagebox.showwarning("Warning", "Don't forget to enter allergy too ! ;)")
        subprocess.call('./newpatient/torecord.py')
        
    # CheckBox 14 needs OK
    def besoinsCoche(self):
        subprocess.call('./14besoins/checkb.py')

    def besoins2Coche(self):
        subprocess.call('./14besoins/checkb2.py')

    def besoins3Coche(self):
        subprocess.call('./14besoins/checkb3.py')

    def besoins4Coche(self):
        subprocess.call('./14besoins/checkb4.py')

    def besoins5Coche(self):
        subprocess.call('./14besoins/checkb5.py')

    def besoins6Coche(self):
        subprocess.call('./14besoins/checkb6.py')

    def besoins7Coche(self):
        subprocess.call('./14besoins/checkb7.py')

    def launchPsycho(self):
        subprocess.call('./psychotabs.py')

    # Agenda
    def patientAgenda(self):
        subprocess.call('./patient_agenda/origin_agenda.py')

    def patientAgenda2(self):
        subprocess.call('./patient_agenda/origin_agenda2.py')

    def patientAgenda3(self):
        subprocess.call('./patient_agenda/origin_agenda3.py')

    def patientAgenda4(self):
        subprocess.call('./patient_agenda/origin_agenda4.py')

    def patientAgenda5(self):
        subprocess.call('./patient_agenda/origin_agenda5.py')

    def patientAgenda6(self):
        subprocess.call('./patient_agenda/origin_agenda6.py')

    def patientAgenda7(self):
        subprocess.call('./patient_agenda/origin_agenda7.py')

    # Func 14 needs suivi OK
    def suiviSoins1(self):
        subprocess.call("./14besoins/suivi_patient_1.py")

    def suiviSoins2(self):
        subprocess.call("./14besoins/suivi_patient_2.py")

    def suiviSoins3(self):
        subprocess.call("./14besoins/suivi_patient_3.py")

    def suiviSoins4(self):
        subprocess.call("./14besoins/suivi_patient_4.py")

    def suiviSoins5(self):
        subprocess.call("./14besoins/suivi_patient_5.py")

    def suiviSoins6(self):
        subprocess.call("./14besoins/suivi_patient_6.py")

    def suiviSoins7(self):
        subprocess.call("./14besoins/suivi_patient_7.py")

    # treatments
    def tttMed1(self):
        subprocess.call("./ttt/patienttt1.py")

    def tttMed2(self):
        subprocess.call("./ttt/patienttt2.py")

    def tttMed3(self):
        subprocess.call("./ttt/patienttt3.py")

    def tttMed4(self):
        subprocess.call("./ttt/patienttt4.py")

    def tttMed5(self):
        subprocess.call("./ttt/patienttt5.py")

    def tttMed6(self):
        subprocess.call("./ttt/patienttt6.py")

    def tttMed7(self):
        subprocess.call("./ttt/patienttt7.py")
    
    # Func BMI
    def calculB(self):
        subprocess.call("./calBmi/CalculBmi.py")

    def calculB2(self):
        subprocess.call("./calBmi/CalculBmi2.py")

    def calculB3(self):
        subprocess.call("./calBmi/CalculBmi3.py")

    def calculB4(self):
        subprocess.call("./calBmi/CalculBmi4.py")

    def calculB5(self):
        subprocess.call("./calBmi/CalculBmi5.py")

    def calculB6(self):
        subprocess.call("./calBmi/CalculBmi6.py")

    def calculB7(self):
        subprocess.call("./calBmi/CalculBmi7.py")

    # Func Visit MED
    def visitMed(self):
        subprocess.call("./vmed/vm_patient1.py")
        
    def visitMed2(self):
        subprocess.call("./vmed/vm_patient2.py")
        
    def visitMed3(self):
        subprocess.call("./vmed/vm_patient3.py")
        
    def visitMed4(self):
        subprocess.call("./vmed/vm_patient4.py")
        
    def visitMed5(self):
        subprocess.call("./vmed/vm_patient5.py")
        
    def visitMed6(self):
        subprocess.call("./vmed/vm_patient6.py")
        
    def visitMed7(self):
        subprocess.call("./vmed/vm_patient7.py")

    # Allergy OK
    def allergyLink(self):
        subprocess.call('./allergy/allerpatient1.py')

    def allergyLink2(self):
        subprocess.call('./allergy/allerpatient2.py')

    def allergyLink3(self):
        subprocess.call('./allergy/allerpatient3.py')

    def allergyLink4(self):
        subprocess.call('./allergy/allerpatient4.py')

    def allergyLink5(self):
        subprocess.call('./allergy/allerpatient5.py')

    def allergyLink6(self):
        subprocess.call('./allergy/allerpatient6.py')

    def allergyLink7(self):
        subprocess.call('./allergy/allerpatient7.py')

    # Func labo
    def laboResult(self):
        subprocess.call('./labo/resultlabo1.py')

    def laboResult2(self):
        subprocess.call('./labo/resultlabo2.py')

    def laboResult3(self):
        subprocess.call('./labo/resultlabo3.py')

    def laboResult4(self):
        subprocess.call('./labo/resultlabo4.py')

    def laboResult5(self):
        subprocess.call('./labo/resultlabo5.py')

    def laboResult6(self):
        subprocess.call('./labo/resultlabo6.py')

    def laboResult7(self):
        subprocess.call('./labo/resultlabo7.py')

    # Func Diagnostic
    def diag1(self):
        subprocess.call("./diag/diag_patient1.py")

    def diag2(self):
        subprocess.call("./diag/diag_patient2.py")

    def diag3(self):
        subprocess.call("./diag/diag_patient3.py")

    def diag4(self):
        subprocess.call("./diag/diag_patient4.py")

    def diag5(self):
        subprocess.call("./diag/diag_patient5.py")

    def diag6(self):
        subprocess.call("./diag/diag_patient6.py")

    def diag7(self):
        subprocess.call("./diag/diag_patient7.py")

    # Manual nurse
    def manualFile(self):
        subprocess.call('./manual/pdfopenmanual.py')

    # Menu print
    def nutritionMenu(self):
        subprocess.call('./nutrition/nutrit_patient1.py')

    def nutritionMenu2(self):
        subprocess.call('./nutrition/nutrit_patient2.py')

    def nutritionMenu3(self):
        subprocess.call('./nutrition/nutrit_patient3.py')

    def nutritionMenu4(self):
        subprocess.call('./nutrition/nutrit_patient4.py')

    def nutritionMenu5(self):
        subprocess.call('./nutrition/nutrit_patient5.py')

    def nutritionMenu6(self):
        subprocess.call('./nutrition/nutrit_patient6.py')

    def nutritionMenu7(self):
        subprocess.call('./nutrition/nutrit_patient7.py')

    def newsTextBox(self):
        self.can.textBox = Text(app, text = "")

    # Backup
    def allFilesBackup(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files1",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        # I have to try with Text (else no scrollbar)
        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup2(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files2",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup3(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files3",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup4(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files4",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup5(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files5",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup6(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files6",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    # Backup
    def allFilesBackup7(self):
        self.label=Tk()
        self.label.title("Search File")
        filepath = filedialog.askopenfilename(initialdir = "./Backup/Files7",
            title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
        print(filepath)
        with open(filepath, 'r') as fichier:
            content = fichier.read()

        self.label=Label(self.label, justify=LEFT, font=('Times 14'),
            bg='gray22', fg='cyan', text=content).pack(padx=3, pady=3)

    def updateFiletxt(self):
        # To backup all files
        listeDate = ["01/05/2020", "18/06/2020", "01/07/2020",
        "01/08/2020", "01/09/2020", "01/10/2020", "01/11/2020",
        "01/12/2020"]
        
        for i in listeDate:
            try:
                if time.strftime("%d/%m/%Y") == i:
                    MSB = messagebox.showinfo('Info', 'Backup is done at the first of each month')
                    subprocess.call('./Backup/backupfile.py')
                    print("+ Backup is done !")
            except FileNotFoundError as errout:
                print("+ It is not the right date for backup, next will" \
                    "be at the first of next month)", errout)

        self.can.configure(scrollregion=self.can.bbox(ALL))

    def upDateAll(self):
        self.master.destroy()
        subprocess.call('./time_track.py')

if __name__=='__main__':
    app = Application()
    app.mainloop()
