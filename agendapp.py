#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os
import time
import datetime


def dispAgBox():
    """
    Display messagebox for agenda if an 
    appointment has been fixed for tomorrow:
    """

    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            new_text1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)
        
    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text1 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile1:
        print("File 1 has not been found", infofile1)
    else:
        ("Error unknow 1")

    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2=namefile.readline()
            new_text2=line2
    except FileNotFoundError as fileout2:
        print("No file entryfile2.txt exist", fileout2)

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
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text2 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile2:
        print("File 2 has not been found", infofile2)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3=namefile.readline()
            new_text3=line3
    except FileNotFoundError as fileout3:
        print("No file entryfile3.txt exist", fileout3)

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
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text3 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile3:
        print("File 3 has not been found", infofile3)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4=namefile.readline()
            new_text4=line4
    except FileNotFoundError as fileout4:
        print("No file entryfile4.txt exist", fileout4)

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
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text4 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile4:
        print("File 4 has not been found", infofile4)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5=namefile.readline()
            new_text5=line5
    except FileNotFoundError as fileout5:
        print("No file entryfile5.txt exist", fileout5)

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
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text5 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile5:
        print("File 5 has not been found", infofile5)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6=namefile.readline()
            new_text6=line6
    except FileNotFoundError as fileout6:
        print("No file entryfile6.txt exist", fileout6)

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
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text6 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile6:
        print("File 6 has not been found", infofile6)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7=namefile.readline()
            new_text7=line7
    except FileNotFoundError as fileout7:
        print("No file entryfile7.txt exist", fileout7)

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
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text7 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile7:
        print("File 7 has not been found", infofile7)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8=namefile.readline()
            new_text8=line8
    except FileNotFoundError as fileout8:
        print("No file entryfile8.txt exist", fileout8)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events8/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text8 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile8:
        print("File 8 has not been found", infofile8)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9=namefile.readline()
            new_text9=line9
    except FileNotFoundError as fileout9:
        print("No file entryfile9.txt exist", fileout9)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events9/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text9 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile9:
        print("File 9 has not been found", infofile9)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10=namefile.readline()
            new_text10=line10
    except FileNotFoundError as fileout10:
        print("No file entryfile10.txt exist", fileout10)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events10/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text10 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile10:
        print("File 10 has not been found", infofile10)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11=namefile.readline()
            new_text11=line11
    except FileNotFoundError as fileout11:
        print("No file entryfile11.txt exist", fileout11)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events11/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text11 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile11:
        print("File 11 has not been found", infofile11)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12=namefile.readline()
            new_text12=line12
    except FileNotFoundError as fileout12:
        print("No file entryfile12.txt exist", fileout12)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events12/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text12 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile12:
        print("File 12 has not been found", infofile12)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13=namefile.readline()
            new_text13=line13
    except FileNotFoundError as fileout13:
        print("No file entryfile13.txt exist", fileout13)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events13/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text13 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile13:
        print("File 13 has not been found", infofile13)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14=namefile.readline()
            new_text14=line14
    except FileNotFoundError as fileout14:
        print("No file entryfile14.txt exist", fileout14)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events14/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text14 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile14:
        print("File 14 has not been found", infofile14)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15=namefile.readline()
            new_text15=line15
    except FileNotFoundError as fileout15:
        print("No file entryfile15.txt exist", fileout15)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events15/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text15 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile15:
        print("File 15 has not been found", infofile15)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16=namefile.readline()
            new_text16=line16
    except FileNotFoundError as fileout16:
        print("No file entryfile16.txt exist", fileout16)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events16/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text16 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile16:
        print("File 16 has not been found", infofile16)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17=namefile.readline()
            new_text17=line17
    except FileNotFoundError as fileout17:
        print("No file entryfile17.txt exist", fileout17)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events17/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text17 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile17:
        print("File 17 has not been found", infofile17)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18=namefile.readline()
            new_text18=line18
    except FileNotFoundError as fileout18:
        print("No file entryfile18.txt exist", fileout18)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events18/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text18 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile18:
        print("File 18 has not been found", infofile18)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19=namefile.readline()
            new_text19=line19
    except FileNotFoundError as fileout19:
        print("No file entryfile19.txt exist", fileout19)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events19/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text19 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile19:
        print("File 19 has not been found", infofile19)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20=namefile.readline()
            new_text20=line20
    except FileNotFoundError as fileout20:
        print("No file entryfile20.txt exist", fileout20)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events20/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text20 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile20:
        print("File 20 has not been found", infofile20)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21=namefile.readline()
            new_text21=line21
    except FileNotFoundError as fileout21:
        print("No file entryfile21.txt exist", fileout21)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events21/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text21 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile21:
        print("File 21 has not been found", infofile21)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22=namefile.readline()
            new_text22=line22
    except FileNotFoundError as fileout22:
        print("No file entryfile22.txt exist", fileout22)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events22/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text22 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile22:
        print("File 22 has not been found", infofile22)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23=namefile.readline()
            new_text23=line23
    except FileNotFoundError as fileout23:
        print("No file entryfile23.txt exist", fileout23)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events23/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text23 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile23:
        print("File 23 has not been found", infofile23)
    else:
        ("Error unknow")

    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24=namefile.readline()
            new_text24=line24
    except FileNotFoundError as fileout24:
        print("No file entryfile24.txt exist", fileout24)

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        with open('./patient_agenda/events24/doc_events/fix_agenda/fixed_rdv.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if dateagenda in line:
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA, there is an appointment tomorrow for : ' + new_text24 + lines[i] + \
                        lines[i+1] + lines[i+2])
                else:
                    pass
    except FileNotFoundError as infofile24:
        print("File 24 has not been found", infofile24)
    else:
        ("Error unknow")
