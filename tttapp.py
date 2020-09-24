#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import json
import os
import time
import datetime


def dispTttBox():
    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            line_text1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        #initword = value[0]["Date of end"]
        #with open('./ttt/doc_ttt/intro_ttt.txt', 'r') as filedate:
        x = 0 or 1 or 2 or 3 or 4 or 5 or 6
        file = open('./ttt/doc_ttt/convdose.json')
        data=json.load(file)
        for (key, value) in data.items():
            print(str(value[x]["Date of end"]))
            datend = (str(value[x]["Date of end"]))
            if datend == word_treattostop:
                print(datend)
                name_treat = (str(value[x]["Treatment"]))
                print(name_treat)
                dose = (str(value[x]["Dosage"]))
                print(dose)
                """
                lines = filedate.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if initword in line:
                        print(line)
                        if word_treattostop in line:
                            print(line)
                """
                MSBTTT2 = messagebox.showwarning('Warning',
                    'Look at TTT, there is a ttt to stop at' + " " + word_treattostop + " " + 'for : ' + \
                    "\n" + line_text1 + "Date of end : " +datend + "\n" + name_treat + "\n" + dose) #+ lines[i-6] + lines[i-5])
    except IndexError as error_ttt:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 1)", error_ttt)
    except FileNotFoundError as info_ttt:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 1)", info_ttt)
    else:
        ("Error unknow 1")

    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            line2=namefile.readline()
            ttt_text2=line2
    except FileNotFoundError as fileout2:
        print("No file entryfile2.txt exist", fileout2)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt2/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text2 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt2:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 2)", info_ttt2)
    else:
        ("Error unknow 2")

    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            line3=namefile.readline()
            ttt_text3=line3
    except FileNotFoundError as fileout3:
        print("No file entryfile3.txt exist", fileout3)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt3/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text3 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt3:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 3)", info_ttt3)
    else:
        ("Error unknow 3")

    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            line4=namefile.readline()
            ttt_text4=line4
    except FileNotFoundError as fileout4:
        print("No file entryfile4.txt exist", fileout4)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt4/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text4 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt4:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 4)", info_ttt4)
    else:
        ("Error unknow 4")

    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            line5=namefile.readline()
            ttt_text5=line5
    except FileNotFoundError as fileout5:
        print("No file entryfile5.txt exist", fileout5)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt5/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text5 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt5:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 5)", info_ttt5)
    else:
        ("Error unknow 5")

    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            line6=namefile.readline()
            ttt_text6=line6
    except FileNotFoundError as fileout6:
        print("No file entryfile6.txt exist", fileout6)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt6/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text6 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt6:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 6)", info_ttt6)
    else:
        ("Error unknow 6")

    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            line7=namefile.readline()
            ttt_text7=line7
    except FileNotFoundError as fileout7:
        print("No file entryfile7.txt exist", fileout7)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt7/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text7 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt7:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 7)", info_ttt7)
    else:
        ("Error unknow 7")

    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            line8=namefile.readline()
            ttt_text8=line8
    except FileNotFoundError as fileout8:
        print("No file entryfile8.txt exist", fileout8)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt8/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text8 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt8:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 8)", info_ttt8)
    else:
        ("Error unknow 8")

    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            line9=namefile.readline()
            ttt_text9=line9
    except FileNotFoundError as fileout9:
        print("No file entryfile9.txt exist", fileout9)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt9/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text9 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt9:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 9)", info_ttt9)
    else:
        ("Error unknow 9")

    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            line10=namefile.readline()
            ttt_text10=line10
    except FileNotFoundError as fileout10:
        print("No file entryfile10.txt exist", fileout10)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt10/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text10 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt10:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 10)", info_ttt10)
    else:
        ("Error unknow 10")

    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            line11=namefile.readline()
            ttt_text11=line11
    except FileNotFoundError as fileout11:
        print("No file entryfile11.txt exist", fileout11)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt11/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text11 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt11:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 11)", info_ttt11)
    else:
        ("Error unknow 11")

    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            line12=namefile.readline()
            ttt_text12=line12
    except FileNotFoundError as fileout12:
        print("No file entryfile12.txt exist", fileout12)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt12/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text12 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt12:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 12)", info_ttt12)
    else:
        ("Error unknow 12")

    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            line13=namefile.readline()
            ttt_text13=line13
    except FileNotFoundError as fileout13:
        print("No file entryfile13.txt exist", fileout13)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt13/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text3 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt13:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 13)", info_ttt13)
    else:
        ("Error unknow 13")

    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            line14=namefile.readline()
            ttt_text14=line14
    except FileNotFoundError as fileout14:
        print("No file entryfile14.txt exist", fileout14)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt14/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text14 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt14:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 14)", info_ttt14)
    else:
        ("Error unknow 14")

    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            line15=namefile.readline()
            ttt_text15=line15
    except FileNotFoundError as fileout15:
        print("No file entryfile15.txt exist", fileout15)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt15/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text15 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt15:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 15)", info_ttt15)
    else:
        ("Error unknow 15")

    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            line16=namefile.readline()
            ttt_text16=line16
    except FileNotFoundError as fileout16:
        print("No file entryfile16.txt exist", fileout16)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt16/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text16 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt16:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 16)", info_ttt16)
    else:
        ("Error unknow 16")

    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            line17=namefile.readline()
            ttt_text17=line17
    except FileNotFoundError as fileout17:
        print("No file entryfile17.txt exist", fileout17)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt17/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text17 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt17:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 17)", info_ttt17)
    else:
        ("Error unknow 17")

    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            line18=namefile.readline()
            ttt_text18=line18
    except FileNotFoundError as fileout18:
        print("No file entryfile18.txt exist", fileout18)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt18/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text18 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt18:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 18)", info_ttt18)
    else:
        ("Error unknow 18")

    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            line19=namefile.readline()
            ttt_text19=line19
    except FileNotFoundError as fileout19:
        print("No file entryfile19.txt exist", fileout19)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt19/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text19 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt19:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 19)", info_ttt19)
    else:
        ("Error unknow 19")

    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            line20=namefile.readline()
            ttt_text20=line20
    except FileNotFoundError as fileout20:
        print("No file entryfile20.txt exist", fileout20)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt20/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text20 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt20:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 20)", info_ttt20)
    else:
        ("Error unknow 20")

    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            line21=namefile.readline()
            ttt_text21=line21
    except FileNotFoundError as fileout21:
        print("No file entryfile21.txt exist", fileout21)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt21/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text21 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt21:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 21)", info_ttt21)
    else:
        ("Error unknow 21")

    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            line22=namefile.readline()
            ttt_text22=line22
    except FileNotFoundError as fileout22:
        print("No file entryfile22.txt exist", fileout22)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt22/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text22 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt22:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 22)", info_ttt22)
    else:
        ("Error unknow 22")

    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            line23=namefile.readline()
            ttt_text23=line23
    except FileNotFoundError as fileout23:
        print("No file entryfile23.txt exist", fileout23)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt23/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text23 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt23:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 23)", info_ttt23)
    else:
        ("Error unknow 23")

    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            line24=namefile.readline()
            ttt_text24=line24
    except FileNotFoundError as fileout24:
        print("No file entryfile24.txt exist", fileout24)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt24/intro_ttt.txt', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt to stop tomorrow for : ' + ttt_text24 + \
                            lines[i] + lines[i-6] + lines[i-5])
    except FileNotFoundError as info_ttt24:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 24)", info_ttt24)
    else:
        ("Error unknow 24")
