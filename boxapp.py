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
from patcaps import callResident

# Main page
def callBox(self):
    self.can.delete(ALL)
    self.can.configure(background='cyan')
    self.photo=PhotoImage(file='./syno_gif/title_tt.png')
    self.item=self.can.create_image(625, 85, image=self.photo)

    # To backup (main file)
    self.updateFiletxt()
    dispAgBox()
    dispTttBox()
    dispResFunc()

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

    # To go to resident page
    self.x6, self.y6 = 115, 75
    self.b6=Button(self.can, width=10, font=16, bd=3, bg='RoyalBlue3', fg='white', 
        highlightbackground='blue', activebackground='dark turquoise',
        activeforeground='white', text="Resident page", command=self.showPatients)
    self.fb6=self.can.create_window(self.x6, self.y6, window=self.b6)

    # TextBox
    self.x63, self.y63 = 625, 450
    self.t63=Text(self.can, height=30, width=80, font=18, relief=SUNKEN)
    self.t63.insert(INSERT, "Previously (yesterday last infos) : ")
    self.t63.insert(END, (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%d/%m/%Y'))
        #time.strftime("%d/%m/%Y at %H:%M:%S :\n"))
    self.ft63=self.can.create_window(self.x63, self.y63, window=self.t63)

    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    # Display text in textbox from 14 Needs files
    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line1)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout:
        print("File 1 has not been found", infofileout)
    except IndexError as inforange:
        print("List 1 got less than 6 lines", inforange)
    else:
        ("Error unknow 1")

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2=namefile.readline()
    except FileNotFoundError as callfile2:
        print("File entryfile2.txt doesn't exist !", callfile2)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi2/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line2)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout1:
        print("File 2 has not been found", infofileout1)
    except IndexError as inforange2:
        print("List 2 got less than 6 lines", inforange2)
    else:
        ("Error unknow")

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3=namefile.readline()
    except FileNotFoundError as callfile3:
        print("File entryfile3.txt doesn't exist !", callfile3)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi3/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line3)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout3:
        print("File 3 has not been found", infofileout3)
    except IndexError as inforange3:
        print("List 3 got less than 6 lines", inforange3)
    else:
        ("Error unknow")

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4=namefile.readline()
    except FileNotFoundError as callfile4:
        print("File entryfile4.txt doesn't exist !", callfile4)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi4/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line4)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout4:
        print("File 4 has not been found", infofileout4)
    except IndexError as inforange4:
        print("List 4 got less than 6 lines", inforange4)
    else:
        ("Error unknow")

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5=namefile.readline()
    except FileNotFoundError as callfile5:
        print("File entryfile5.txt doesn't exist !", callfile5)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi5/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line5)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout5:
        print("File 5 has not been found", infofileout5)
    except IndexError as inforange5:
        print("List 5 got less than 6 lines", inforange5)
    else:
        ("Error unknow")

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6=namefile.readline()
    except FileNotFoundError as callfile6:
        print("File entryfile6.txt doesn't exist !", callfile6)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi6/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line6)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout6:
        print("File 6 has not been found", infofileout6)
    except IndexError as inforange6:
        print("List 6 got less than 6 lines", inforange6)
    else:
        ("Error unknow")

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7=namefile.readline()
    except FileNotFoundError as callfile7:
        print("File entryfile7.txt doesn't exist !", callfile7)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi7/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line7)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout7:
        print("File 7 has not been found", infofileout7)
    except IndexError as inforange7:
        print("List 7 got less than 6 lines", inforange7)
    else:
        ("Error unknow")

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8=namefile.readline()
    except FileNotFoundError as callfile8:
        print("File entryfile8.txt doesn't exist !", callfile8)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi8/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line8)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout8:
        print("File 8 has not been found", infofileout8)
    except IndexError as inforange8:
        print("List 8 got less than 6 lines", inforange8)
    else:
        ("Error unknow")

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9=namefile.readline()
    except FileNotFoundError as callfile9:
        print("File entryfile9.txt doesn't exist !", callfile9)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi9/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line9)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout9:
        print("File 9 has not been found", infofileout9)
    except IndexError as inforange9:
        print("List 9 got less than 6 lines", inforange9)
    else:
        ("Error unknow")

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10=namefile.readline()
    except FileNotFoundError as callfile10:
        print("File entryfile10.txt doesn't exist !", callfile10)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi10/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line10)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout10:
        print("File 10 has not been found", infofileout10)
    except IndexError as inforange10:
        print("List 10 got less than 6 lines", inforange10)
    else:
        ("Error unknow")

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11=namefile.readline()
    except FileNotFoundError as callfile11:
        print("File entryfile11.txt doesn't exist !", callfile11)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi11/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line11)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout11:
        print("File 11 has not been found", infofileout11)
    except IndexError as inforange11:
        print("List 11 got less than 6 lines", inforange11)
    else:
        ("Error unknow")

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12=namefile.readline()
    except FileNotFoundError as callfile12:
        print("File entryfile12.txt doesn't exist !", callfile12)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi12/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line12)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout12:
        print("File 12 has not been found", infofileout12)
    except IndexError as inforange12:
        print("List 12 got less than 6 lines", inforange12)
    else:
        ("Error unknow")

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13=namefile.readline()
    except FileNotFoundError as callfile13:
        print("File entryfile13.txt doesn't exist !", callfile13)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi13/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line13)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout13:
        print("File 13 has not been found", infofileout13)
    except IndexError as inforange13:
        print("List 13 got less than 6 lines", inforange13)
    else:
        ("Error unknow")

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14=namefile.readline()
    except FileNotFoundError as callfile14:
        print("File entryfile14.txt doesn't exist !", callfile14)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi14/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line14)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout14:
        print("File 14 has not been found", infofileout14)
    except IndexError as inforange14:
        print("List 14 got less than 6 lines", inforange14)
    else:
        ("Error unknow")

    # Patient 15
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15=namefile.readline()
    except FileNotFoundError as callfile15:
        print("File entryfile15.txt doesn't exist !", callfile15)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi15/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line15)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout15:
        print("File 15 has not been found", infofileout15)
    except IndexError as inforange15:
        print("List 15 got less than 6 lines", inforange15)
    else:
        ("Error unknow")

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16=namefile.readline()
    except FileNotFoundError as callfile16:
        print("File entryfile16.txt doesn't exist !", callfile16)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi16/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line16)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout16:
        print("File 16 has not been found", infofileout16)
    except IndexError as inforange16:
        print("List 16 got less than 6 lines", inforange16)
    else:
        ("Error unknow")

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17=namefile.readline()
    except FileNotFoundError as callfile17:
        print("File entryfile17.txt doesn't exist !", callfile17)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi17/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line17)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout17:
        print("File 17 has not been found", infofileout17)
    except IndexError as inforange17:
        print("List 17 got less than 6 lines", inforange17)
    else:
        ("Error unknow")

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18=namefile.readline()
    except FileNotFoundError as callfile18:
        print("File entryfile18.txt doesn't exist !", callfile18)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi18/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line18)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout18:
        print("File 18 has not been found", infofileout18)
    except IndexError as inforange18:
        print("List 18 got less than 6 lines", inforange18)
    else:
        ("Error unknow")

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19=namefile.readline()
    except FileNotFoundError as callfile19:
        print("File entryfile19.txt doesn't exist !", callfile19)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi19/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line19)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout19:
        print("File 19 has not been found", infofileout19)
    except IndexError as inforange19:
        print("List 19 got less than 6 lines", inforange19)
    else:
        ("Error unknow")

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20=namefile.readline()
    except FileNotFoundError as callfile20:
        print("File entryfile20.txt doesn't exist !", callfile20)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi20/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line20)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout20:
        print("File 20 has not been found", infofileout20)
    except IndexError as inforange20:
        print("List 20 got less than 6 lines", inforange20)
    else:
        ("Error unknow")

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21=namefile.readline()
    except FileNotFoundError as callfile21:
        print("File entryfile21.txt doesn't exist !", callfile21)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi21/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line21)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout21:
        print("File 21 has not been found", infofileout21)
    except IndexError as inforange21:
        print("List 21 got less than 6 lines", inforange21)
    else:
        ("Error unknow")

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22=namefile.readline()
    except FileNotFoundError as callfile22:
        print("File entryfile22.txt doesn't exist !", callfile22)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi22/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line22)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout22:
        print("File 22 has not been found", infofileout22)
    except IndexError as inforange22:
        print("List 22 got less than 6 lines", inforange22)
    else:
        ("Error unknow")

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23=namefile.readline()
    except FileNotFoundError as callfile23:
        print("File entryfile23.txt doesn't exist !", callfile23)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi23/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line23)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout23:
        print("File 23 has not been found", infofileout23)
    except IndexError as inforange23:
        print("List 23 got less than 6 lines", inforange23)
    else:
        ("Error unknow")

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24=namefile.readline()
    except FileNotFoundError as callfile24:
        print("File entryfile24.txt doesn't exist !", callfile24)

    try:
        datesearch = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./14besoins/doc_suivi24/main_14b.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if datesearch in line:
                    self.t63.insert(END, "\n\n---> " + line24)
                    self.t63.insert(INSERT, line)
                    self.t63.insert(INSERT, lines[i+1])
                    self.t63.insert(INSERT, lines[i+2])
                    self.t63.insert(INSERT, "Lire suite dans care and monitoring...")
                else:
                    pass
    except FileNotFoundError as infofileout24:
        print("File 24 has not been found", infofileout24)
    except IndexError as inforange24:
        print("List 24 got less than 6 lines", inforange24)
    else:
        ("Error unknow")
        
    self.can.configure(scrollregion=self.can.bbox(ALL))
