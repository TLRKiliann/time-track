#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import time
import datetime


def displayDates(self):
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
                    print(line)
                    print(lines[i+1])
                    print(lines[i+2])
                    MSB2 = messagebox.showwarning('Info',
                        'Look at AGENDA,there is an appointment for patient 1 !')
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
                        'Look at AGENDA, there is an appointment for patient 2 !')
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
                        'Look at AGENDA, there is an appointment for patient 3 !')
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
                        'Look at AGENDA, there is an appointment for patient 4 !')
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
                        'Look at AGENDA, there is an appointment for patient 5 !')
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
                        'Look at AGENDA, there is an appointment for patient 6 !')
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
                        'Look at AGENDA, there is an appointment for patient 7 !')
                else:
                    pass
    except FileNotFoundError as infofile7:
        print("File 7 has not been found", infofile7)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 8 !')
                else:
                    pass
    except FileNotFoundError as infofile8:
        print("File 8 has not been found", infofile8)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 9 !')
                else:
                    pass
    except FileNotFoundError as infofile9:
        print("File 9 has not been found", infofile9)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 10 !')
                else:
                    pass
    except FileNotFoundError as infofile10:
        print("File 10 has not been found", infofile10)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 11 !')
                else:
                    pass
    except FileNotFoundError as infofile11:
        print("File 11 has not been found", infofile11)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 12 !')
                else:
                    pass
    except FileNotFoundError as infofile12:
        print("File 12 has not been found", infofile12)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 13 !')
                else:
                    pass
    except FileNotFoundError as infofile13:
        print("File 13 has not been found", infofile13)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 14 !')
                else:
                    pass
    except FileNotFoundError as infofile14:
        print("File 14 has not been found", infofile14)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 15 !')
                else:
                    pass
    except FileNotFoundError as infofile15:
        print("File 15 has not been found", infofile15)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 16 !')
                else:
                    pass
    except FileNotFoundError as infofile16:
        print("File 16 has not been found", infofile16)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 17 !')
                else:
                    pass
    except FileNotFoundError as infofile17:
        print("File 17 has not been found", infofile17)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 18 !')
                else:
                    pass
    except FileNotFoundError as infofile18:
        print("File 18 has not been found", infofile18)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 19 !')
                else:
                    pass
    except FileNotFoundError as infofile19:
        print("File 19 has not been found", infofile19)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 20 !')
                else:
                    pass
    except FileNotFoundError as infofile20:
        print("File 20 has not been found", infofile20)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 21 !')
                else:
                    pass
    except FileNotFoundError as infofile21:
        print("File 21 has not been found", infofile21)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 22 !')
                else:
                    pass
    except FileNotFoundError as infofile22:
        print("File 22 has not been found", infofile22)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 23 !')
                else:
                    pass
    except FileNotFoundError as infofile23:
        print("File 23 has not been found", infofile23)
    else:
        ("Error unknow")

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
                        'Look at AGENDA, there is an appointment for patient 24 !')
                else:
                    pass
    except FileNotFoundError as infofile24:
        print("File 24 has not been found", infofile24)
    else:
        ("Error unknow")
