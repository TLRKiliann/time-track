#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import time
import datetime


# Synopsis page
def callBox(self):
    self.can.delete(ALL)
    self.can.configure(background='cyan')
    #self.photo=PhotoImage(file='./syno_gif/fondcolor2.png')
    #self.item=self.can.create_image(625, 400, image=self.photo)
    self.can.create_text(625, 30, anchor=CENTER, text="TIME-TRACK",
        font=('Times New Roman', 20), fill='blue')

    # To backup à revoir !!!!!!!!!!!!!!!!!!!!!!!!
    self.updateFiletxt()

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

    # To display time dynamically
    # To introduce a new pytient
    self.x3, self.y3 = 135, 110 # here
    self.b3=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='white', activebackground='dark turquoise',
        text="New Entry", command=self.callPatient1)
    self.fb3=self.can.create_window(self.x3, self.y3, window=self.b3)

    # To add one patient and files
    self.x4, self.y4 = 135, 170
    self.b4=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='cyan', activebackground='dark turquoise', 
        text="Add patient", command=self.addPatientAfter)
    self.fb4=self.can.create_window(self.x4, self.y4, window=self.b4)
    
    # To refresh canvas + menu bar
    self.x5, self.y5 = 135, 230
    self.b5=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='SpringGreen2', activebackground='yellow', activeforeground='blue',
        text="Refresh", command=self.upDateAll)
    self.fb5=self.can.create_window(self.x5, self.y5, window=self.b5)

    # To delete one patient and all files
    self.x6, self.y6 = 135, 290
    self.b6=Button(self.can, width=10, font=16, bd=3, highlightbackground='blue',
        bg='RoyalBlue3', fg='coral', activebackground='black', activeforeground='red',
        text="Delete patient", command=self.delEverPat)
    self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)

    # TextBox
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
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
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
                else:
                    pass
    except FileNotFoundError as infofileout20:
        print("File 20 has not been found", infofileout20)
    except IndexError as inforange20:
        print("List 20 got less than 6 lines", inforange20)
    else:
        ("Error unknow")

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi21/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n--- Patient 21 ---\n")
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
                else:
                    pass
    except FileNotFoundError as infofileout21:
        print("File 21 has not been found", infofileout21)
    except IndexError as inforange21:
        print("List 21 got less than 6 lines", inforange21)
    else:
        ("Error unknow")

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi22/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n--- Patient 22 ---\n")
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
                else:
                    pass
    except FileNotFoundError as infofileout22:
        print("File 22 has not been found", infofileout22)
    except IndexError as inforange22:
        print("List 22 got less than 6 lines", inforange22)
    else:
        ("Error unknow")

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi23/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n--- Patient 23 ---\n")
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
                else:
                    pass
    except FileNotFoundError as infofileout23:
        print("File 23 has not been found", infofileout23)
    except IndexError as inforange23:
        print("List 23 got less than 6 lines", inforange23)
    else:
        ("Error unknow")

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi24/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n--- Patient 24 ---\n")
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, lines[i+3])
                    self.t63.insert(INSERT, lines[i+4])
                    self.t63.insert(INSERT, lines[i+5])
                    self.t63.insert(INSERT, lines[i+6])
                else:
                    pass
    except FileNotFoundError as infofileout24:
        print("File 24 has not been found", infofileout24)
    except IndexError as inforange24:
        print("List 24 got less than 6 lines", inforange24)
    else:
        ("Error unknow")

    #Patient1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    self.data_time=line1
    self.x10, self.y10 = 129, 400
    self.Data_write=Entry(self.can)
    self.new_data1=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data1,
        highlightbackground='grey', bd=4)
    self.new_data1.set(line1)
    self.Data_write=self.can.create_window(self.x10, self.y10,
        window=self.Data_write)

    self.x11, self.y11 = 271, 400
    self.b11=Button(self.can, width=8, font=16, bg='grey30', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink)
    self.fb11=self.can.create_window(self.x11, self.y11, window=self.b11)

    self.x12, self.y12 = 429, 400
    self.b12=Button(self.can, width=18, font=16, bg='grey30', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag1)
    self.fb12=self.can.create_window(self.x12, self.y12, window=self.b12)

    self.x13, self.y13 = 597, 400
    self.b13=Button(self.can, width=10, font=16, bg='grey30', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult)
    self.fb13=self.can.create_window(self.x13, self.y13, window=self.b13)

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2=namefile.readline()
    except FileNotFoundError as callfile2:
        print("File entryfile2.txt doesn't exist !", callfile2)

    self.new_data2=line2
    self.x20, self.y20 = 129, 432
    self.Data_write=Entry(self.can)
    self.new_data2=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data2,
      highlightbackground='grey', bd=4)
    self.new_data2.set(line2)
    self.Data_write=self.can.create_window(self.x20, self.y20,
      window=self.Data_write)

    self.x21, self.y21 = 271, 432
    self.b21=Button(self.can, width=8, font=16, bg='grey25', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink2)
    self.fb21=self.can.create_window(self.x21, self.y21, window=self.b21)

    self.x22, self.y22 = 429, 432
    self.b22=Button(self.can, width=18, font=16, bg='grey25', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag2)
    self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)

    self.x22, self.y22 = 597, 432
    self.b22=Button(self.can, width=10, font=16, bg='grey25', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult2)
    self.fb22=self.can.create_window(self.x22, self.y22, window=self.b22)

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3=namefile.readline()
    except FileNotFoundError as callfile3:
        print("File entryfile3.txt doesn't exist !", callfile3)

    self.new_data3=line3
    self.x30, self.y30 = 129, 464
    self.Data_write=Entry(self.can)
    self.new_data3=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data3,
      highlightbackground='grey', bd=4)
    self.new_data3.set(line3)
    self.Data_write=self.can.create_window(self.x30, self.y30,
      window=self.Data_write)

    self.x31, self.y31 = 271, 464
    self.b31=Button(self.can, width=8, font=16, bg='grey20', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink3)
    self.fb31=self.can.create_window(self.x31, self.y31, window=self.b31)

    self.x32, self.y32 = 429, 464
    self.b32=Button(self.can, width=18, font=16, bg='grey20', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag3)
    self.fb32=self.can.create_window(self.x32, self.y32, window=self.b32)

    self.x33, self.y33 = 597, 464
    self.b33=Button(self.can, width=10, font=16, bg='grey20', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult3)
    self.fb33=self.can.create_window(self.x33, self.y33, window=self.b33)

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4=namefile.readline()
    except FileNotFoundError as callfile4:
        print("File entryfile4.txt doesn't exist !", callfile4)

    self.new_data4=line4
    self.x40, self.y40 = 129, 496
    self.Data_write=Entry(self.can)
    self.new_data4=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data4,
      highlightbackground='grey', bd=4)
    self.new_data4.set(line4)
    self.Data_write=self.can.create_window(self.x40, self.y40,
      window=self.Data_write)

    self.x41, self.y41 = 271, 496
    self.b41=Button(self.can, width=8, font=16, bg='grey18', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink4)
    self.fb41=self.can.create_window(self.x41, self.y41, window=self.b41)

    self.x42, self.y42 = 429, 496
    self.b42=Button(self.can, width=18, font=16, bg='grey18', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag4)
    self.fb42=self.can.create_window(self.x42, self.y42, window=self.b42)

    self.x43, self.y43 = 597, 496
    self.b43=Button(self.can, width=10, font=16, bg='grey18', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult4)
    self.fb43=self.can.create_window(self.x43, self.y43, window=self.b43)

    #patient5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5=namefile.readline()
    except FileNotFoundError as callfile5:
        print("File entryfile5.txt doesn't exist !", callfile5)

    self.new_data5=line5
    self.x50, self.y50 = 129, 528
    self.Data_write=Entry(self.can)
    self.new_data5=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data5,
      highlightbackground='grey', bd=4)
    self.new_data5.set(line5)
    self.Data_write=self.can.create_window(self.x50, self.y50,
      window=self.Data_write)

    self.x51, self.y51 = 271, 528
    self.b51=Button(self.can, width=8, font=16, bg='grey15', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink5)
    self.fb51=self.can.create_window(self.x51, self.y51, window=self.b51)

    self.x52, self.y52 = 429, 528
    self.b52=Button(self.can, width=18, font=16, bg='grey15', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag5)
    self.fb52=self.can.create_window(self.x52, self.y52, window=self.b52)

    self.x53, self.y53 = 597, 528
    self.b53=Button(self.can, width=10, font=16, bg='grey15', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult5)
    self.fb53=self.can.create_window(self.x53, self.y53, window=self.b53)

    #patient6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6=namefile.readline()
    except FileNotFoundError as callfile6:
        print("File entryfile6.txt doesn't exist !", callfile6)

    self.new_data6=line6
    self.x60, self.y60 = 129, 560
    self.Data_write=Entry(self.can)
    self.new_data6=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data6,
      highlightbackground='grey', bd=4)
    self.new_data6.set(line6)
    self.Data_write=self.can.create_window(self.x60, self.y60,
      window=self.Data_write)

    self.x61, self.y61 = 271, 560
    self.b61=Button(self.can, width=8, font=16, bg='grey12', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink6)
    self.fb61=self.can.create_window(self.x61, self.y61, window=self.b61)

    self.x62, self.y62 = 429, 560
    self.b62=Button(self.can, width=18, font=16, bg='grey12', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag6)
    self.fb62=self.can.create_window(self.x62, self.y62, window=self.b62)

    self.x64, self.y64 = 597, 560
    self.b64=Button(self.can, width=10, font=16, bg='grey12', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult6)
    self.fb64=self.can.create_window(self.x64, self.y64, window=self.b64)
    
    #patient7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7=namefile.readline()
    except FileNotFoundError as callfile7:
        print("File entryfile7.txt doesn't exist !", callfile7)

    self.new_data7=line7
    self.x70, self.y70 = 129, 592
    self.Data_write=Entry(self.can)
    self.new_data7=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data7,
      highlightbackground='grey', bd=4)
    self.new_data7.set(line7)
    self.Data_write=self.can.create_window(self.x70, self.y70,
      window=self.Data_write)

    self.x71, self.y71 = 271, 592
    self.b71=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink7)
    self.fb71=self.can.create_window(self.x71, self.y71, window=self.b71)

    self.x72, self.y72 = 429, 592
    self.b72=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag7)
    self.fb72=self.can.create_window(self.x72, self.y72, window=self.b72)

    self.x73, self.y73 = 597, 592
    self.b73=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult7)
    self.fb73=self.can.create_window(self.x73, self.y73, window=self.b73)

    #patient8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8=namefile.readline()
    except FileNotFoundError as callfile8:
        print("File entryfile8.txt doesn't exist !", callfile8)

    self.new_data8=line8
    self.x80, self.y80 = 129, 624
    self.Data_write=Entry(self.can)
    self.new_data8=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data8,
      highlightbackground='grey', bd=4)
    self.new_data8.set(line8)
    self.Data_write=self.can.create_window(self.x80, self.y80,
      window=self.Data_write)

    self.x81, self.y81 = 271, 624
    self.b81=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink8)
    self.fb81=self.can.create_window(self.x81, self.y81, window=self.b81)

    self.x82, self.y82 = 429, 624
    self.b82=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag8)
    self.fb82=self.can.create_window(self.x82, self.y82, window=self.b82)

    self.x83, self.y83 = 597, 624
    self.b83=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult8)
    self.fb83=self.can.create_window(self.x83, self.y83, window=self.b83)

    #patient9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9=namefile.readline()
    except FileNotFoundError as callfile9:
        print("File entryfile9.txt doesn't exist !", callfile9)

    self.new_data9=line9
    self.x90, self.y90 = 129, 656
    self.Data_write=Entry(self.can)
    self.new_data9=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data9,
      highlightbackground='grey', bd=4)
    self.new_data9.set(line9)
    self.Data_write=self.can.create_window(self.x90, self.y90,
      window=self.Data_write)

    self.x91, self.y91 = 271, 656
    self.b91=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink9)
    self.fb91=self.can.create_window(self.x91, self.y91, window=self.b91)

    self.x92, self.y92 = 429, 656
    self.b92=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag9)
    self.fb92=self.can.create_window(self.x92, self.y92, window=self.b92)

    self.x93, self.y93 = 597, 656
    self.b93=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult9)
    self.fb93=self.can.create_window(self.x93, self.y93, window=self.b93)

    #patient10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10=namefile.readline()
    except FileNotFoundError as callfile10:
        print("File entryfile10.txt doesn't exist !", callfile10)

    self.new_data10=line10
    self.x100, self.y100 = 129, 688
    self.Data_write=Entry(self.can)
    self.new_data10=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data10,
      highlightbackground='grey', bd=4)
    self.new_data10.set(line10)
    self.Data_write=self.can.create_window(self.x100, self.y100,
      window=self.Data_write)

    self.x101, self.y101 = 271, 688
    self.b101=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb101=self.can.create_window(self.x101, self.y101, window=self.b101)

    self.x102, self.y102 = 429, 688
    self.b102=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb102=self.can.create_window(self.x102, self.y102, window=self.b102)

    self.x103, self.y103 = 597, 688
    self.b103=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb103=self.can.create_window(self.x103, self.y103, window=self.b103)

    #patient11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11=namefile.readline()
    except FileNotFoundError as callfile11:
        print("File entryfile11.txt doesn't exist !", callfile11)

    self.new_data11=line11
    self.x110, self.y110 = 129, 720
    self.Data_write=Entry(self.can)
    self.new_data11=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data11,
      highlightbackground='grey', bd=4)
    self.new_data11.set(line11)
    self.Data_write=self.can.create_window(self.x110, self.y110,
      window=self.Data_write)

    self.x111, self.y111 = 271, 720
    self.b111=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb111=self.can.create_window(self.x111, self.y111, window=self.b111)

    self.x112, self.y112 = 429, 720
    self.b112=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb112=self.can.create_window(self.x112, self.y112, window=self.b112)

    self.x113, self.y113 = 597, 720
    self.b113=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb113=self.can.create_window(self.x113, self.y113, window=self.b113)

    #patient12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12=namefile.readline()
    except FileNotFoundError as callfile12:
        print("File entryfile12.txt doesn't exist !", callfile12)

    self.new_data12=line12
    self.x120, self.y120 = 129, 752
    self.Data_write=Entry(self.can)
    self.new_data12=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data12,
      highlightbackground='grey', bd=4)
    self.new_data12.set(line12)
    self.Data_write=self.can.create_window(self.x120, self.y120,
      window=self.Data_write)

    self.x121, self.y121 = 271, 752
    self.b121=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb121=self.can.create_window(self.x121, self.y121, window=self.b121)

    self.x122, self.y122 = 429, 752
    self.b122=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb122=self.can.create_window(self.x122, self.y122, window=self.b122)

    self.x123, self.y123 = 597, 752
    self.b123=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb123=self.can.create_window(self.x123, self.y123, window=self.b123)

    #patient13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13=namefile.readline()
    except FileNotFoundError as callfile13:
        print("File entryfile13.txt doesn't exist !", callfile13)

    self.new_data13=line13
    self.x130, self.y130 = 129, 784
    self.Data_write=Entry(self.can)
    self.new_data13=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data13,
      highlightbackground='grey', bd=4)
    self.new_data13.set(line13)
    self.Data_write=self.can.create_window(self.x130, self.y130,
      window=self.Data_write)

    self.x131, self.y131 = 271, 784
    self.b131=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb131=self.can.create_window(self.x131, self.y131, window=self.b131)

    self.x132, self.y132 = 429, 784
    self.b132=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb132=self.can.create_window(self.x132, self.y132, window=self.b132)

    self.x133, self.y133 = 597, 784
    self.b133=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb133=self.can.create_window(self.x133, self.y133, window=self.b133)

    #patient14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14=namefile.readline()
    except FileNotFoundError as callfile14:
        print("File entryfile14.txt doesn't exist !", callfile14)

    self.new_data14=line14
    self.x140, self.y140 = 129, 816
    self.Data_write=Entry(self.can)
    self.new_data14=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data14,
      highlightbackground='grey', bd=4)
    self.new_data14.set(line14)
    self.Data_write=self.can.create_window(self.x140, self.y140,
      window=self.Data_write)

    self.x141, self.y141 = 271, 816
    self.b141=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb141=self.can.create_window(self.x141, self.y141, window=self.b141)

    self.x142, self.y142 = 429, 816
    self.b142=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb142=self.can.create_window(self.x142, self.y142, window=self.b142)

    self.x143, self.y143 = 597, 816
    self.b143=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb143=self.can.create_window(self.x143, self.y143, window=self.b143)

    #patient15
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15=namefile.readline()
    except FileNotFoundError as callfile15:
        print("File entryfile15.txt doesn't exist !", callfile15)

    self.new_data15=line15
    self.x150, self.y150 = 129, 848
    self.Data_write=Entry(self.can)
    self.new_data15=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data15,
      highlightbackground='grey', bd=4)
    self.new_data15.set(line15)
    self.Data_write=self.can.create_window(self.x150, self.y150,
      window=self.Data_write)

    self.x151, self.y151 = 271, 848
    self.b151=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb151=self.can.create_window(self.x151, self.y151, window=self.b151)

    self.x152, self.y152 = 429, 848
    self.b152=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb152=self.can.create_window(self.x152, self.y152, window=self.b152)

    self.x153, self.y153 = 597, 848
    self.b153=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb153=self.can.create_window(self.x153, self.y153, window=self.b153)

    #patient16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16=namefile.readline()
    except FileNotFoundError as callfile16:
        print("File entryfile16.txt doesn't exist !", callfile16)

    self.new_data16=line16
    self.x160, self.y160 = 129, 880
    self.Data_write=Entry(self.can)
    self.new_data16=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data16,
      highlightbackground='grey', bd=4)
    self.new_data16.set(line16)
    self.Data_write=self.can.create_window(self.x160, self.y160,
      window=self.Data_write)

    self.x161, self.y161 = 271, 880
    self.b161=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb161=self.can.create_window(self.x161, self.y161, window=self.b161)

    self.x162, self.y162 = 429, 880
    self.b162=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb162=self.can.create_window(self.x162, self.y162, window=self.b162)

    self.x163, self.y163 = 597, 880
    self.b163=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb163=self.can.create_window(self.x163, self.y163, window=self.b163)

    #patient17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17=namefile.readline()
    except FileNotFoundError as callfile17:
        print("File entryfile17.txt doesn't exist !", callfile17)

    self.new_data17=line17
    self.x170, self.y170 = 129, 912
    self.Data_write=Entry(self.can)
    self.new_data17=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data17,
      highlightbackground='grey', bd=4)
    self.new_data17.set(line17)
    self.Data_write=self.can.create_window(self.x170, self.y170,
      window=self.Data_write)

    self.x171, self.y171 = 271, 912
    self.b171=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb171=self.can.create_window(self.x171, self.y171, window=self.b171)

    self.x172, self.y172 = 429, 912
    self.b172=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb172=self.can.create_window(self.x172, self.y172, window=self.b172)

    self.x173, self.y173 = 597, 912
    self.b173=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb173=self.can.create_window(self.x173, self.y173, window=self.b173)

    #patient18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18=namefile.readline()
    except FileNotFoundError as callfile18:
        print("File entryfile18.txt doesn't exist !", callfile18)

    self.new_data18=line18
    self.x180, self.y180 = 129, 944
    self.Data_write=Entry(self.can)
    self.new_data18=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data18,
      highlightbackground='grey', bd=4)
    self.new_data18.set(line18)
    self.Data_write=self.can.create_window(self.x180, self.y180,
      window=self.Data_write)

    self.x181, self.y181 = 271, 944
    self.b181=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb181=self.can.create_window(self.x181, self.y181, window=self.b181)

    self.x182, self.y182 = 429, 944
    self.b182=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb182=self.can.create_window(self.x182, self.y182, window=self.b182)

    self.x183, self.y183 = 597, 944
    self.b183=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb183=self.can.create_window(self.x183, self.y183, window=self.b183)

    #patient19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19=namefile.readline()
    except FileNotFoundError as callfile19:
        print("File entryfile19.txt doesn't exist !", callfile19)

    self.new_data19=line19
    self.x190, self.y190 = 129, 976
    self.Data_write=Entry(self.can)
    self.new_data19=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data19,
      highlightbackground='grey', bd=4)
    self.new_data19.set(line19)
    self.Data_write=self.can.create_window(self.x190, self.y190,
      window=self.Data_write)

    self.x191, self.y191 = 271, 976
    self.b191=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb191=self.can.create_window(self.x191, self.y191, window=self.b191)

    self.x192, self.y192 = 429, 976
    self.b192=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb192=self.can.create_window(self.x192, self.y192, window=self.b192)

    self.x193, self.y193 = 597, 976
    self.b193=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb193=self.can.create_window(self.x193, self.y193, window=self.b193)

    #patient20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20=namefile.readline()
    except FileNotFoundError as callfile20:
        print("File entryfile20.txt doesn't exist !", callfile20)

    self.new_data20=line20
    self.x200, self.y200 = 129, 1008
    self.Data_write=Entry(self.can)
    self.new_data20=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data20,
      highlightbackground='grey', bd=4)
    self.new_data20.set(line20)
    self.Data_write=self.can.create_window(self.x200, self.y200,
      window=self.Data_write)

    self.x201, self.y201 = 271, 1008
    self.b201=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb201=self.can.create_window(self.x201, self.y201, window=self.b201)

    self.x202, self.y202 = 429, 1008
    self.b202=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb202=self.can.create_window(self.x202, self.y202, window=self.b202)

    self.x203, self.y203 = 597, 1008
    self.b203=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb203=self.can.create_window(self.x203, self.y203, window=self.b203)

    #patient21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21=namefile.readline()
    except FileNotFoundError as callfile21:
        print("File entryfile21.txt doesn't exist !", callfile21)

    self.new_data21=line21
    self.x210, self.y210 = 129, 1040
    self.Data_write=Entry(self.can)
    self.new_data21=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data21,
      highlightbackground='grey', bd=4)
    self.new_data21.set(line21)
    self.Data_write=self.can.create_window(self.x210, self.y210,
      window=self.Data_write)

    self.x211, self.y211 = 271, 1040
    self.b211=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb211=self.can.create_window(self.x211, self.y211, window=self.b211)

    self.x212, self.y212 = 429, 1040
    self.b212=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb212=self.can.create_window(self.x212, self.y212, window=self.b212)

    self.x213, self.y213 = 597, 1040
    self.b213=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb213=self.can.create_window(self.x213, self.y213, window=self.b213)

    #patient22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22=namefile.readline()
    except FileNotFoundError as callfile22:
        print("File entryfile22.txt doesn't exist !", callfile22)

    self.new_data22=line22
    self.x220, self.y220 = 129, 1072
    self.Data_write=Entry(self.can)
    self.new_data22=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data22,
      highlightbackground='grey', bd=4)
    self.new_data22.set(line22)
    self.Data_write=self.can.create_window(self.x220, self.y220,
      window=self.Data_write)

    self.x221, self.y221 = 271, 1072
    self.b221=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb221=self.can.create_window(self.x221, self.y221, window=self.b221)

    self.x222, self.y222 = 429, 1072
    self.b222=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb222=self.can.create_window(self.x222, self.y222, window=self.b222)

    self.x223, self.y223 = 597, 1072
    self.b223=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb223=self.can.create_window(self.x223, self.y223, window=self.b223)

    #patient23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23=namefile.readline()
    except FileNotFoundError as callfile23:
        print("File entryfile23.txt doesn't exist !", callfile23)

    self.new_data23=line23
    self.x230, self.y230 = 129, 1104
    self.Data_write=Entry(self.can)
    self.new_data23=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data23,
      highlightbackground='grey', bd=4)
    self.new_data23.set(line23)
    self.Data_write=self.can.create_window(self.x230, self.y230,
      window=self.Data_write)

    self.x231, self.y231 = 271, 1104
    self.b231=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb231=self.can.create_window(self.x231, self.y231, window=self.b231)

    self.x232, self.y232 = 429, 1104
    self.b232=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb232=self.can.create_window(self.x232, self.y232, window=self.b232)

    self.x233, self.y233 = 597, 1104
    self.b233=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb233=self.can.create_window(self.x233, self.y233, window=self.b233)

    #patient24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24=namefile.readline()
    except FileNotFoundError as callfile24:
        print("File entryfile24.txt doesn't exist !", callfile24)

    self.new_data24=line24
    self.x240, self.y240 = 129, 1136
    self.Data_write=Entry(self.can)
    self.new_data24=StringVar()
    self.Data_write=Entry(self.can, textvariable=self.new_data24,
      highlightbackground='grey', bd=4)
    self.new_data24.set(line24)
    self.Data_write=self.can.create_window(self.x240, self.y240,
      window=self.Data_write)

    self.x241, self.y241 = 271, 1136
    self.b241=Button(self.can, width=8, font=16, bg='black', fg='coral',
        activebackground='dark turquoise', text="Allergy",
        command=self.allergyLink10)
    self.fb241=self.can.create_window(self.x241, self.y241, window=self.b241)

    self.x242, self.y242 = 429, 1136
    self.b242=Button(self.can, width=18, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Diagnostic + ATCD",
        command=self.diag10)
    self.fb242=self.can.create_window(self.x242, self.y242, window=self.b242)

    self.x243, self.y243 = 597, 1136
    self.b243=Button(self.can, width=10, font=16, bg='black', fg='cyan',
        activebackground='dark turquoise', text="Laboratory",
        command=self.laboResult10)
    self.fb243=self.can.create_window(self.x243, self.y243, window=self.b243)

    self.can.configure(scrollregion=self.can.bbox(ALL))
