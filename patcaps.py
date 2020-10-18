#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import time
import datetime
from backapp import *
from agendapp import dispAgBox
from tttapp import dispTttBox
from resapp import dispResFunc


# Main page
def callResident(self):
    self.can.delete(ALL)
    self.can.configure(background='cyan')
    self.photo=PhotoImage(file='./syno_gif/title_tt.png')
    self.item=self.can.create_image(625, 85, image=self.photo)

    """
    # To backup (main file)
    self.updateFiletxt()
    dispAgBox()
    dispTttBox()
    dispResFunc()
    """

    # Display date
    self.x1, self.y1 = 1065, 70
    self.Date_write=Entry(self.can)
    self.data_time=StringVar()
    self.Date_write=Entry(self.can, textvariable=self.data_time, width=10,
        highlightbackground='grey', bd=4)
    self.data_time.set(time.strftime("%d/%m/%Y"))
    self.Date_write=self.can.create_window(self.x1, self.y1,
        window=self.Date_write)

    # Static time
    self.x2, self.y2 = 1165, 70
    self.Date_write2 = Entry(self.can)
    self.data_time2 = StringVar()
    self.Date_write2 = Entry(self.can, width=10, textvariable=self.data_time2,
        highlightbackground='grey', bd=4)
    self.data_time2.set(time.strftime("%H:%M:%S %p"))
    self.Date_write2=self.can.create_window(self.x2, self.y2,
        window=self.Date_write2)

    # To display time dynamically à revoir (new_file.py)
    # To introduce a new pytient
    self.x3, self.y3 = 200, 160
    self.b3=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='white', activebackground='dark turquoise',
        activeforeground='white', text="New Entry", command=self.callPatient1)
    self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)

    # To add one patient and files
    self.x4, self.y4 = 400, 160
    self.b4=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='cyan', activebackground='dark turquoise',
        activeforeground='white', text="Add patient", command=self.addPatientAfter)
    self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
    
    # To refresh canvas + menu bar
    self.x5, self.y5 = 600, 160
    self.b5=Button(self.can, width=10, font=16, bd=3, bg='RoyalBlue3',
        fg='SpringGreen2', highlightbackground='blue',
        activebackground='yellow', activeforeground='SpringGreen2',
        text="Refresh", command=self.upDateAll)
    self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)

    # To delete one patient and all files
    self.x6, self.y6 = 800, 160
    self.b6=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='coral', activebackground='red', 
        activeforeground='white', text="Delete patient", command=self.delEverPat)
    self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)

    # To go to resident page
    self.x6, self.y6 = 1000, 160
    self.b6=Button(self.can, width=10, font=16, bd=3, bg='RoyalBlue3', fg='white',
        highlightbackground='blue', activebackground='dark turquoise',
        activeforeground='white', text="TextBox page", command=self.showSynopsis)
    self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)

    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    self.data_time=line1
    self.x10, self.y10 = 129, 230
    self.Data_write=Entry(self.can)
    self.new_data1=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data1,
        highlightbackground='grey', bd=4)
    self.new_data1.set(line1)
    self.Data_write=self.can.create_window(self.x10, self.y10,
        window=self.Data_write)

    self.x11, self.y11 = 271, 230
    self.b11=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink)
    self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)

    self.x12, self.y12 = 429, 230
    self.b12=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag1)
    self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)

    self.x13, self.y13 = 597, 230
    self.b13=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed1)
    self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

    self.x14, self.y14 = 725, 230
    self.b14=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult)
    self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)

    self.x15, self.y15 = 853, 230
    self.b15=Button(self.can, width=10, font=15, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed)
    self.fb15=self.can.create_window(self.x15, self.y15, window=self.b15)

    self.x16, self.y16 = 981, 230
    self.b16=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu)
    self.fb16=self.can.create_window(self.x16, self.y16, window=self.b16)

    self.x17, self.y17 = 1109, 230
    self.b17=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB)
    self.fb17=self.can.create_window(self.x17, self.y17, window=self.b17)

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2=namefile.readline()
    except FileNotFoundError as callfile2:
        print("File entryfile2.txt doesn't exist !", callfile2)

    self.new_data2=line2
    self.x20, self.y20 = 129, 262
    self.Data_write=Entry(self.can)
    self.new_data2=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data2,
      highlightbackground='grey', bd=4)
    self.new_data2.set(line2)
    self.Data_write=self.can.create_window(self.x20, self.y20,
      window=self.Data_write)

    self.x21, self.y21 = 271, 262
    self.b21=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink2)
    self.fb21=self.can.create_window(self.x21, self.y21, window=self.b21)

    self.x22, self.y22 = 429, 262
    self.b22=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag2)
    self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)

    self.x23, self.y23 = 597, 262
    self.b23=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed2)
    self.fb23=self.can.create_window(self.x23, self.y23, window=self.b23)

    self.x24, self.y24 = 725, 262
    self.b24=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult2)
    self.fb24=self.can.create_window(self.x24, self.y24, window=self.b24)

    self.x25, self.y25 = 853, 262
    self.b25=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed2)
    self.fb25=self.can.create_window(self.x25, self.y25, window=self.b25)

    self.x26, self.y26 = 981, 262
    self.b26=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu2)
    self.fb26=self.can.create_window(self.x26, self.y26, window=self.b26)

    self.x27, self.y27 = 1109, 262
    self.b27=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB2)
    self.fb27=self.can.create_window(self.x27, self.y27, window=self.b27)

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3=namefile.readline()
    except FileNotFoundError as callfile3:
        print("File entryfile3.txt doesn't exist !", callfile3)

    self.new_data3=line3
    self.x30, self.y30 = 129, 294
    self.Data_write=Entry(self.can)
    self.new_data3=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data3,
      highlightbackground='grey', bd=4)
    self.new_data3.set(line3)
    self.Data_write=self.can.create_window(self.x30, self.y30,
      window=self.Data_write)

    self.x31, self.y31 = 271, 294
    self.b31=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink3)
    self.fb31=self.can.create_window(self.x31, self.y31, window=self.b31)

    self.x32, self.y32 = 429, 294
    self.b32=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag3)
    self.fb32=self.can.create_window(self.x32, self.y32, window=self.b32)

    self.x33, self.y33 = 597, 294
    self.b33=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed3)
    self.fb33=self.can.create_window(self.x33, self.y33, window=self.b33)

    self.x34, self.y34 = 725, 294
    self.b34=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult3)
    self.fb34=self.can.create_window(self.x34, self.y34, window=self.b34)

    self.x35, self.y35 = 853, 294
    self.b35=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed3)
    self.fb35=self.can.create_window(self.x35, self.y35, window=self.b35)

    self.x36, self.y36 = 981, 294
    self.b36=Button(self.can, width=10, font=36, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu3)
    self.fb36=self.can.create_window(self.x36, self.y36, window=self.b36)

    self.x37, self.y37 = 1109, 294
    self.b37=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB3)
    self.fb37=self.can.create_window(self.x37, self.y37, window=self.b37)

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4=namefile.readline()
    except FileNotFoundError as callfile4:
        print("File entryfile4.txt doesn't exist !", callfile4)

    self.new_data4=line4
    self.x40, self.y40 = 129, 326
    self.Data_write=Entry(self.can)
    self.new_data4=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data4,
      highlightbackground='grey', bd=4)
    self.new_data4.set(line4)
    self.Data_write=self.can.create_window(self.x40, self.y40,
      window=self.Data_write)

    self.x41, self.y41 = 271, 326
    self.b41=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink4)
    self.fb41=self.can.create_window(self.x41, self.y41, window=self.b41)

    self.x42, self.y42 = 429, 326
    self.b42=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag4)
    self.fb42=self.can.create_window(self.x42, self.y42, window=self.b42)

    self.x43, self.y43 = 597, 326
    self.b43=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed4)
    self.fb43=self.can.create_window(self.x43, self.y43, window=self.b43)

    self.x44, self.y44 = 725, 326
    self.b44=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult4)
    self.fb44=self.can.create_window(self.x44, self.y44, window=self.b44)

    self.x45, self.y45 = 853, 326
    self.b45=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed4)
    self.fb45=self.can.create_window(self.x45, self.y45, window=self.b45)

    self.x46, self.y46 = 981, 326
    self.b46=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu4)
    self.fb46=self.can.create_window(self.x46, self.y46, window=self.b46)

    self.x47, self.y47 = 1109, 326
    self.b47=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB4)
    self.fb47=self.can.create_window(self.x47, self.y47, window=self.b47)

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5=namefile.readline()
    except FileNotFoundError as callfile5:
        print("File entryfile5.txt doesn't exist !", callfile5)

    self.new_data5=line5
    self.x50, self.y50 = 129, 358
    self.Data_write=Entry(self.can)
    self.new_data5=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data5,
      highlightbackground='grey', bd=4)
    self.new_data5.set(line5)
    self.Data_write=self.can.create_window(self.x50, self.y50,
      window=self.Data_write)

    self.x51, self.y51 = 271, 358
    self.b51=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink5)
    self.fb51=self.can.create_window(self.x51, self.y51, window=self.b51)

    self.x52, self.y52 = 429, 358
    self.b52=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag5)
    self.fb52=self.can.create_window(self.x52, self.y52, window=self.b52)

    self.x53, self.y53 = 597, 358
    self.b53=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed5)
    self.fb53=self.can.create_window(self.x53, self.y53, window=self.b53)

    self.x54, self.y54 = 725, 358
    self.b54=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult5)
    self.fb54=self.can.create_window(self.x54, self.y54, window=self.b54)

    self.x55, self.y55 = 853, 358
    self.b55=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed5)
    self.fb55=self.can.create_window(self.x55, self.y55, window=self.b55)

    self.x56, self.y56 = 981, 358
    self.b56=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu5)
    self.fb56=self.can.create_window(self.x56, self.y56, window=self.b56)

    self.x57, self.y57 = 1109, 358
    self.b57=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB5)
    self.fb57=self.can.create_window(self.x57, self.y57, window=self.b57)

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6=namefile.readline()
    except FileNotFoundError as callfile6:
        print("File entryfile6.txt doesn't exist !", callfile6)

    self.new_data6=line6
    self.x60, self.y60 = 129, 390
    self.Data_write=Entry(self.can)
    self.new_data6=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data6,
      highlightbackground='grey', bd=4)
    self.new_data6.set(line6)
    self.Data_write=self.can.create_window(self.x60, self.y60,
      window=self.Data_write)

    self.x61, self.y61 = 271, 390
    self.b61=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink6)
    self.fb61=self.can.create_window(self.x61, self.y61, window=self.b61)

    self.x62, self.y62 = 429, 390
    self.b62=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag6)
    self.fb62=self.can.create_window(self.x62, self.y62, window=self.b62)

    self.x64, self.y64 = 597, 390
    self.b64=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed6)
    self.fb64=self.can.create_window(self.x64, self.y64, window=self.b64)

    self.x65, self.y65 = 725, 390
    self.b65=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult6)
    self.fb65=self.can.create_window(self.x65, self.y65, window=self.b65)

    self.x66, self.y66 = 853, 390
    self.b66=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed6)
    self.fb66=self.can.create_window(self.x66, self.y66, window=self.b66)

    self.x67, self.y67 = 981, 390
    self.b67=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu6)
    self.fb67=self.can.create_window(self.x67, self.y67, window=self.b67)

    self.x68, self.y68 = 1109, 390
    self.b68=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB6)
    self.fb68=self.can.create_window(self.x68, self.y68, window=self.b68)

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7=namefile.readline()
    except FileNotFoundError as callfile7:
        print("File entryfile7.txt doesn't exist !", callfile7)

    self.new_data7=line7
    self.x70, self.y70 = 129, 422
    self.Data_write=Entry(self.can)
    self.new_data7=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data7,
      highlightbackground='grey', bd=4)
    self.new_data7.set(line7)
    self.Data_write=self.can.create_window(self.x70, self.y70,
      window=self.Data_write)

    self.x71, self.y71 = 271, 422
    self.b71=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink7)
    self.fb71=self.can.create_window(self.x71, self.y71, window=self.b71)

    self.x72, self.y72 = 429, 422
    self.b72=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag7)
    self.fb72=self.can.create_window(self.x72, self.y72, window=self.b72)

    self.x73, self.y73 = 597, 422
    self.b73=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed7)
    self.fb73=self.can.create_window(self.x73, self.y73, window=self.b73)

    self.x74, self.y74 = 725, 422
    self.b74=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult7)
    self.fb74=self.can.create_window(self.x74, self.y74, window=self.b74)

    self.x75, self.y75 = 853, 422
    self.b75=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed7)
    self.fb75=self.can.create_window(self.x75, self.y75, window=self.b75)

    self.x76, self.y76 = 981, 422
    self.b76=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu7)
    self.fb76=self.can.create_window(self.x76, self.y76, window=self.b76)

    self.x77, self.y77 = 1109, 422
    self.b77=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB7)
    self.fb77=self.can.create_window(self.x77, self.y77, window=self.b77)

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8=namefile.readline()
    except FileNotFoundError as callfile8:
        print("File entryfile8.txt doesn't exist !", callfile8)

    self.new_data8=line8
    self.x80, self.y80 = 129, 454
    self.Data_write=Entry(self.can)
    self.new_data8=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data8,
      highlightbackground='grey', bd=4)
    self.new_data8.set(line8)
    self.Data_write=self.can.create_window(self.x80, self.y80,
      window=self.Data_write)

    self.x81, self.y81 = 271, 454
    self.b81=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink8)
    self.fb81=self.can.create_window(self.x81, self.y81, window=self.b81)

    self.x82, self.y82 = 429, 454
    self.b82=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag8)
    self.fb82=self.can.create_window(self.x82, self.y82, window=self.b82)

    self.x83, self.y83 = 597, 454
    self.b83=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed8)
    self.fb83=self.can.create_window(self.x83, self.y83, window=self.b83)

    self.x84, self.y84 = 725, 454
    self.b84=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult8)
    self.fb84=self.can.create_window(self.x84, self.y84, window=self.b84)

    self.x85, self.y85 = 853, 454
    self.b85=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed8)
    self.fb85=self.can.create_window(self.x85, self.y85, window=self.b85)

    self.x86, self.y86 = 981, 454
    self.b86=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu8)
    self.fb86=self.can.create_window(self.x86, self.y86, window=self.b86)

    self.x87, self.y87 = 1109, 454
    self.b87=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB8)
    self.fb87=self.can.create_window(self.x87, self.y87, window=self.b87)

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9=namefile.readline()
    except FileNotFoundError as callfile9:
        print("File entryfile9.txt doesn't exist !", callfile9)

    self.new_data9=line9
    self.x90, self.y90 = 129, 486
    self.Data_write=Entry(self.can)
    self.new_data9=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data9,
      highlightbackground='grey', bd=4)
    self.new_data9.set(line9)
    self.Data_write=self.can.create_window(self.x90, self.y90,
      window=self.Data_write)

    self.x91, self.y91 = 271, 486
    self.b91=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink9)
    self.fb91=self.can.create_window(self.x91, self.y91, window=self.b91)

    self.x92, self.y92 = 429, 486
    self.b92=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag9)
    self.fb92=self.can.create_window(self.x92, self.y92, window=self.b92)

    self.x93, self.y93 = 597, 486
    self.b93=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed9)
    self.fb93=self.can.create_window(self.x93, self.y93, window=self.b93)

    self.x94, self.y94 = 725, 486
    self.b94=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult9)
    self.fb94=self.can.create_window(self.x94, self.y94, window=self.b94)

    self.x95, self.y95 = 853, 486
    self.b95=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed9)
    self.fb95=self.can.create_window(self.x95, self.y95, window=self.b95)

    self.x96, self.y96 = 981, 486
    self.b96=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu9)
    self.fb96=self.can.create_window(self.x96, self.y96, window=self.b96)

    self.x97, self.y97 = 1109, 486
    self.b97=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB9)
    self.fb97=self.can.create_window(self.x97, self.y97, window=self.b97)

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10=namefile.readline()
    except FileNotFoundError as callfile10:
        print("File entryfile10.txt doesn't exist !", callfile10)

    self.new_data10=line10
    self.x100, self.y100 = 129, 518
    self.Data_write=Entry(self.can)
    self.new_data10=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data10,
      highlightbackground='grey', bd=4)
    self.new_data10.set(line10)
    self.Data_write=self.can.create_window(self.x100, self.y100,
      window=self.Data_write)

    self.x101, self.y101 = 271, 518
    self.b101=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb101=self.can.create_window(self.x101, self.y101, window=self.b101)

    self.x102, self.y102 = 429, 518
    self.b102=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb102=self.can.create_window(self.x102, self.y102, window=self.b102)

    self.x103, self.y103 = 597, 518
    self.b103=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed10)
    self.fb103=self.can.create_window(self.x103, self.y103, window=self.b103)

    self.x104, self.y104 = 725, 518
    self.b104=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb104=self.can.create_window(self.x104, self.y104, window=self.b104)

    self.x105, self.y105 = 853, 518
    self.b105=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed10)
    self.fb105=self.can.create_window(self.x105, self.y105, window=self.b105)

    self.x106, self.y106 = 981, 518
    self.b106=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu10)
    self.fb106=self.can.create_window(self.x106, self.y106, window=self.b106)

    self.x107, self.y107 = 1109, 518
    self.b107=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB10)
    self.fb107=self.can.create_window(self.x107, self.y107, window=self.b107)

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11=namefile.readline()
    except FileNotFoundError as callfile11:
        print("File entryfile11.txt doesn't exist !", callfile11)

    self.new_data11=line11
    self.x110, self.y110 = 129, 550
    self.Data_write=Entry(self.can)
    self.new_data11=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data11,
      highlightbackground='grey', bd=4)
    self.new_data11.set(line11)
    self.Data_write=self.can.create_window(self.x110, self.y110,
      window=self.Data_write)

    self.x111, self.y111 = 271, 550
    self.b111=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink11)
    self.fb111=self.can.create_window(self.x111, self.y111, window=self.b111)

    self.x112, self.y112 = 429, 550
    self.b112=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag11)
    self.fb112=self.can.create_window(self.x112, self.y112, window=self.b112)

    self.x113, self.y113 = 597, 550
    self.b113=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed11)
    self.fb113=self.can.create_window(self.x113, self.y113, window=self.b113)

    self.x114, self.y114 = 725, 550
    self.b114=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult11)
    self.fb114=self.can.create_window(self.x114, self.y114, window=self.b114)

    self.x115, self.y115 = 853, 550
    self.b115=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed11)
    self.fb115=self.can.create_window(self.x115, self.y115, window=self.b115)

    self.x116, self.y116 = 981, 550
    self.b116=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu11)
    self.fb116=self.can.create_window(self.x116, self.y116, window=self.b116)

    self.x117, self.y117 = 1109, 550
    self.b117=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB11)
    self.fb117=self.can.create_window(self.x117, self.y117, window=self.b117)

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12=namefile.readline()
    except FileNotFoundError as callfile12:
        print("File entryfile12.txt doesn't exist !", callfile12)

    self.new_data12=line12
    self.x120, self.y120 = 129, 582
    self.Data_write=Entry(self.can)
    self.new_data12=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data12,
      highlightbackground='grey', bd=4)
    self.new_data12.set(line12)
    self.Data_write=self.can.create_window(self.x120, self.y120,
      window=self.Data_write)

    self.x121, self.y121 = 271, 582
    self.b121=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink12)
    self.fb121=self.can.create_window(self.x121, self.y121, window=self.b121)

    self.x122, self.y122 = 429, 582
    self.b122=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag12)
    self.fb122=self.can.create_window(self.x122, self.y122, window=self.b122)

    self.x123, self.y123 = 597, 582
    self.b123=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed12)
    self.fb123=self.can.create_window(self.x123, self.y123, window=self.b123)

    self.x124, self.y124 = 725, 582
    self.b124=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult12)
    self.fb124=self.can.create_window(self.x124, self.y124, window=self.b124)

    self.x125, self.y125 = 853, 582
    self.b125=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed12)
    self.fb125=self.can.create_window(self.x125, self.y125, window=self.b125)

    self.x126, self.y126 = 981, 582
    self.b126=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu12)
    self.fb126=self.can.create_window(self.x126, self.y126, window=self.b126)

    self.x127, self.y127 = 1109, 582
    self.b127=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB12)
    self.fb127=self.can.create_window(self.x127, self.y127, window=self.b127)

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13=namefile.readline()
    except FileNotFoundError as callfile13:
        print("File entryfile13.txt doesn't exist !", callfile13)

    self.new_data13=line13
    self.x130, self.y130 = 129, 614
    self.Data_write=Entry(self.can)
    self.new_data13=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data13,
      highlightbackground='grey', bd=4)
    self.new_data13.set(line13)
    self.Data_write=self.can.create_window(self.x130, self.y130,
      window=self.Data_write)

    self.x131, self.y131 = 271, 614
    self.b131=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink13)
    self.fb131=self.can.create_window(self.x131, self.y131, window=self.b131)

    self.x132, self.y132 = 429, 614
    self.b132=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag13)
    self.fb132=self.can.create_window(self.x132, self.y132, window=self.b132)

    self.x133, self.y133 = 597, 614
    self.b133=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed13)
    self.fb133=self.can.create_window(self.x133, self.y133, window=self.b133)

    self.x134, self.y134 = 725, 614
    self.b134=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult13)
    self.fb134=self.can.create_window(self.x134, self.y134, window=self.b134)

    self.x135, self.y135 = 853, 614
    self.b135=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed13)
    self.fb135=self.can.create_window(self.x135, self.y135, window=self.b135)

    self.x136, self.y136 = 981, 614
    self.b136=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu13)
    self.fb136=self.can.create_window(self.x136, self.y136, window=self.b136)

    self.x137, self.y137 = 1109, 614
    self.b137=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB13)
    self.fb137=self.can.create_window(self.x137, self.y137, window=self.b137)

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14=namefile.readline()
    except FileNotFoundError as callfile14:
        print("File entryfile14.txt doesn't exist !", callfile14)

    self.new_data14=line14
    self.x140, self.y140 = 129, 646
    self.Data_write=Entry(self.can)
    self.new_data14=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data14,
      highlightbackground='grey', bd=4)
    self.new_data14.set(line14)
    self.Data_write=self.can.create_window(self.x140, self.y140,
      window=self.Data_write)

    self.x141, self.y141 = 271, 646
    self.b141=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink14)
    self.fb141=self.can.create_window(self.x141, self.y141, window=self.b141)

    self.x142, self.y142 = 429, 646
    self.b142=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag14)
    self.fb142=self.can.create_window(self.x142, self.y142, window=self.b142)

    self.x143, self.y143 = 597, 646
    self.b143=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed14)
    self.fb143=self.can.create_window(self.x143, self.y143, window=self.b143)

    self.x144, self.y144 = 725, 646
    self.b144=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult14)
    self.fb144=self.can.create_window(self.x144, self.y144, window=self.b144)

    self.x145, self.y145 = 853, 646
    self.b145=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed14)
    self.fb145=self.can.create_window(self.x145, self.y145, window=self.b145)

    self.x146, self.y146 = 981, 646
    self.b146=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu14)
    self.fb146=self.can.create_window(self.x146, self.y146, window=self.b146)

    self.x147, self.y147 = 1109, 646
    self.b147=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB14)
    self.fb147=self.can.create_window(self.x147, self.y147, window=self.b147)

    # Patient 15
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15=namefile.readline()
    except FileNotFoundError as callfile15:
        print("File entryfile15.txt doesn't exist !", callfile15)

    self.new_data15=line15
    self.x150, self.y150 = 129, 678
    self.Data_write=Entry(self.can)
    self.new_data15=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data15,
      highlightbackground='grey', bd=4)
    self.new_data15.set(line15)
    self.Data_write=self.can.create_window(self.x150, self.y150,
      window=self.Data_write)

    self.x151, self.y151 = 271, 678
    self.b151=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink15)
    self.fb151=self.can.create_window(self.x151, self.y151, window=self.b151)

    self.x152, self.y152 = 429, 678
    self.b152=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag15)
    self.fb152=self.can.create_window(self.x152, self.y152, window=self.b152)

    self.x153, self.y153 = 597, 678
    self.b153=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed15)
    self.fb153=self.can.create_window(self.x153, self.y153, window=self.b153)

    self.x154, self.y154 = 725, 678
    self.b154=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult15)
    self.fb154=self.can.create_window(self.x154, self.y154, window=self.b154)

    self.x155, self.y155 = 853, 678
    self.b155=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed15)
    self.fb155=self.can.create_window(self.x155, self.y155, window=self.b155)

    self.x156, self.y156 = 981, 678
    self.b156=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu15)
    self.fb156=self.can.create_window(self.x156, self.y156, window=self.b156)

    self.x157, self.y157 = 1109, 678
    self.b157=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB15)
    self.fb157=self.can.create_window(self.x157, self.y157, window=self.b157)

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16=namefile.readline()
    except FileNotFoundError as callfile16:
        print("File entryfile16.txt doesn't exist !", callfile16)

    self.new_data16=line16
    self.x160, self.y160 = 129, 710
    self.Data_write=Entry(self.can)
    self.new_data16=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data16,
      highlightbackground='grey', bd=4)
    self.new_data16.set(line16)
    self.Data_write=self.can.create_window(self.x160, self.y160,
      window=self.Data_write)

    self.x161, self.y161 = 271, 710
    self.b161=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink16)
    self.fb161=self.can.create_window(self.x161, self.y161, window=self.b161)

    self.x162, self.y162 = 429, 710
    self.b162=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag16)
    self.fb162=self.can.create_window(self.x162, self.y162, window=self.b162)

    self.x163, self.y163 = 597, 710
    self.b163=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed16)
    self.fb163=self.can.create_window(self.x163, self.y163, window=self.b163)

    self.x164, self.y164 = 725, 710
    self.b164=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult16)
    self.fb164=self.can.create_window(self.x164, self.y164, window=self.b164)

    self.x165, self.y165 = 853, 710
    self.b165=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed16)
    self.fb165=self.can.create_window(self.x165, self.y165, window=self.b165)

    self.x166, self.y166 = 981, 710
    self.b166=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu16)
    self.fb166=self.can.create_window(self.x166, self.y166, window=self.b166)

    self.x167, self.y167 = 1109, 710
    self.b167=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB16)
    self.fb167=self.can.create_window(self.x167, self.y167, window=self.b167)

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17=namefile.readline()
    except FileNotFoundError as callfile17:
        print("File entryfile17.txt doesn't exist !", callfile17)

    self.new_data17=line17
    self.x170, self.y170 = 129, 742
    self.Data_write=Entry(self.can)
    self.new_data17=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data17,
      highlightbackground='grey', bd=4)
    self.new_data17.set(line17)
    self.Data_write=self.can.create_window(self.x170, self.y170,
      window=self.Data_write)

    self.x171, self.y171 = 271, 742
    self.b171=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink17)
    self.fb171=self.can.create_window(self.x171, self.y171, window=self.b171)

    self.x172, self.y172 = 429, 742
    self.b172=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag17)
    self.fb172=self.can.create_window(self.x172, self.y172, window=self.b172)

    self.x173, self.y173 = 597, 742
    self.b173=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed17)
    self.fb173=self.can.create_window(self.x173, self.y173, window=self.b173)

    self.x174, self.y174 = 725, 742
    self.b174=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult17)
    self.fb174=self.can.create_window(self.x174, self.y174, window=self.b174)

    self.x175, self.y175 = 853, 742
    self.b175=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed17)
    self.fb175=self.can.create_window(self.x175, self.y175, window=self.b175)

    self.x176, self.y176 = 981, 742
    self.b176=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu17)
    self.fb176=self.can.create_window(self.x176, self.y176, window=self.b176)

    self.x177, self.y177 = 1109, 742
    self.b177=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB17)
    self.fb177=self.can.create_window(self.x177, self.y177, window=self.b177)

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18=namefile.readline()
    except FileNotFoundError as callfile18:
        print("File entryfile18.txt doesn't exist !", callfile18)

    self.new_data18=line18
    self.x180, self.y180 = 129, 774
    self.Data_write=Entry(self.can)
    self.new_data18=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data18,
      highlightbackground='grey', bd=4)
    self.new_data18.set(line18)
    self.Data_write=self.can.create_window(self.x180, self.y180,
      window=self.Data_write)

    self.x181, self.y181 = 271, 774
    self.b181=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink18)
    self.fb181=self.can.create_window(self.x181, self.y181, window=self.b181)

    self.x182, self.y182 = 429, 774
    self.b182=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag18)
    self.fb182=self.can.create_window(self.x182, self.y182, window=self.b182)

    self.x183, self.y183 = 597, 774
    self.b183=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed18)
    self.fb183=self.can.create_window(self.x183, self.y183, window=self.b183)

    self.x184, self.y184 = 725, 774
    self.b184=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult18)
    self.fb184=self.can.create_window(self.x184, self.y184, window=self.b184)

    self.x185, self.y185 = 853, 774
    self.b185=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed18)
    self.fb185=self.can.create_window(self.x185, self.y185, window=self.b185)

    self.x186, self.y186 = 981, 774
    self.b186=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu18)
    self.fb186=self.can.create_window(self.x186, self.y186, window=self.b186)

    self.x187, self.y187 = 1109, 774
    self.b187=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB18)
    self.fb187=self.can.create_window(self.x187, self.y187, window=self.b187)

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19=namefile.readline()
    except FileNotFoundError as callfile19:
        print("File entryfile19.txt doesn't exist !", callfile19)

    self.new_data19=line19
    self.x190, self.y190 = 129, 806
    self.Data_write=Entry(self.can)
    self.new_data19=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data19,
      highlightbackground='grey', bd=4)
    self.new_data19.set(line19)
    self.Data_write=self.can.create_window(self.x190, self.y190,
      window=self.Data_write)

    self.x191, self.y191 = 271, 806
    self.b191=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink19)
    self.fb191=self.can.create_window(self.x191, self.y191, window=self.b191)

    self.x192, self.y192 = 429, 806
    self.b192=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag19)
    self.fb192=self.can.create_window(self.x192, self.y192, window=self.b192)

    self.x193, self.y193 = 597, 806
    self.b193=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed19)
    self.fb193=self.can.create_window(self.x193, self.y193, window=self.b193)

    self.x194, self.y194 = 725, 806
    self.b194=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult19)
    self.fb194=self.can.create_window(self.x194, self.y194, window=self.b194)

    self.x195, self.y195 = 853, 806
    self.b195=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed19)
    self.fb195=self.can.create_window(self.x195, self.y195, window=self.b195)

    self.x196, self.y196 = 981, 806
    self.b196=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu19)
    self.fb196=self.can.create_window(self.x196, self.y196, window=self.b196)

    self.x197, self.y197 = 1109, 806
    self.b197=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB19)
    self.fb197=self.can.create_window(self.x197, self.y197, window=self.b197)

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20=namefile.readline()
    except FileNotFoundError as callfile20:
        print("File entryfile20.txt doesn't exist !", callfile20)

    self.new_data20=line20
    self.x200, self.y200 = 129, 838
    self.Data_write=Entry(self.can)
    self.new_data20=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data20,
      highlightbackground='grey', bd=4)
    self.new_data20.set(line20)
    self.Data_write=self.can.create_window(self.x200, self.y200,
      window=self.Data_write)

    self.x201, self.y201 = 271, 838
    self.b201=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink20)
    self.fb201=self.can.create_window(self.x201, self.y201, window=self.b201)

    self.x202, self.y202 = 429, 838
    self.b202=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag20)
    self.fb202=self.can.create_window(self.x202, self.y202, window=self.b202)

    self.x203, self.y203 = 597, 838
    self.b203=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed20)
    self.fb203=self.can.create_window(self.x203, self.y203, window=self.b203)

    self.x204, self.y204 = 725, 838
    self.b204=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult20)
    self.fb204=self.can.create_window(self.x204, self.y204, window=self.b204)

    self.x205, self.y205 = 853, 838
    self.b205=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed20)
    self.fb205=self.can.create_window(self.x205, self.y205, window=self.b205)

    self.x206, self.y206 = 981, 838
    self.b206=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu20)
    self.fb206=self.can.create_window(self.x206, self.y206, window=self.b206)

    self.x207, self.y207 = 1109, 838
    self.b207=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB20)
    self.fb207=self.can.create_window(self.x207, self.y207, window=self.b207)

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21=namefile.readline()
    except FileNotFoundError as callfile21:
        print("File entryfile21.txt doesn't exist !", callfile21)

    self.new_data21=line21
    self.x210, self.y210 = 129, 870
    self.Data_write=Entry(self.can)
    self.new_data21=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data21,
      highlightbackground='grey', bd=4)
    self.new_data21.set(line21)
    self.Data_write=self.can.create_window(self.x210, self.y210,
      window=self.Data_write)

    self.x211, self.y211 = 271, 870
    self.b211=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink21)
    self.fb211=self.can.create_window(self.x211, self.y211, window=self.b211)

    self.x212, self.y212 = 429, 870
    self.b212=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag21)
    self.fb212=self.can.create_window(self.x212, self.y212, window=self.b212)

    self.x213, self.y213 = 597, 870
    self.b213=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed21)
    self.fb213=self.can.create_window(self.x213, self.y213, window=self.b213)

    self.x214, self.y214 = 725, 870
    self.b214=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult21)
    self.fb214=self.can.create_window(self.x214, self.y214, window=self.b214)

    self.x215, self.y215 = 853, 870
    self.b215=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed21)
    self.fb215=self.can.create_window(self.x215, self.y215, window=self.b215)

    self.x216, self.y216 = 981, 870
    self.b216=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu21)
    self.fb216=self.can.create_window(self.x216, self.y216, window=self.b216)

    self.x217, self.y217 = 1109, 870
    self.b217=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB21)
    self.fb217=self.can.create_window(self.x217, self.y217, window=self.b217)

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22=namefile.readline()
    except FileNotFoundError as callfile22:
        print("File entryfile22.txt doesn't exist !", callfile22)

    self.new_data22=line22
    self.x220, self.y220 = 129, 902
    self.Data_write=Entry(self.can)
    self.new_data22=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data22,
      highlightbackground='grey', bd=4)
    self.new_data22.set(line22)
    self.Data_write=self.can.create_window(self.x220, self.y220,
      window=self.Data_write)

    self.x221, self.y221 = 271, 902
    self.b221=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink22)
    self.fb221=self.can.create_window(self.x221, self.y221, window=self.b221)

    self.x222, self.y222 = 429, 902
    self.b222=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag22)
    self.fb222=self.can.create_window(self.x222, self.y222, window=self.b222)

    self.x223, self.y223 = 597, 902
    self.b223=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed22)
    self.fb223=self.can.create_window(self.x223, self.y223, window=self.b223)

    self.x224, self.y224 = 725, 902
    self.b224=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult22)
    self.fb224=self.can.create_window(self.x224, self.y224, window=self.b224)

    self.x225, self.y225 = 853, 902
    self.b225=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed22)
    self.fb225=self.can.create_window(self.x225, self.y225, window=self.b225)

    self.x226, self.y226 = 981, 902
    self.b226=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu22)
    self.fb226=self.can.create_window(self.x226, self.y226, window=self.b226)

    self.x227, self.y227 = 1109, 902
    self.b227=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB22)
    self.fb227=self.can.create_window(self.x227, self.y227, window=self.b227)

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23=namefile.readline()
    except FileNotFoundError as callfile23:
        print("File entryfile23.txt doesn't exist !", callfile23)

    self.new_data23=line23
    self.x230, self.y230 = 129, 934
    self.Data_write=Entry(self.can)
    self.new_data23=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data23,
      highlightbackground='grey', bd=4)
    self.new_data23.set(line23)
    self.Data_write=self.can.create_window(self.x230, self.y230,
      window=self.Data_write)

    self.x231, self.y231 = 271, 934
    self.b231=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='aquamarine', text="Allergy",
        command=self.allergyLink23)
    self.fb231=self.can.create_window(self.x231, self.y231, window=self.b231)

    self.x232, self.y232 = 429, 934
    self.b232=Button(self.can, width=18, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Diagnostic + ATCD",
        command=self.diag23)
    self.fb232=self.can.create_window(self.x232, self.y232, window=self.b232)

    self.x233, self.y233 = 597, 934
    self.b233=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Treatments",
        command=self.tttMed23)
    self.fb233=self.can.create_window(self.x233, self.y233, window=self.b233)

    self.x234, self.y234 = 725, 934
    self.b234=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Laboratory",
        command=self.laboResult23)
    self.fb234=self.can.create_window(self.x234, self.y234, window=self.b234)

    self.x235, self.y235 = 853, 934
    self.b235=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Medical Visit",
        command=self.visitMed23)
    self.fb235=self.can.create_window(self.x235, self.y235, window=self.b235)

    self.x236, self.y236 = 981, 934
    self.b236=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="Intolerance",
        command=self.nutritionMenu23)
    self.fb236=self.can.create_window(self.x236, self.y236, window=self.b236)

    self.x237, self.y237 = 1109, 934
    self.b237=Button(self.can, width=10, font=16, bg='RoyalBlue3', fg='cyan',
        activebackground='aquamarine', text="BMI",
        command=self.calculB23)
    self.fb237=self.can.create_window(self.x237, self.y237, window=self.b237)

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24=namefile.readline()
    except FileNotFoundError as callfile24:
        print("File entryfile24.txt doesn't exist !", callfile24)

    self.new_data24=line24
    self.x240, self.y240 = 129, 966
    self.Data_write=Entry(self.can)
    self.new_data24=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data24,
      highlightbackground='grey', bd=4)
    self.new_data24.set(line24)
    self.Data_write=self.can.create_window(self.x240, self.y240,
      window=self.Data_write)

    self.x241, self.y241 = 271, 966
    self.b241=Button(self.can, width=8, font=16, bg='blue violet', fg='cyan',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink24)
    self.fb241=self.can.create_window(self.x241, self.y241, window=self.b241)

    self.x242, self.y242 = 429, 966
    self.b242=Button(self.can, width=18, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag24)
    self.fb242=self.can.create_window(self.x242, self.y242, window=self.b242)

    self.x243, self.y243 = 597, 966
    self.b243=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Treatments",
        command=self.tttMed24)
    self.fb243=self.can.create_window(self.x243, self.y243, window=self.b243)

    self.x244, self.y244 = 725, 966
    self.b244=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult24)
    self.fb244=self.can.create_window(self.x244, self.y244, window=self.b244)

    self.x245, self.y245 = 853, 966
    self.b245=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Medical Visit",
        command=self.visitMed24)
    self.fb245=self.can.create_window(self.x245, self.y245, window=self.b245)

    self.x246, self.y246 = 981, 966
    self.b246=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="Intolerance",
        command=self.nutritionMenu24)
    self.fb246=self.can.create_window(self.x246, self.y246, window=self.b246)

    self.x247, self.y247 = 1109, 966
    self.b247=Button(self.can, width=10, font=16, bg='DodgerBlue2', fg='white',
        activebackground='dark turquoise', text="BMI",
        command=self.calculB24)
    self.fb247=self.can.create_window(self.x247, self.y247, window=self.b247)

    self.can.configure(scrollregion=self.can.bbox(ALL))
