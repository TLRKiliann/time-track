#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import time
import datetime


# Synopsis page
def callBox(self):
    self.can.delete(ALL)
    #self.photo=PhotoImage(file='./syno_gif/fondcolor2.png')
    #self.item=self.can.create_image(625, 400, image=self.photo)
    #self.can.create_text(625, 80, anchor=CENTER, text="SYNOPSIS",
    #    font=('Times New Roman', 40), fill='turquoise')

    # To backup à revoir !!!!!!!!!!!!!!!!!!!!!!!!
    self.updateFiletxt()

    # Display date
    self.x1, self.y1 = 1065, 70
    self.Date_write=Entry(self.can)
    self.data_time=StringVar()
    self.Date_write=Entry(textvariable=self.data_time, width=10,
        highlightbackground='grey', bd=4)
    self.data_time.set(time.strftime("%d/%m/%Y"))
    self.Date_write=self.can.create_window(self.x1, self.y1,
        window=self.Date_write)

    # Static time
    self.x2, self.y2 = 1165, 70
    self.Date_write2 = Entry(self.can)
    self.data_time2 = StringVar()
    self.Date_write2 = Entry(width=10, textvariable=self.data_time2,
        highlightbackground='grey', bd=4)
    self.data_time2.set(time.strftime("%H:%M:%S %p"))
    self.Date_write2=self.can.create_window(self.x2, self.y2,
        window=self.Date_write2)
    # To display time dynamically

    # To introduce a new pytient
    self.x100, self.y100 = 135, 110 # here
    self.b100=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='white', activebackground='dark turquoise',
        text="New Entry", command=self.callPatient1)
    self.fb100=self.can.create_window(self.x100, self.y100, window=self.b100)

    # To add one patient and files
    self.x200, self.y200 = 135, 170
    self.b200=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='cyan', activebackground='dark turquoise', 
        text="Add patient", command=self.addPatientAfter)
    self.fb200=self.can.create_window(self.x200, self.y200, window=self.b200)
    
    # To refresh canvas + menu bar
    self.x101, self.y101 = 135, 230
    self.b101=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='SpringGreen2', activebackground='yellow', activeforeground='blue',
        text="Refresh", command=self.upDateAll)
    self.fb101=self.can.create_window(self.x101, self.y101, window=self.b101)

    # To delete one patient and all files
    self.x200, self.y200 = 135, 290
    self.b200=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='coral', activebackground='black', activeforeground='red',
        text="Delete patient", command=self.delEverPat)
    self.fb200=self.can.create_window(self.x200, self.y200, window=self.b200)

    # TextBox !!!!!!!!!!!!!!!!!!!!!!!!!!!!@@@@@@########################
    self.x63, self.y63 = 625, 200
    self.t63=Text(self.can, height=15, width=70, font=18, relief=SUNKEN)
    self.t63.insert(INSERT, "Previously (yesterday last infos) : ")
    self.t63.insert(END, (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%d/%m/%Y'))
        #time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
    self.ft63=self.can.create_window(self.x63, self.y63, window=self.t63)

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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
                else:
                    pass
    except FileNotFoundError as infofileout8:
        print("File 8 has not been found", infofileout8)
    except IndexError as inforange8:
        print("List 8 got less than 6 lines", inforange8)
    else:
        ("Error unknow")

    #Patient1
    # For label below (in me2.add_command)
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
                else:
                    pass
    except FileNotFoundError as infofileout10:
        print("File 10 has not been found", infofileout10)
    except IndexError as inforange10:
        print("List 10 got less than 6 lines", inforange10)
    else:
        ("Error unknow")

    #Patient1
    # For label below (in me2.add_command)
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    self.data_time=line1
    self.x2, self.y2 = 129, 400
    self.Data_write=Entry(self.can)
    self.new_data1=StringVar()
    self.Data_write=Entry(textvariable=self.new_data1,
        highlightbackground='grey', bd=4)
    self.new_data1.set(line1)
    self.Data_write=self.can.create_window(self.x2, self.y2,
        window=self.Data_write)

    self.x3, self.y3 = 271, 400
    self.b=Button(self.can, width=8, font=16, bg='grey30', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink)
    self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

    self.x3, self.y3 = 429, 400
    self.b=Button(self.can, width=18, font=16, bg='grey30', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag1)
    self.fb=self.can.create_window(self.x3, self.y3, window=self.b)

    self.x4, self.y4 = 597, 400
    self.b4=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult)
    self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2=namefile.readline()
    except FileNotFoundError as callfile2:
        print("File entryfile2.txt doesn't exist !", callfile2)

    self.new_data2=line2
    self.x9, self.y9 = 129, 432
    self.Data_write=Entry(self.can)
    self.new_data2=StringVar()
    self.Data_write=Entry(textvariable=self.new_data2,
      highlightbackground='grey', bd=4)
    self.new_data2.set(line2)
    self.Data_write=self.can.create_window(self.x9, self.y9,
      window=self.Data_write)

    self.x10, self.y10 = 271, 432
    self.b10=Button(self.can, width=8, font=16, bg='grey25', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink2)
    self.fb10=self.can.create_window(self.x10, self.y10, window=self.b10)

    self.x13, self.y13 = 429, 432
    self.b13=Button(self.can, width=18, font=16, bg='grey25', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag2)
    self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

    self.x14, self.y14 = 597, 432
    self.b14=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult2)
    self.fb14=self.can.create_window(self.x14, self.y14, window=self.b14)

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3=namefile.readline()
    except FileNotFoundError as callfile3:
        print("File entryfile3.txt doesn't exist !", callfile3)

    self.new_data3=line3
    self.x18, self.y18 = 129, 464
    self.Data_write=Entry(self.can)
    self.new_data3=StringVar()
    self.Data_write=Entry(textvariable=self.new_data3,
      highlightbackground='grey', bd=4)
    self.new_data3.set(line3)
    self.Data_write=self.can.create_window(self.x18, self.y18,
      window=self.Data_write)

    self.x19, self.y19 = 271, 464
    self.b19=Button(self.can, width=8, font=16, bg='grey20', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink3)
    self.fb19=self.can.create_window(self.x19, self.y19, window=self.b19)

    self.x22, self.y22 = 429, 464
    self.b22=Button(self.can, width=18, font=16, bg='grey20', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag3)
    self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)

    self.x23, self.y23 = 597, 464
    self.b23=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult3)
    self.fb23=self.can.create_window(self.x23, self.y23, window=self.b23)

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4=namefile.readline()
    except FileNotFoundError as callfile4:
        print("File entryfile4.txt doesn't exist !", callfile4)

    self.new_data4=line4
    self.x27, self.y27 = 129, 496
    self.Data_write=Entry(self.can)
    self.new_data4=StringVar()
    self.Data_write=Entry(textvariable=self.new_data4,
      highlightbackground='grey', bd=4)
    self.new_data4.set(line4)
    self.Data_write=self.can.create_window(self.x27, self.y27,
      window=self.Data_write)

    self.x28, self.y28 = 271, 496
    self.b28=Button(self.can, width=8, font=16, bg='grey18', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink4)
    self.fb28=self.can.create_window(self.x28, self.y28, window=self.b28)

    self.x31, self.y31 = 429, 496
    self.b31=Button(self.can, width=18, font=16, bg='grey18', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag4)
    self.fb31=self.can.create_window(self.x31, self.y31, window=self.b31)

    self.x32, self.y32 = 597, 496
    self.b32=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult4)
    self.fb32=self.can.create_window(self.x32, self.y32, window=self.b32)

    #patient5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5=namefile.readline()
    except FileNotFoundError as callfile5:
        print("File entryfile5.txt doesn't exist !", callfile5)

    self.new_data5=line5
    self.x36, self.y36 = 129, 528
    self.Data_write=Entry(self.can)
    self.new_data5=StringVar()
    self.Data_write=Entry(textvariable=self.new_data5,
      highlightbackground='grey', bd=4)
    self.new_data5.set(line5)
    self.Data_write=self.can.create_window(self.x36, self.y36,
      window=self.Data_write)

    self.x37, self.y37 = 271, 528
    self.b37=Button(self.can, width=8, font=16, bg='grey15', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink5)
    self.fb37=self.can.create_window(self.x37, self.y37, window=self.b37)

    self.x40, self.y40 = 429, 528
    self.b40=Button(self.can, width=18, font=16, bg='grey15', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag5)
    self.fb40=self.can.create_window(self.x40, self.y40, window=self.b40)

    self.x41, self.y41 = 597, 528
    self.b41=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult5)
    self.fb41=self.can.create_window(self.x41, self.y41, window=self.b41)

    #patient6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6=namefile.readline()
    except FileNotFoundError as callfile6:
        print("File entryfile6.txt doesn't exist !", callfile6)

    self.new_data6=line6
    self.x45, self.y45 = 129, 560
    self.Data_write=Entry(self.can)
    self.new_data6=StringVar()
    self.Data_write=Entry(textvariable=self.new_data6,
      highlightbackground='grey', bd=4)
    self.new_data6.set(line6)
    self.Data_write=self.can.create_window(self.x45, self.y45,
      window=self.Data_write)

    self.x46, self.y46 = 271, 560
    self.b46=Button(self.can, width=8, font=16, bg='grey12', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink6)
    self.fb46=self.can.create_window(self.x46, self.y46, window=self.b46)

    self.x49, self.y49 = 429, 560
    self.b49=Button(self.can, width=18, font=16, bg='grey12', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag6)
    self.fb49=self.can.create_window(self.x49, self.y49, window=self.b49)

    self.x50, self.y50 = 597, 560
    self.b50=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult6)
    self.fb50=self.can.create_window(self.x50, self.y50, window=self.b50)
    
    #patient7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7=namefile.readline()
    except FileNotFoundError as callfile7:
        print("File entryfile7.txt doesn't exist !", callfile7)

    self.new_data7=line7
    self.x54, self.y54 = 129, 592
    self.Data_write=Entry(self.can)
    self.new_data7=StringVar()
    self.Data_write=Entry(textvariable=self.new_data7,
      highlightbackground='grey', bd=4)
    self.new_data7.set(line7)
    self.Data_write=self.can.create_window(self.x54, self.y54,
      window=self.Data_write)

    self.x54, self.y54 = 271, 592
    self.b54=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink7)
    self.fb54=self.can.create_window(self.x54, self.y54, window=self.b54)

    self.x57, self.y57 = 429, 592
    self.b57=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag7)
    self.fb57=self.can.create_window(self.x57, self.y57, window=self.b57)

    self.x58, self.y58 = 597, 592
    self.b58=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult7)
    self.fb58=self.can.create_window(self.x58, self.y58, window=self.b58)

    #patient8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8=namefile.readline()
    except FileNotFoundError as callfile8:
        print("File entryfile8.txt doesn't exist !", callfile8)

    self.new_data8=line8
    self.x54, self.y54 = 129, 624
    self.Data_write=Entry(self.can)
    self.new_data8=StringVar()
    self.Data_write=Entry(textvariable=self.new_data8,
      highlightbackground='grey', bd=4)
    self.new_data8.set(line8)
    self.Data_write=self.can.create_window(self.x54, self.y54,
      window=self.Data_write)

    self.x54, self.y54 = 271, 624
    self.b54=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink8)
    self.fb54=self.can.create_window(self.x54, self.y54, window=self.b54)

    self.x57, self.y57 = 429, 624
    self.b57=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag8)
    self.fb57=self.can.create_window(self.x57, self.y57, window=self.b57)

    self.x58, self.y58 = 597, 624
    self.b58=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult8)
    self.fb58=self.can.create_window(self.x58, self.y58, window=self.b58)

    #patient9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9=namefile.readline()
    except FileNotFoundError as callfile9:
        print("File entryfile9.txt doesn't exist !", callfile9)

    self.new_data9=line9
    self.x54, self.y54 = 129, 656
    self.Data_write=Entry(self.can)
    self.new_data9=StringVar()
    self.Data_write=Entry(textvariable=self.new_data9,
      highlightbackground='grey', bd=4)
    self.new_data9.set(line9)
    self.Data_write=self.can.create_window(self.x54, self.y54,
      window=self.Data_write)

    self.x54, self.y54 = 271, 656
    self.b54=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink9)
    self.fb54=self.can.create_window(self.x54, self.y54, window=self.b54)

    self.x57, self.y57 = 429, 656
    self.b57=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag9)
    self.fb57=self.can.create_window(self.x57, self.y57, window=self.b57)

    self.x58, self.y58 = 597, 656
    self.b58=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult9)
    self.fb58=self.can.create_window(self.x58, self.y58, window=self.b58)

    #patient10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10=namefile.readline()
    except FileNotFoundError as callfile10:
        print("File entryfile10.txt doesn't exist !", callfile10)

    self.new_data10=line10
    self.x54, self.y54 = 129, 688
    self.Data_write=Entry(self.can)
    self.new_data10=StringVar()
    self.Data_write=Entry(textvariable=self.new_data10,
      highlightbackground='grey', bd=4)
    self.new_data10.set(line10)
    self.Data_write=self.can.create_window(self.x54, self.y54,
      window=self.Data_write)

    self.x54, self.y54 = 271, 688
    self.b54=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb54=self.can.create_window(self.x54, self.y54, window=self.b54)

    self.x57, self.y57 = 429, 688
    self.b57=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb57=self.can.create_window(self.x57, self.y57, window=self.b57)

    self.x58, self.y58 = 597, 688
    self.b58=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb58=self.can.create_window(self.x58, self.y58, window=self.b58)
    self.can.configure(scrollregion=self.can.bbox(ALL))
