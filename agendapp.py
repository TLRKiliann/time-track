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
                        'Look at AGENDA,there is an appointment for patient 1!')
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
                        'Look at AGENDA, there is an appointment for patient 2!')
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
                        'Look at AGENDA, there is an appointment for patient 3!')
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
                        'Look at AGENDA, there is an appointment for patient 4!')
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
                        'Look at AGENDA, there is an appointment for patient 5!')
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
                        'Look at AGENDA, there is an appointment for patient 6!')
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
                        'Look at AGENDA, there is an appointment for patient 7!')
                else:
                    pass
    except FileNotFoundError as infofile7:
        print("File 7 has not been found", infofile7)
    else:
        ("Error unknow")