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
        new_text8=StringVar()
        new_text9=StringVar()
        new_text10=StringVar()
        new_text11=StringVar()
        new_text12=StringVar()
        new_text13=StringVar()
        new_text14=StringVar()
        new_text15=StringVar()
        new_text16=StringVar()
        new_text17=StringVar()
        new_text18=StringVar()
        new_text19=StringVar()
        new_text20=StringVar()

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
        
        # For label below (in me.add_command)
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

        try:
            with open('./newpatient/entryfile8.txt', 'r') as namefile:
                line8=namefile.readline()
                new_text8=line8
        except FileNotFoundError as fileout8:
            print("No file entryfile8.txt exist", fileout8)

        try:
            with open('./newpatient/entryfile9.txt', 'r') as namefile:
                line9=namefile.readline()
                new_text9=line9
        except FileNotFoundError as fileout9:
            print("No file entryfile9.txt exist", fileout9)

        try:
            with open('./newpatient/entryfile10.txt', 'r') as namefile:
                line10=namefile.readline()
                new_text10=line10
        except FileNotFoundError as fileout10:
            print("No file entryfile10.txt exist", fileout10)

        try:
            with open('./newpatient/entryfile11.txt', 'r') as namefile:
                line11=namefile.readline()
                new_text11=line11
        except FileNotFoundError as fileout11:
            print("No file entryfile11.txt exist", fileout11)

        try:
            with open('./newpatient/entryfile12.txt', 'r') as namefile:
                line12=namefile.readline()
                new_text12=line12
        except FileNotFoundError as fileout12:
            print("No file entryfile12.txt exist", fileout12)

        try:
            with open('./newpatient/entryfile13.txt', 'r') as namefile:
                line13=namefile.readline()
                new_text13=line13
        except FileNotFoundError as fileout13:
            print("No file entryfile13.txt exist", fileout13)

        try:
            with open('./newpatient/entryfile14.txt', 'r') as namefile:
                line14=namefile.readline()
                new_text14=line14
        except FileNotFoundError as fileout14:
            print("No file entryfile14.txt exist", fileout14)

        try:
            with open('./newpatient/entryfile15.txt', 'r') as namefile:
                line15=namefile.readline()
                new_text15=line15
        except FileNotFoundError as fileout15:
            print("No file entryfile15.txt exist", fileout15)

        try:
            with open('./newpatient/entryfile16.txt', 'r') as namefile:
                line16=namefile.readline()
                new_text16=line16
        except FileNotFoundError as fileout16:
            print("No file entryfile16.txt exist", fileout16)

        try:
            with open('./newpatient/entryfile17.txt', 'r') as namefile:
                line17=namefile.readline()
                new_text17=line17
        except FileNotFoundError as fileout17:
            print("No file entryfile17.txt exist", fileout17)

        try:
            with open('./newpatient/entryfile18.txt', 'r') as namefile:
                line18=namefile.readline()
                new_text18=line18
        except FileNotFoundError as fileout18:
            print("No file entryfile18.txt exist", fileout18)

        try:
            with open('./newpatient/entryfile19.txt', 'r') as namefile:
                line19=namefile.readline()
                new_text19=line19
        except FileNotFoundError as fileout19:
            print("No file entryfile19.txt exist", fileout19)

        try:
            with open('./newpatient/entryfile20.txt', 'r') as namefile:
                line20=namefile.readline()
                new_text20=line20
        except FileNotFoundError as fileout20:
            print("No file entryfile20.txt exist", fileout20)

        # Agenda menu
        self.cmd_agenda=Menubutton(self, text='Agenda', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_agenda.pack(side=LEFT, padx=3)
        me3 = Menu(self.cmd_agenda)
        # Partie déroulante du menu agenda
        me3.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda)
        me3.add_separator()
        me3.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda2)
        me3.add_separator()
        me3.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda3)
        me3.add_separator()
        me3.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda4)
        me3.add_separator()
        me3.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda5)
        me3.add_separator()
        me3.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda6)
        me3.add_separator()
        me3.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda7)
        me3.add_separator()
        me3.add_command(label=new_text8, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda8)
        me3.add_separator()
        me3.add_command(label=new_text9, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda9)
        me3.add_separator()
        me3.add_command(label=new_text10, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda10)
        me3.add_separator()
        me3.add_command(label=new_text11, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda11)
        me3.add_separator()
        me3.add_command(label=new_text12, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda12)
        me3.add_separator()
        me3.add_command(label=new_text13, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda13)
        me3.add_separator()
        me3.add_command(label=new_text14, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda14)
        me3.add_separator()
        me3.add_command(label=new_text15, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda15)
        me3.add_separator()
        me3.add_command(label=new_text16, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda16)
        me3.add_separator()
        me3.add_command(label=new_text17, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda17)
        me3.add_separator()
        me3.add_command(label=new_text18, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda18)
        me3.add_separator()
        me3.add_command(label=new_text19, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda19)
        me3.add_separator()
        me3.add_command(label=new_text20, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.patientAgenda20)
        # Integration of agenda menu
        self.cmd_agenda.configure(activeforeground='black', activebackground='cyan', 
            menu=me3)

        # 14 besoins menu
        self.cmd_Besoins=Menubutton(self, text='14 Needs', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Besoins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu 14b
        me4 = Menu(self.cmd_Besoins)
        me4.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoinsCoche)
        me4.add_separator()
        me4.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins2Coche)
        me4.add_separator()
        me4.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins3Coche)
        me4.add_separator()
        me4.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins4Coche)
        me4.add_separator()
        me4.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins5Coche)
        me4.add_separator()
        me4.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins6Coche)
        me4.add_separator()
        me4.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins7Coche)
        me4.add_separator()
        me4.add_command(label=new_text8, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins8Coche)
        me4.add_separator()
        me4.add_command(label=new_text9, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins9Coche)
        me4.add_separator()
        me4.add_command(label=new_text10, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins10Coche)
        me4.add_separator()
        me4.add_command(label=new_text11, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins11Coche)
        me4.add_separator()
        me4.add_command(label=new_text12, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins12Coche)
        me4.add_separator()
        me4.add_command(label=new_text13, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins13Coche)
        me4.add_separator()
        me4.add_command(label=new_text14, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins14Coche)
        me4.add_separator()
        me4.add_command(label=new_text15, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins15Coche)
        me4.add_separator()
        me4.add_command(label=new_text16, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins16Coche)
        me4.add_separator()
        me4.add_command(label=new_text17, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins17Coche)
        me4.add_separator()
        me4.add_command(label=new_text18, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins18Coche)
        me4.add_separator()
        me4.add_command(label=new_text19, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins19Coche)
        me4.add_separator()
        me4.add_command(label=new_text20, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.besoins20Coche)
        # Integration of 14b menu
        self.cmd_Besoins.configure(activeforeground='black', activebackground='cyan',
            menu=me4)

        # Helth and care menu
        self.cmd_Soins=Menubutton(self, text='Care and monitoring', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_Soins.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meSoins = Menu(self.cmd_Soins)
        meSoins.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins1)
        meSoins.add_separator()
        meSoins.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins2)
        meSoins.add_separator()
        meSoins.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins3)
        meSoins.add_separator()
        meSoins.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins4)
        meSoins.add_separator()
        meSoins.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins5)
        meSoins.add_separator()
        meSoins.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins6)
        meSoins.add_separator()
        meSoins.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins7)
        meSoins.add_separator()
        meSoins.add_command(label=new_text8, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins8)
        meSoins.add_separator()
        meSoins.add_command(label=new_text9, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins9)
        meSoins.add_separator()
        meSoins.add_command(label=new_text10, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins10)
        meSoins.add_separator()
        meSoins.add_command(label=new_text11, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins11)
        meSoins.add_separator()
        meSoins.add_command(label=new_text12, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins12)
        meSoins.add_separator()
        meSoins.add_command(label=new_text13, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins13)
        meSoins.add_separator()
        meSoins.add_command(label=new_text14, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins14)
        meSoins.add_separator()
        meSoins.add_command(label=new_text15, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins15)
        meSoins.add_separator()
        meSoins.add_command(label=new_text16, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins16)
        meSoins.add_separator()
        meSoins.add_command(label=new_text17, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins17)
        meSoins.add_separator()
        meSoins.add_command(label=new_text18, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins18)
        meSoins.add_separator()
        meSoins.add_command(label=new_text19, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins19)
        meSoins.add_separator()
        meSoins.add_command(label=new_text20, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.suiviSoins20)
        # Integration of health and care menu
        self.cmd_Soins.configure(activeforeground='black', activebackground='cyan',
            menu=meSoins)

        # Treatments
        self.cmd_ttt=Menubutton(self, text='Treatments', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_ttt.pack(side=LEFT, padx=3)
        # Partie déroulante du menu health and care
        meTtt = Menu(self.cmd_ttt)
        meTtt.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed1)
        meTtt.add_separator()
        meTtt.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed2)
        meTtt.add_separator()
        meTtt.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed3)
        meTtt.add_separator()
        meTtt.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed4)
        meTtt.add_separator()
        meTtt.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed5)
        meTtt.add_separator()
        meTtt.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed6)
        meTtt.add_separator()
        meTtt.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed7)
        meTtt.add_separator()
        meTtt.add_command(label=new_text8, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed8)
        meTtt.add_separator()
        meTtt.add_command(label=new_text9, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed9)
        meTtt.add_separator()
        meTtt.add_command(label=new_text10, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed10)
        meTtt.add_separator()
        meTtt.add_command(label=new_text11, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed11)
        meTtt.add_separator()
        meTtt.add_command(label=new_text12, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed12)
        meTtt.add_separator()
        meTtt.add_command(label=new_text13, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed13)
        meTtt.add_separator()
        meTtt.add_command(label=new_text14, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed14)
        meTtt.add_separator()
        meTtt.add_command(label=new_text15, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed15)
        meTtt.add_separator()
        meTtt.add_command(label=new_text16, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed16)
        meTtt.add_separator()
        meTtt.add_command(label=new_text17, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed17)
        meTtt.add_separator()
        meTtt.add_command(label=new_text18, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed18)
        meTtt.add_separator()
        meTtt.add_command(label=new_text19, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed19)
        meTtt.add_separator()
        meTtt.add_command(label=new_text20, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.tttMed20)
        # Integration of health and care menu
        self.cmd_ttt.configure(activeforeground='black', activebackground='cyan',
            menu=meTtt)

        # BMI menu
        self.cmd_BMI=Menubutton(self, text='Body Mass Indice', font=("Times 14"),
            fg='cyan', bg='grey30', relief=GROOVE)
        self.cmd_BMI.pack(side=LEFT, padx=3)
        # drop-down portion of BMI menu
        meBmi = Menu(self.cmd_BMI)
        meBmi.add_command(label=new_text, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB)
        meBmi.add_separator()
        meBmi.add_command(label=new_text2, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB2)
        meBmi.add_separator()
        meBmi.add_command(label=new_text3, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB3)
        meBmi.add_separator()
        meBmi.add_command(label=new_text4, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB4)
        meBmi.add_separator()
        meBmi.add_command(label=new_text5, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB5)
        meBmi.add_separator()
        meBmi.add_command(label=new_text6, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB6)
        meBmi.add_separator()
        meBmi.add_command(label=new_text7, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB7)
        meBmi.add_separator()
        meBmi.add_command(label=new_text8, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB8)
        meBmi.add_separator()
        meBmi.add_command(label=new_text9, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB9)
        meBmi.add_separator()
        meBmi.add_command(label=new_text10, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB10)
        meBmi.add_separator()
        meBmi.add_command(label=new_text11, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB11)
        meBmi.add_separator()
        meBmi.add_command(label=new_text12, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB12)
        meBmi.add_separator()
        meBmi.add_command(label=new_text13, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB13)
        meBmi.add_separator()
        meBmi.add_command(label=new_text14, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB14)
        meBmi.add_separator()
        meBmi.add_command(label=new_text15, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB15)
        meBmi.add_separator()
        meBmi.add_command(label=new_text16, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB16)
        meBmi.add_separator()
        meBmi.add_command(label=new_text17, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB17)
        meBmi.add_separator()
        meBmi.add_command(label=new_text18, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB18)
        meBmi.add_separator()
        meBmi.add_command(label=new_text19, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB19)
        meBmi.add_separator()
        meBmi.add_command(label=new_text20, font=('Times 16'), background='black',
            activebackground='cyan', foreground='cyan', activeforeground='black',
            command=boss.calculB20)
        # Integration of 3rd menu
        self.cmd_BMI.configure(activeforeground='black', activebackground='cyan',
            menu=meBmi)

# Application principale (Main app)
class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='grey22', padx=20, pady=20, relief=GROOVE)
        self.master.title('TIME-TRACK - Developed by ko@l@tr33 - 2020')
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
        self.button1.configure(width=10, bd=3, highlightbackground='navy',
            activebackground='dark turquoise')
        self.button1_window = self.can.create_window(75, 30, anchor=CENTER,
            window=self.button1)
        # Synopsis button
        self.button2 = Button(self, text="TIME-TRACK", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.showsynopsis)
        self.button2.configure(width=15, bd=3, highlightbackground='navy',
            activebackground='dark turquoise')
        self.button2_window = self.can.create_window(450, 550, anchor=CENTER,
            window=self.button2)
        # Psychotabs button
        self.button3 = Button(self, text="PSYCHOTABS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.launchPsycho)
        self.button3.configure(width=15, bd=3, highlightbackground='navy', 
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
        self.photo=PhotoImage(file='./syno_gif/angelbg.png')
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
        self.button2 = Button(self, text="TIME-TRACK", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.showsynopsis)
        self.button2.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button2_window = self.can.create_window(450, 550, anchor=CENTER,
            window=self.button2)
        self.can.configure(scrollregion=self.can.bbox(ALL)) 
        # Statistics button
        self.button3 = Button(self, text="PSYCHOTABS", font=('Times 18 bold'),
            bg='RoyalBlue3', fg='cyan', command = self.launchPsycho)
        self.button3.configure(width=15, bd=3, highlightbackground='#82193e',
            activebackground='dark turquoise')
        self.button3_window = self.can.create_window(790, 550, anchor=CENTER,
            window=self.button3)
        self.pack()

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

            "TIME-TRACK\n\n"
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
            "+ BMI\n"
            "+ Agenda\n\n"

            "PSYCHOTABS\n\n"
            "Psychotabs is an application only for consulting neurleptics treatments.\n\n"
            "\nDevelopped on Linux Xubuntu (xfce4) Voyager 18.04 by Cédric Kuchen - alias ko@l@tr33\n",
            font=('Times', 13), fill='aquamarine')
        self.can.configure(scrollregion=self.can.bbox(ALL))

    # Synopsis page
    def showsynopsis(self):
        self.can.delete(ALL)
        self.photo=PhotoImage(file='./syno_gif/fondcolor2.png')
        self.item=self.can.create_image(625, 400, image=self.photo)
        #self.can.create_text(625, 80, anchor=CENTER, text="TIME-TRACK",
        #    font=('Times New Roman', 40), fill='turquoise')

        self.x1, self.y1 = 1100, 50
        self.Date_write=Entry(self.can)
        self.data_time=StringVar()
        self.Date_write=Entry(textvariable=self.data_time, width=10,
            highlightbackground='grey', bd=4)
        self.data_time.set(time.strftime("%d/%m/%Y"))
        self.Date_write=self.can.create_window(self.x1, self.y1,
            window=self.Date_write)

        # To backup
        self.updateFiletxt()

        # Static time
        self.x2, self.y2 = 1100, 100
        self.Date_write2 = Entry(self.can)
        self.data_time2 = StringVar()
        self.Date_write2 = Entry(width=10, textvariable=self.data_time2,
            highlightbackground='grey', bd=4)
        self.data_time2.set(time.strftime("%H:%M:%S %p"))
        self.Date_write2=self.can.create_window(self.x2, self.y2,
            window=self.Date_write2)
        # To display time dynamically

        # To introduce a new pytient
        self.x100, self.y100 = 130, 50
        self.b100=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='white', activebackground='dark turquoise',
            text="New Entry", command=self.callPatient1)
        self.fb100=self.can.create_window(self.x100, self.y100, window=self.b100)
        
        # To refresh canvas + menu bar
        self.x101, self.y101 = 270, 50
        self.b101=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='SpringGreen2', activebackground='yellow', activeforeground='blue',
            text="Refresh", command=self.upDateAll)
        self.fb101=self.can.create_window(self.x101, self.y101, window=self.b101)

        # To delete one patient and all files
        self.x200, self.y200 = 130, 100
        self.b200=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='coral', activebackground='black', activeforeground='red',
            text="Delete patient", command=self.delEverPat)
        self.fb200=self.can.create_window(self.x200, self.y200, window=self.b200)

        # To add one patient and files
        self.x200, self.y200 = 270, 100
        self.b200=Button(self.can, width=10, font=16, bd=3, highlightbackground='#82193e',
            bg='RoyalBlue3', fg='cyan', activebackground='dark turquoise', 
            text="Add patient", command=self.addPatientAfter)
        self.fb200=self.can.create_window(self.x200, self.y200, window=self.b200)

        # TextBox
        self.x63, self.y63 = 625, 325 #625, 600
        self.t63=Text(self.can, height=15, width=60, font=18, relief=SUNKEN)
        self.t63.insert(INSERT, "Previously (yesterday last infos) : ")
        self.t63.insert(END, (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%d/%m/%Y'))
            #time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
        self.ft63=self.can.create_window(self.x63, self.y63, window=self.t63)

        #Patient1
        # For label below (in me2.add_command)
        try:
            with open('./newpatient/entryfile.txt', 'r') as namefile:
                line1=namefile.readline()
        except FileNotFoundError as callfile:
            print("File entryfile.txt doen't exist !", callfile)

        self.data_time=line1
        self.x2, self.y2 = 129, 525 #200
        self.Data_write=Entry(self.can)
        self.new_data1=StringVar()
        self.Data_write=Entry(textvariable=self.new_data1,
            highlightbackground='grey', bd=4)
        self.new_data1.set(line1)
        self.Data_write=self.can.create_window(self.x2, self.y2,
            window=self.Data_write)

        self.x3, self.y3 = 271, 525
        self.b=Button(self.can, width=8, font=16, bg='grey30', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink)
        self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

        self.x3, self.y3 = 429, 525
        self.b=Button(self.can, width=18, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag1)
        self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

        self.x4, self.y4 = 597, 525
        self.b4=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult)
        self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)

        # Patient 2
        try:
            with open('./newpatient/entryfile2.txt', 'r') as namefile:
                line2=namefile.readline()
        except FileNotFoundError as callfile2:
            print("File entryfile2.txt doen't exist !", callfile2)

        self.new_data2=line2
        self.x9, self.y9 = 129, 557
        self.Data_write=Entry(self.can)
        self.new_data2=StringVar()
        self.Data_write=Entry(textvariable=self.new_data2,
          highlightbackground='grey', bd=4)
        self.new_data2.set(line2)
        self.Data_write=self.can.create_window(self.x9, self.y9,
          window=self.Data_write)

        self.x10, self.y10 = 271, 557 #232
        self.b10=Button(self.can, width=8, font=16, bg='grey25', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink2)
        self.fb10=self.can.create_window(self.x10, self.y10, window=self.b10)

        self.x13, self.y13 = 429, 557
        self.b13=Button(self.can, width=18, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag2)
        self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

        self.x14, self.y14 = 597, 557
        self.b14=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult2)
        self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)

        # Patient 3
        try:
            with open('./newpatient/entryfile3.txt', 'r') as namefile:
                line3=namefile.readline()
        except FileNotFoundError as callfile3:
            print("File entryfile3.txt doen't exist !", callfile3)

        self.new_data3=line3
        self.x18, self.y18 = 129, 589 #264
        self.Data_write=Entry(self.can)
        self.new_data3=StringVar()
        self.Data_write=Entry(textvariable=self.new_data3,
          highlightbackground='grey', bd=4)
        self.new_data3.set(line3)
        self.Data_write=self.can.create_window(self.x18, self.y18,
          window=self.Data_write)

        self.x19, self.y19 = 271, 589
        self.b19=Button(self.can, width=8, font=16, bg='grey20', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink3)
        self.fb19=self.can.create_window(self.x19, self.y19, window=self.b19)

        self.x22, self.y22 = 429, 589
        self.b22=Button(self.can, width=18, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag3)
        self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)

        self.x23, self.y23 = 597, 589
        self.b23=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult3)
        self.fb23=self.can.create_window(self.x23, self.y23, window=self.b23)

        # Patient 4
        try:
            with open('./newpatient/entryfile4.txt', 'r') as namefile:
                line4=namefile.readline()
        except FileNotFoundError as callfile4:
            print("File entryfile4.txt doen't exist !", callfile4)

        self.new_data4=line4
        self.x27, self.y27 = 129, 621 #296
        self.Data_write=Entry(self.can)
        self.new_data4=StringVar()
        self.Data_write=Entry(textvariable=self.new_data4,
          highlightbackground='grey', bd=4)
        self.new_data4.set(line4)
        self.Data_write=self.can.create_window(self.x27, self.y27,
          window=self.Data_write)

        self.x28, self.y28 = 271, 621
        self.b28=Button(self.can, width=8, font=16, bg='grey18', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink4)
        self.fb28=self.can.create_window(self.x28, self.y28, window=self.b28)

        self.x31, self.y31 = 429, 621
        self.b31=Button(self.can, width=18, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag4)
        self.fb31=self.can.create_window(self.x31, self.y31, window=self.b31)

        self.x32, self.y32 = 597, 621
        self.b32=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult4)
        self.fb32=self.can.create_window(self.x32, self.y32, window=self.b32)

        #patient5
        try:
            with open('./newpatient/entryfile5.txt', 'r') as namefile:
                line5=namefile.readline()
        except FileNotFoundError as callfile5:
            print("File entryfile5.txt doen't exist !", callfile5)

        self.new_data5=line5
        self.x36, self.y36 = 129, 653 #328
        self.Data_write=Entry(self.can)
        self.new_data5=StringVar()
        self.Data_write=Entry(textvariable=self.new_data5,
          highlightbackground='grey', bd=4)
        self.new_data5.set(line5)
        self.Data_write=self.can.create_window(self.x36, self.y36,
          window=self.Data_write)

        self.x37, self.y37 = 271, 653
        self.b37=Button(self.can, width=8, font=16, bg='grey15', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink5)
        self.fb37=self.can.create_window(self.x37, self.y37, window=self.b37)

        self.x40, self.y40 = 429, 653
        self.b40=Button(self.can, width=18, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag5)
        self.fb40=self.can.create_window(self.x40, self.y40, window=self.b40)

        self.x41, self.y41 = 597, 653
        self.b41=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult5)
        self.fb41=self.can.create_window(self.x41, self.y41, window=self.b41)

        #patient6
        try:
            with open('./newpatient/entryfile6.txt', 'r') as namefile:
                line6=namefile.readline()
        except FileNotFoundError as callfile6:
            print("File entryfile6.txt doen't exist !", callfile6)

        self.new_data6=line6
        self.x45, self.y45 = 129, 685 #360
        self.Data_write=Entry(self.can)
        self.new_data6=StringVar()
        self.Data_write=Entry(textvariable=self.new_data6,
          highlightbackground='grey', bd=4)
        self.new_data6.set(line6)
        self.Data_write=self.can.create_window(self.x45, self.y45,
          window=self.Data_write)

        self.x46, self.y46 = 271, 685
        self.b46=Button(self.can, width=8, font=16, bg='grey12', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink6)
        self.fb46=self.can.create_window(self.x46, self.y46, window=self.b46)

        self.x49, self.y49 = 429, 685
        self.b49=Button(self.can, width=18, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag6)
        self.fb49=self.can.create_window(self.x49, self.y49, window=self.b49)

        self.x50, self.y50 = 597, 685
        self.b50=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult6)
        self.fb50=self.can.create_window(self.x50, self.y50, window=self.b50)
        
        #patient7
        try:
            with open('./newpatient/entryfile7.txt', 'r') as namefile:
                line7=namefile.readline()
        except FileNotFoundError as callfile7:
            print("File entryfile7.txt doen't exist !", callfile7)

        self.new_data7=line7
        self.x70, self.y70 = 129, 717 #392
        self.Data_write=Entry(self.can)
        self.new_data7=StringVar()
        self.Data_write=Entry(textvariable=self.new_data7,
          highlightbackground='grey', bd=4)
        self.new_data7.set(line7)
        self.Data_write=self.can.create_window(self.x70, self.y70,
          window=self.Data_write)

        self.x71, self.y71 = 271, 717
        self.b71=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink7)
        self.fb71=self.can.create_window(self.x71, self.y71, window=self.b71)

        self.x72, self.y72 = 429, 717
        self.b72=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag7)
        self.fb72=self.can.create_window(self.x72, self.y72, window=self.b72)

        self.x73, self.y73 = 597, 717
        self.b73=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult7)
        self.fb73=self.can.create_window(self.x73, self.y73, window=self.b73)

        #patient8 new patients added !!!
        try:
            with open('./newpatient/entryfile8.txt', 'r') as namefile:
                line8=namefile.readline()
        except FileNotFoundError as callfile8:
            print("File entryfile8.txt doen't exist !", callfile8)

        self.new_data8=line8
        self.x80, self.y80 = 129, 1042
        self.Data_write=Entry(self.can)
        self.new_data8=StringVar()
        self.Data_write=Entry(textvariable=self.new_data8,
          highlightbackground='grey', bd=4)
        self.new_data8.set(line8)
        self.Data_write=self.can.create_window(self.x80, self.y80,
          window=self.Data_write)

        self.x81, self.y81 = 271, 1042
        self.b81=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink8)
        self.fb81=self.can.create_window(self.x81, self.y81, window=self.b81)

        self.x82, self.y82 = 429, 1042
        self.b82=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag8)
        self.fb82=self.can.create_window(self.x82, self.y82, window=self.b82)

        self.x83, self.y83 = 597, 1042
        self.b83=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult8)
        self.fb83=self.can.create_window(self.x83, self.y83, window=self.b83)

        #patient9
        try:
            with open('./newpatient/entryfile9.txt', 'r') as namefile:
                line9=namefile.readline()
        except FileNotFoundError as callfile9:
            print("File entryfile9.txt doen't exist !", callfile9)

        self.new_data9=line9
        self.x90, self.y90 = 129, 1367
        self.Data_write=Entry(self.can)
        self.new_data9=StringVar()
        self.Data_write=Entry(textvariable=self.new_data9,
          highlightbackground='grey', bd=4)
        self.new_data9.set(line9)
        self.Data_write=self.can.create_window(self.x90, self.y90,
          window=self.Data_write)

        self.x91, self.y91 = 271, 1367
        self.b91=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink9)
        self.fb91=self.can.create_window(self.x91, self.y91, window=self.b91)

        self.x92, self.y92 = 429, 1367
        self.b92=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag9)
        self.fb92=self.can.create_window(self.x92, self.y92, window=self.b92)

        self.x93, self.y93 = 597, 1367
        self.b93=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult9)
        self.fb93=self.can.create_window(self.x93, self.y93, window=self.b93)

        #patient10
        try:
            with open('./newpatient/entryfile10.txt', 'r') as namefile:
                line10=namefile.readline()
        except FileNotFoundError as callfile10:
            print("File entryfile10.txt doen't exist !", callfile10)

        self.new_data10=line10
        self.x100, self.y100 = 129, 1692
        self.Data_write=Entry(self.can)
        self.new_data10=StringVar()
        self.Data_write=Entry(textvariable=self.new_data10,
          highlightbackground='grey', bd=4)
        self.new_data10.set(line10)
        self.Data_write=self.can.create_window(self.x100, self.y100,
          window=self.Data_write)

        self.x101, self.y101 = 271, 1692
        self.b101=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink10)
        self.fb101=self.can.create_window(self.x101, self.y101, window=self.b101)

        self.x102, self.y102 = 429, 1692
        self.b102=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag10)
        self.fb102=self.can.create_window(self.x102, self.y102, window=self.b102)

        self.x103, self.y103 = 597, 1692
        self.b103=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult10)
        self.fb103=self.can.create_window(self.x103, self.y103, window=self.b103)

        #patient11
        try:
            with open('./newpatient/entryfile11.txt', 'r') as namefile:
                line11=namefile.readline()
        except FileNotFoundError as callfile11:
            print("File entryfile11.txt doen't exist !", callfile11)

        self.new_data11=line11
        self.x110, self.y110 = 129, 2017 
        self.Data_write=Entry(self.can)
        self.new_data11=StringVar()
        self.Data_write=Entry(textvariable=self.new_data11,
          highlightbackground='grey', bd=4)
        self.new_data11.set(line11)
        self.Data_write=self.can.create_window(self.x110, self.y110,
          window=self.Data_write)

        self.x111, self.y111 = 271, 2017
        self.b111=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink11)
        self.fb111=self.can.create_window(self.x111, self.y111, window=self.b111)

        self.x112, self.y112 = 429, 2017
        self.b112=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag11)
        self.fb112=self.can.create_window(self.x112, self.y112, window=self.b112)

        self.x113, self.y113 = 597, 2017
        self.b113=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult11)
        self.fb113=self.can.create_window(self.x113, self.y113, window=self.b113)

        #patient12
        try:
            with open('./newpatient/entryfile12.txt', 'r') as namefile:
                line12=namefile.readline()
        except FileNotFoundError as callfile12:
            print("File entryfile12.txt doen't exist !", callfile12)

        self.new_data12=line12
        self.x120, self.y120 = 129, 2342
        self.Data_write=Entry(self.can)
        self.new_data12=StringVar()
        self.Data_write=Entry(textvariable=self.new_data12,
          highlightbackground='grey', bd=4)
        self.new_data12.set(line12)
        self.Data_write=self.can.create_window(self.x120, self.y120,
          window=self.Data_write)

        self.x121, self.y121 = 271, 2342
        self.b121=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink12)
        self.fb121=self.can.create_window(self.x121, self.y121, window=self.b121)

        self.x122, self.y122 = 429, 2342
        self.b122=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag12)
        self.fb122=self.can.create_window(self.x122, self.y122, window=self.b122)

        self.x123, self.y123 = 597, 2342
        self.b123=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult12)
        self.fb123=self.can.create_window(self.x123, self.y123, window=self.b123)

        #patient13
        try:
            with open('./newpatient/entryfile13.txt', 'r') as namefile:
                line13=namefile.readline()
        except FileNotFoundError as callfile13:
            print("File entryfile13.txt doen't exist !", callfile13)

        self.new_data13=line13
        self.x130, self.y130 = 129, 2667
        self.Data_write=Entry(self.can)
        self.new_data13=StringVar()
        self.Data_write=Entry(textvariable=self.new_data13,
          highlightbackground='grey', bd=4)
        self.new_data13.set(line13)
        self.Data_write=self.can.create_window(self.x130, self.y130,
          window=self.Data_write)

        self.x131, self.y131 = 271, 2667
        self.b131=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink13)
        self.fb131=self.can.create_window(self.x131, self.y131, window=self.b131)

        self.x132, self.y132 = 429, 2667
        self.b132=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag13)
        self.fb132=self.can.create_window(self.x132, self.y132, window=self.b132)

        self.x133, self.y133 = 597, 2667
        self.b133=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult13)
        self.fb133=self.can.create_window(self.x133, self.y133, window=self.b133)

        #patient14
        try:
            with open('./newpatient/entryfile14.txt', 'r') as namefile:
                line14=namefile.readline()
        except FileNotFoundError as callfile14:
            print("File entryfile14.txt doen't exist !", callfile14)

        self.new_data14=line14
        self.x140, self.y140 = 129, 2992 
        self.Data_write=Entry(self.can)
        self.new_data14=StringVar()
        self.Data_write=Entry(textvariable=self.new_data14,
          highlightbackground='grey', bd=4)
        self.new_data14.set(line14)
        self.Data_write=self.can.create_window(self.x140, self.y140,
          window=self.Data_write)

        self.x141, self.y141 = 271, 2992
        self.b141=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink14)
        self.fb141=self.can.create_window(self.x141, self.y141, window=self.b141)

        self.x142, self.y142 = 429, 2992
        self.b142=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag14)
        self.fb142=self.can.create_window(self.x142, self.y142, window=self.b142)

        self.x143, self.y143 = 597, 2992
        self.b143=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult14)
        self.fb143=self.can.create_window(self.x143, self.y143, window=self.b143)

        #patient15
        try:
            with open('./newpatient/entryfile15.txt', 'r') as namefile:
                line15=namefile.readline()
        except FileNotFoundError as callfile15:
            print("File entryfile15.txt doen't exist !", callfile15)

        self.new_data15=line15
        self.x150, self.y150 = 129, 3317
        self.Data_write=Entry(self.can)
        self.new_data15=StringVar()
        self.Data_write=Entry(textvariable=self.new_data15,
          highlightbackground='grey', bd=4)
        self.new_data15.set(line15)
        self.Data_write=self.can.create_window(self.x150, self.y150,
          window=self.Data_write)

        self.x151, self.y151 = 271, 3317
        self.b151=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink15)
        self.fb151=self.can.create_window(self.x151, self.y151, window=self.b151)

        self.x152, self.y152 = 429, 3317
        self.b152=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag15)
        self.fb152=self.can.create_window(self.x152, self.y152, window=self.b152)

        self.x153, self.y153 = 597, 3317
        self.b153=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult15)
        self.fb153=self.can.create_window(self.x153, self.y153, window=self.b153)

        #patient16
        try:
            with open('./newpatient/entryfile16.txt', 'r') as namefile:
                line16=namefile.readline()
        except FileNotFoundError as callfile16:
            print("File entryfile16.txt doen't exist !", callfile16)

        self.new_data16=line16
        self.x160, self.y160 = 129, 3642
        self.Data_write=Entry(self.can)
        self.new_data16=StringVar()
        self.Data_write=Entry(textvariable=self.new_data16,
          highlightbackground='grey', bd=4)
        self.new_data16.set(line16)
        self.Data_write=self.can.create_window(self.x160, self.y160,
          window=self.Data_write)

        self.x161, self.y161 = 271, 3642
        self.b161=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink16)
        self.fb161=self.can.create_window(self.x161, self.y161, window=self.b161)

        self.x162, self.y162 = 429, 3642
        self.b162=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag16)
        self.fb162=self.can.create_window(self.x162, self.y162, window=self.b162)

        self.x163, self.y163 = 597, 3642
        self.b163=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult16)
        self.fb163=self.can.create_window(self.x163, self.y163, window=self.b163)

        #patient17
        try:
            with open('./newpatient/entryfile17.txt', 'r') as namefile:
                line17=namefile.readline()
        except FileNotFoundError as callfile17:
            print("File entryfile17.txt doen't exist !", callfile17)

        self.new_data17=line17
        self.x170, self.y170 = 129, 3967
        self.Data_write=Entry(self.can)
        self.new_data17=StringVar()
        self.Data_write=Entry(textvariable=self.new_data17,
          highlightbackground='grey', bd=4)
        self.new_data17.set(line17)
        self.Data_write=self.can.create_window(self.x170, self.y170,
          window=self.Data_write)

        self.x171, self.y171 = 271, 3967
        self.b171=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink17)
        self.fb171=self.can.create_window(self.x171, self.y171, window=self.b171)

        self.x172, self.y172 = 429, 3967
        self.b172=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag17)
        self.fb172=self.can.create_window(self.x172, self.y172, window=self.b172)

        self.x173, self.y173 = 597, 3967
        self.b173=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult17)
        self.fb173=self.can.create_window(self.x173, self.y173, window=self.b173)

        #patient18
        try:
            with open('./newpatient/entryfile18.txt', 'r') as namefile:
                line18=namefile.readline()
        except FileNotFoundError as callfile18:
            print("File entryfile18.txt doen't exist !", callfile18)

        self.new_data18=line18
        self.x180, self.y180 = 129, 4292
        self.Data_write=Entry(self.can)
        self.new_data18=StringVar()
        self.Data_write=Entry(textvariable=self.new_data18,
          highlightbackground='grey', bd=4)
        self.new_data18.set(line18)
        self.Data_write=self.can.create_window(self.x180, self.y180,
          window=self.Data_write)

        self.x181, self.y181 = 271, 4292
        self.b181=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink18)
        self.fb181=self.can.create_window(self.x181, self.y181, window=self.b181)

        self.x182, self.y182 = 429, 4292
        self.b182=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag18)
        self.fb182=self.can.create_window(self.x182, self.y182, window=self.b182)

        self.x183, self.y183 = 597, 4292
        self.b183=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult18)
        self.fb183=self.can.create_window(self.x183, self.y183, window=self.b183)

        #patient19
        try:
            with open('./newpatient/entryfile19.txt', 'r') as namefile:
                line19=namefile.readline()
        except FileNotFoundError as callfile19:
            print("File entryfile19.txt doen't exist !", callfile19)

        self.new_data19=line19
        self.x190, self.y190 = 129, 4617
        self.Data_write=Entry(self.can)
        self.new_data19=StringVar()
        self.Data_write=Entry(textvariable=self.new_data19,
          highlightbackground='grey', bd=4)
        self.new_data19.set(line19)
        self.Data_write=self.can.create_window(self.x190, self.y190,
          window=self.Data_write)

        self.x191, self.y191 = 271, 4617
        self.b191=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink19)
        self.fb191=self.can.create_window(self.x191, self.y191, window=self.b191)

        self.x192, self.y192 = 429, 4617
        self.b192=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag19)
        self.fb192=self.can.create_window(self.x192, self.y192, window=self.b192)

        self.x193, self.y193 = 597, 4617
        self.b193=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult19)
        self.fb193=self.can.create_window(self.x193, self.y193, window=self.b193)

        #patient20
        try:
            with open('./newpatient/entryfile20.txt', 'r') as namefile:
                line20=namefile.readline()
        except FileNotFoundError as callfile20:
            print("File entryfile20.txt doen't exist !", callfile20)

        self.new_data20=line20
        self.x200, self.y200 = 129, 4942
        self.Data_write=Entry(self.can)
        self.new_data20=StringVar()
        self.Data_write=Entry(textvariable=self.new_data20,
          highlightbackground='grey', bd=4)
        self.new_data20.set(line20)
        self.Data_write=self.can.create_window(self.x200, self.y200,
          window=self.Data_write)

        self.x201, self.y201 = 271, 4942
        self.b201=Button(self.can, width=8, font=16, bg='black', fg='coral',
            activebackground='dark turquoise', text="Allergy",
            command=self.allergyLink20)
        self.fb201=self.can.create_window(self.x201, self.y201, window=self.b201)

        self.x202, self.y202 = 429, 4942
        self.b202=Button(self.can, width=18, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Diagnostic + ATCD",
            command=self.diag20)
        self.fb202=self.can.create_window(self.x202, self.y202, window=self.b202)

        self.x203, self.y203 = 597, 4942
        self.b203=Button(self.can, width=10, font=16, bg='black', fg='cyan',
            activebackground='dark turquoise', text="Laboratory",
            command=self.laboResult20)
        self.fb203=self.can.create_window(self.x203, self.y203, window=self.b203)

        # Display text in textbox from 14 Needs files
        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n--- Patient 1 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout:
            print("File 1 has not been found", infofileout)
        except IndexError as inforange:
            print("List 1 got less than 6 lines", inforange)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi2/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 2 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout1:
            print("File 2 has not been found", infofileout1)
        except IndexError as inforange2:
            print("List 2 got less than 6 lines", inforange2)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi3/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 3 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout3:
            print("File 3 has not been found", infofileout3)
        except IndexError as inforange3:
            print("List 3 got less than 6 lines", inforange3)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi4/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 4 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout4:
            print("File 4 has not been found", infofileout4)
        except IndexError as inforange4:
            print("List 4 got less than 6 lines", inforange4)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi5/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 5 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout5:
            print("File 5 has not been found", infofileout5)
        except IndexError as inforange5:
            print("List 5 got less than 6 lines", inforange5)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi6/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 6 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout6:
            print("File 6 has not been found", infofileout6)
        except IndexError as inforange6:
            print("List 6 got less than 6 lines", inforange6)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi7/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 7 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout7:
            print("File 7 has not been found", infofileout7)
        except IndexError as inforange7:
            print("List 7 got less than 6 lines", inforange7)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi8/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 8 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout8:
            print("File 8 has not been found", infofileout8)
        except IndexError as inforange8:
            print("List 8 got less than 6 lines", inforange8)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi9/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 9 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout9:
            print("File 9 has not been found", infofileout9)
        except IndexError as inforange9:
            print("List 9 got less than 6 lines", inforange9)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi10/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 10 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout10:
            print("File 10 has not been found", infofileout10)
        except IndexError as inforange10:
            print("List 10 got less than 6 lines", inforange10)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi11/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 11 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout11:
            print("File 11 has not been found", infofileout11)
        except IndexError as inforange11:
            print("List 11 got less than 6 lines", inforange11)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi12/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 12 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout12:
            print("File 12 has not been found", infofileout12)
        except IndexError as inforange12:
            print("List 12 got less than 6 lines", inforange12)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi13/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 13 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout13:
            print("File 13 has not been found", infofileout13)
        except IndexError as inforange13:
            print("List 13 got less than 6 lines", inforange13)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi14/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 14 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout14:
            print("File 14 has not been found", infofileout14)
        except IndexError as inforange14:
            print("List 14 got less than 6 lines", inforange14)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi15/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 15 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout15:
            print("File 15 has not been found", infofileout15)
        except IndexError as inforange15:
            print("List 15 got less than 6 lines", inforange15)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi16/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 16 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout16:
            print("File 16 has not been found", infofileout16)
        except IndexError as inforange16:
            print("List 16 got less than 6 lines", inforange16)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi17/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 17 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout17:
            print("File 17 has not been found", infofileout17)
        except IndexError as inforange17:
            print("List 17 got less than 6 lines", inforange17)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi18/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 18 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout18:
            print("File 18 has not been found", infofileout18)
        except IndexError as inforange18:
            print("List 18 got less than 6 lines", inforange18)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi19/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 19 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout19:
            print("File 19 has not been found", infofileout19)
        except IndexError as inforange19:
            print("List 19 got less than 6 lines", inforange19)
        else:
            ("Error unknow")

        try:
            datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./14besoins/doc_suivi20/main_14b.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if datesearch in line:
                        self.t63.insert(END, "\n\n--- Patient 20 ---\n")
                        self.t63.insert(INSERT, line)
                        self.t63.insert(INSERT, lines[i+1])
                        self.t63.insert(INSERT, lines[i+2])
                        self.t63.insert(INSERT, "...")
                    else:
                        pass
        except FileNotFoundError as infofileout20:
            print("File 20 has not been found", infofileout20)
        except IndexError as inforange20:
            print("List 20 got less than 6 lines", inforange20)
        else:
            ("Error unknow")

    def agendaDateSearch(self):
        """
        Display messagebox for agenda if an 
        appointment has been fixed for tomorrow:
        """
        print("Hello, let's see if appointment has been fixed for tomorrow...")
        time.sleep(1)
        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(lines[i])
                        print(lines[i+1])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA,there is an appointment for patient 1 tomorrow !')
                    else:
                        pass
        except FileNotFoundError as infofile1:
            print("File 1 has not been found", infofile1)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 2 tomorrow !')
                    else:
                        pass
        except FileNotFoundError as infofile2:
            print("File 2 has not been found", infofile2)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 3 tomorrow !')
                    else:
                        pass
        except FileNotFoundError as infofile3:
            print("File 3 has not been found", infofile3)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events4/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 4 tomorrow !')
                    else:
                        pass
        except FileNotFoundError as infofile4:
            print("File 4 has not been found", infofile4)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events5/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 5 tomorrow !')
                    else:
                        pass
        except FileNotFoundError as infofile5:
            print("File 5 has not been found", infofile5)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 6 tomorrow !')
                    else:
                        pass
        except FileNotFoundError as infofile6:
            print("File 6 has not been found", infofile6)
        else:
            ("Error unknow")

        try:
            dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
            with open('./patient_agenda/events7/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
                lines=filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if dateagenda in line:
                        print(line)
                        print(lines[i+1])
                        print(lines[i+2])
                        MSB2 = messagebox.showwarning('Info',
                            'Look at AGENDA, there is an appointment for patient 7 tomorrow !')
                    else:
                        pass
        except FileNotFoundError as infofile7:
            print("File 7 has not been found", infofile7)
        else:
            ("Error unknow")

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
        self.lab.title("INFO")
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
            "can ask me that to : philogenie@protonmail.com\n\n"
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

    # To launch psychotabs prog    
    def launchPsycho(self):
        subprocess.call('./psychotabs.py')

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

    def allergyLink8(self):
        subprocess.call('./allergy/allerpatient8.py')

    def allergyLink9(self):
        subprocess.call('./allergy/allerpatient9.py')

    def allergyLink10(self):
        subprocess.call('./allergy/allerpatient10.py')

    def allergyLink11(self):
        subprocess.call('./allergy/allerpatient11.py')

    def allergyLink12(self):
        subprocess.call('./allergy/allerpatient12.py')

    def allergyLink13(self):
        subprocess.call('./allergy/allerpatient13.py')

    def allergyLink14(self):
        subprocess.call('./allergy/allerpatient14.py')

    def allergyLink15(self):
        subprocess.call('./allergy/allerpatient15.py')

    def allergyLink16(self):
        subprocess.call('./allergy/allerpatient16.py')

    def allergyLink17(self):
        subprocess.call('./allergy/allerpatient17.py')

    def allergyLink18(self):
        subprocess.call('./allergy/allerpatient18.py')

    def allergyLink19(self):
        subprocess.call('./allergy/allerpatient19.py')

    def allergyLink20(self):
        subprocess.call('./allergy/allerpatient20.py')

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

    def patientAgenda8(self):
        subprocess.call('./patient_agenda/origin_agenda8.py')

    def patientAgenda9(self):
        subprocess.call('./patient_agenda/origin_agenda9.py')

    def patientAgenda10(self):
        subprocess.call('./patient_agenda/origin_agenda10.py')

    def patientAgenda11(self):
        subprocess.call('./patient_agenda/origin_agenda11.py')

    def patientAgenda12(self):
        subprocess.call('./patient_agenda/origin_agenda12.py')

    def patientAgenda13(self):
        subprocess.call('./patient_agenda/origin_agenda13.py')

    def patientAgenda14(self):
        subprocess.call('./patient_agenda/origin_agenda14.py')

    def patientAgenda15(self):
        subprocess.call('./patient_agenda/origin_agenda15.py')

    def patientAgenda16(self):
        subprocess.call('./patient_agenda/origin_agenda16.py')

    def patientAgenda17(self):
        subprocess.call('./patient_agenda/origin_agenda17.py')

    def patientAgenda18(self):
        subprocess.call('./patient_agenda/origin_agenda18.py')

    def patientAgenda19(self):
        subprocess.call('./patient_agenda/origin_agenda19.py')

    def patientAgenda20(self):
        subprocess.call('./patient_agenda/origin_agenda20.py')

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

    def besoins8Coche(self):
        subprocess.call('./14besoins/checkb8.py')

    def besoins9Coche(self):
        subprocess.call('./14besoins/checkb9.py')

    def besoins10Coche(self):
        subprocess.call('./14besoins/checkb10.py')

    def besoins11Coche(self):
        subprocess.call('./14besoins/checkb11.py')

    def besoins12Coche(self):
        subprocess.call('./14besoins/checkb12.py')

    def besoins13Coche(self):
        subprocess.call('./14besoins/checkb13.py')

    def besoins14Coche(self):
        subprocess.call('./14besoins/checkb14.py')

    def besoins15Coche(self):
        subprocess.call('./14besoins/checkb15.py')

    def besoins16Coche(self):
        subprocess.call('./14besoins/checkb16.py')

    def besoins17Coche(self):
        subprocess.call('./14besoins/checkb17.py')

    def besoins18Coche(self):
        subprocess.call('./14besoins/checkb18.py')

    def besoins19Coche(self):
        subprocess.call('./14besoins/checkb19.py')

    def besoins20Coche(self):
        subprocess.call('./14besoins/checkb20.py')

    # Call psychotabs
    def launchPsycho(self):
        subprocess.call('./psychotabs.py')

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

    def suiviSoins8(self):
        subprocess.call("./14besoins/suivi_patient_8.py")

    def suiviSoins9(self):
        subprocess.call("./14besoins/suivi_patient_9.py")

    def suiviSoins10(self):
        subprocess.call("./14besoins/suivi_patient_10.py")

    def suiviSoins11(self):
        subprocess.call("./14besoins/suivi_patient_11.py")

    def suiviSoins12(self):
        subprocess.call("./14besoins/suivi_patient_12.py")

    def suiviSoins13(self):
        subprocess.call("./14besoins/suivi_patient_13.py")

    def suiviSoins14(self):
        subprocess.call("./14besoins/suivi_patient_14.py")

    def suiviSoins15(self):
        subprocess.call("./14besoins/suivi_patient_15.py")

    def suiviSoins16(self):
        subprocess.call("./14besoins/suivi_patient_16.py")

    def suiviSoins17(self):
        subprocess.call("./14besoins/suivi_patient_17.py")

    def suiviSoins18(self):
        subprocess.call("./14besoins/suivi_patient_18.py")

    def suiviSoins19(self):
        subprocess.call("./14besoins/suivi_patient_19.py")

    def suiviSoins20(self):
        subprocess.call("./14besoins/suivi_patient_20.py")

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

    def tttMed8(self):
        subprocess.call("./ttt/patienttt8.py")

    def tttMed9(self):
        subprocess.call("./ttt/patienttt9.py")

    def tttMed10(self):
        subprocess.call("./ttt/patienttt10.py")

    def tttMed11(self):
        subprocess.call("./ttt/patienttt11.py")

    def tttMed12(self):
        subprocess.call("./ttt/patienttt12.py")

    def tttMed13(self):
        subprocess.call("./ttt/patienttt13.py")

    def tttMed14(self):
        subprocess.call("./ttt/patienttt14.py")

    def tttMed15(self):
        subprocess.call("./ttt/patienttt15.py")

    def tttMed16(self):
        subprocess.call("./ttt/patienttt16.py")

    def tttMed17(self):
        subprocess.call("./ttt/patienttt17.py")

    def tttMed18(self):
        subprocess.call("./ttt/patienttt18.py")

    def tttMed19(self):
        subprocess.call("./ttt/patienttt19.py")

    def tttMed20(self):
        subprocess.call("./ttt/patienttt20.py")

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

    def calculB8(self):
        subprocess.call("./calBmi/CalculBmi8.py")

    def calculB9(self):
        subprocess.call("./calBmi/CalculBmi9.py")

    def calculB10(self):
        subprocess.call("./calBmi/CalculBmi10.py")

    def calculB11(self):
        subprocess.call("./calBmi/CalculBmi11.py")

    def calculB12(self):
        subprocess.call("./calBmi/CalculBmi12.py")

    def calculB13(self):
        subprocess.call("./calBmi/CalculBmi13.py")

    def calculB14(self):
        subprocess.call("./calBmi/CalculBmi14.py")

    def calculB15(self):
        subprocess.call("./calBmi/CalculBmi15.py")

    def calculB16(self):
        subprocess.call("./calBmi/CalculBmi16.py")

    def calculB17(self):
        subprocess.call("./calBmi/CalculBmi17.py")

    def calculB18(self):
        subprocess.call("./calBmi/CalculBmi18.py")

    def calculB19(self):
        subprocess.call("./calBmi/CalculBmi19.py")

    def calculB20(self):
        subprocess.call("./calBmi/CalculBmi20.py")

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

    def laboResult8(self):
        subprocess.call('./labo/resultlabo8.py')

    def laboResult9(self):
        subprocess.call('./labo/resultlabo9.py')

    def laboResult10(self):
        subprocess.call('./labo/resultlabo10.py')

    def laboResult11(self):
        subprocess.call('./labo/resultlabo11.py')

    def laboResult12(self):
        subprocess.call('./labo/resultlabo12.py')

    def laboResult13(self):
        subprocess.call('./labo/resultlabo13.py')

    def laboResult14(self):
        subprocess.call('./labo/resultlabo14.py')

    def laboResult15(self):
        subprocess.call('./labo/resultlabo15.py')

    def laboResult16(self):
        subprocess.call('./labo/resultlabo16.py')

    def laboResult17(self):
        subprocess.call('./labo/resultlabo17.py')

    def laboResult18(self):
        subprocess.call('./labo/resultlabo18.py')

    def laboResult19(self):
        subprocess.call('./labo/resultlabo19.py')

    def laboResult20(self):
        subprocess.call('./labo/resultlabo20.py')

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

    def diag8(self):
        subprocess.call("./diag/diag_patient8.py")

    def diag9(self):
        subprocess.call("./diag/diag_patient9.py")

    def diag10(self):
        subprocess.call("./diag/diag_patient10.py")

    def diag11(self):
        subprocess.call("./diag/diag_patient11.py")

    def diag12(self):
        subprocess.call("./diag/diag_patient12.py")

    def diag13(self):
        subprocess.call("./diag/diag_patient13.py")

    def diag14(self):
        subprocess.call("./diag/diag_patient14.py")

    def diag15(self):
        subprocess.call("./diag/diag_patient15.py")

    def diag16(self):
        subprocess.call("./diag/diag_patient16.py")

    def diag17(self):
        subprocess.call("./diag/diag_patient17.py")

    def diag18(self):
        subprocess.call("./diag/diag_patient18.py")

    def diag19(self):
        subprocess.call("./diag/diag_patient19.py")

    def diag20(self):
        subprocess.call("./diag/diag_patient20.py")

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

    def newsTextBox(self):
        self.can.textBox = Text(app, text = "")

    def updateFiletxt(self):
        # To backup all files
        listeDate = ["01/08/2020", "01/09/2020", "01/10/2020", "01/11/2020",
        "01/12/2020", "01/01/2021", "01/02/2021", "01/03/2021", "01/04/2021",
        "01/05/2021", "01/06/2021", "01/07/2021", "01/08/2021", "01/09/2021", 
        "01/10/2021", "01/11/2021", "01/12/2021", "01/01/2022", "01/02/2022"]
        
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
