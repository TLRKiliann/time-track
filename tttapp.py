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
            line_text1 = namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    try:
        word_ttstop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file = open('./ttt/doc_ttt/convdose.json')
        data=json.load(file)
        for (key, value) in data.items():
            listdata_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x:
                print(str(value[x]["Date of end"]))
                date_end = (str(value[x]["Date of end"]))
                if date_end == word_ttstop:
                    print(date_end)
                    name_treat = (str(value[x]["Treatment"]))
                    print(name_treat)
                    dose_ttt = (str(value[x]["Dosage"]))
                    print(dose_ttt)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop + " " + \
                        'for : ' + "\n" + line_text1 + "Date of end : " + date_end + "\n" + name_treat + \
                        "\n" + dose_ttt) 
    except IndexError as error_ttt:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 1)", error_ttt)
    except FileNotFoundError as info_ttt:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 1)", info_ttt)
    else:
        ("Error unknow 1")

    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile2:
            ttt_text2 = namefile2.readline()
    except FileNotFoundError as fileout2:
        print("No file entryfile2.txt exist", fileout2)

    try:
        word_ttstop2 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file2 = open('./ttt/doc_ttt2/convdose.json')
        data2 = json.load(file2)
        for (key, value) in data2.items():
            listdata_x2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x2:
                print(str(value[x]["Date of end"]))
                date_end2 = (str(value[x]["Date of end"]))
                if date_end2 == word_ttstop2:
                    print(date_end2)
                    name_treat2 = (str(value[x]["Treatment"]))
                    print(name_treat2)
                    dose_ttt2 = (str(value[x]["Dosage"]))
                    print(dose_ttt2)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop2 + " " + \
                        'for : ' + "\n" + ttt_text2 + "Date of end : " + date_end2 + "\n" + name_treat2 + \
                        "\n" + dose_ttt2) 
    except IndexError as error_ttt2:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 2)", error_ttt2)
    except FileNotFoundError as info_ttt2:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 2)", info_ttt2)
    else:
        ("Error unknow 2")

    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile3:
            ttt_text3 = namefile3.readline()
    except FileNotFoundError as fileout3:
        print("No file entryfile3.txt exist", fileout3)

    try:
        word_ttstop3 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file3 = open('./ttt/doc_ttt3/convdose.json')
        data3 = json.load(file3)
        for (key, value) in data3.items():
            listdata_x3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x3:
                print(str(value[x]["Date of end"]))
                date_end3 = (str(value[x]["Date of end"]))
                if date_end3 == word_ttstop3:
                    print(date_end3)
                    name_treat3 = (str(value[x]["Treatment"]))
                    print(name_treat3)
                    dose_ttt3 = (str(value[x]["Dosage"]))
                    print(dose_ttt3)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop3 + " " + \
                        'for : ' + "\n" + ttt_text3 + "Date of end : " + date_end3 + "\n" + name_treat3 + \
                        "\n" + dose_ttt3) 
    except IndexError as error_ttt3:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 3)", error_ttt3)
    except FileNotFoundError as info_ttt3:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 3)", info_ttt3)
    else:
        ("Error unknow 3")

    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile4:
            ttt_text4 = namefile4.readline()
    except FileNotFoundError as fileout4:
        print("No file entryfile4.txt exist", fileout4)

    try:
        word_ttstop4 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file4 = open('./ttt/doc_ttt4/convdose.json')
        data4 = json.load(file4)
        for (key, value) in data4.items():
            listdata_x4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x4:
                print(str(value[x]["Date of end"]))
                date_end4 = (str(value[x]["Date of end"]))
                if date_end4 == word_ttstop4:
                    print(date_end4)
                    name_treat4 = (str(value[x]["Treatment"]))
                    print(name_treat4)
                    dose_ttt4 = (str(value[x]["Dosage"]))
                    print(dose_ttt4)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop4 + " " + \
                        'for : ' + "\n" + ttt_text4 + "Date of end : " + date_end4 + "\n" + name_treat4 + \
                        "\n" + dose_ttt4) 
    except IndexError as error_ttt4:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 4)", error_ttt4)
    except FileNotFoundError as info_ttt4:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 4)", info_ttt4)
    else:
        ("Error unknow 4")

    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile5:
            ttt_text5 = namefile5.readline()
    except FileNotFoundError as fileout5:
        print("No file entryfile5.txt exist", fileout5)

    try:
        word_ttstop5 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file5 = open('./ttt/doc_ttt5/convdose.json')
        data5 = json.load(file5)
        for (key, value) in data5.items():
            listdata_x5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x5:
                print(str(value[x]["Date of end"]))
                date_end5 = (str(value[x]["Date of end"]))
                if date_end5 == word_ttstop5:
                    print(date_end5)
                    name_treat5 = (str(value[x]["Treatment"]))
                    print(name_treat5)
                    dose_ttt5 = (str(value[x]["Dosage"]))
                    print(dose_ttt5)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop5 + " " + \
                        'for : ' + "\n" + ttt_text5 + "Date of end : " + date_end5 + "\n" + name_treat5 + \
                        "\n" + dose_ttt5) 
    except IndexError as error_ttt5:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 5)", error_ttt5)
    except FileNotFoundError as info_ttt5:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 5)", info_ttt5)
    else:
        ("Error unknow 5")

    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile6:
            ttt_text6 = namefile6.readline()
    except FileNotFoundError as fileout6:
        print("No file entryfile6.txt exist", fileout6)

    try:
        word_ttstop6 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file6 = open('./ttt/doc_ttt6/convdose.json')
        data6 = json.load(file6)
        for (key, value) in data6.items():
            listdata_x6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x6:
                print(str(value[x]["Date of end"]))
                date_end6 = (str(value[x]["Date of end"]))
                if date_end6 == word_ttstop6:
                    print(date_end6)
                    name_treat6 = (str(value[x]["Treatment"]))
                    print(name_treat6)
                    dose_ttt6 = (str(value[x]["Dosage"]))
                    print(dose_ttt6)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop6 + " " + \
                        'for : ' + "\n" + ttt_text6 + "Date of end : " + date_end6 + "\n" + name_treat6 + \
                        "\n" + dose_ttt6) 
    except IndexError as error_ttt6:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 6)", error_ttt6)
    except FileNotFoundError as info_ttt6:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 6)", info_ttt6)
    else:
        ("Error unknow 6")

    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile7:
            ttt_text7 = namefile7.readline()
    except FileNotFoundError as fileout7:
        print("No file entryfile7.txt exist", fileout7)

    try:
        word_ttstop7 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file7 = open('./ttt/doc_ttt7/convdose.json')
        data7 = json.load(file7)
        for (key, value) in data7.items():
            listdata_x7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x7:
                print(str(value[x]["Date of end"]))
                date_end7 = (str(value[x]["Date of end"]))
                if date_end7 == word_ttstop7:
                    print(date_end7)
                    name_treat7 = (str(value[x]["Treatment"]))
                    print(name_treat7)
                    dose_ttt7 = (str(value[x]["Dosage"]))
                    print(dose_ttt7)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop7 + " " + \
                        'for : ' + "\n" + ttt_text7 + "Date of end : " + date_end7 + "\n" + name_treat7 + \
                        "\n" + dose_ttt7) 
    except IndexError as error_ttt7:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 7)", error_ttt7)
    except FileNotFoundError as info_ttt7:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 7)", info_ttt7)
    else:
        ("Error unknow 7")

    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile8:
            ttt_text8 = namefile8.readline()
    except FileNotFoundError as fileout8:
        print("No file entryfile8.txt exist", fileout8)

    try:
        word_ttstop8 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file8 = open('./ttt/doc_ttt8/convdose.json')
        data8 = json.load(file8)
        for (key, value) in data8.items():
            listdata_x8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x8:
                print(str(value[x]["Date of end"]))
                date_end8 = (str(value[x]["Date of end"]))
                if date_end8 == word_ttstop8:
                    print(date_end8)
                    name_treat8 = (str(value[x]["Treatment"]))
                    print(name_treat8)
                    dose_ttt8 = (str(value[x]["Dosage"]))
                    print(dose_ttt8)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop8 + " " + \
                        'for : ' + "\n" + ttt_text8 + "Date of end : " + date_end8 + "\n" + name_treat8 + \
                        "\n" + dose_ttt8) 
    except IndexError as error_ttt8:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 8)", error_ttt8)
    except FileNotFoundError as info_ttt8:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 8)", info_ttt8)
    else:
        ("Error unknow 8")

    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile9:
            ttt_text9 = namefile9.readline()
    except FileNotFoundError as fileout9:
        print("No file entryfile9.txt exist", fileout9)

    try:
        word_ttstop9 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file9 = open('./ttt/doc_ttt9/convdose.json')
        data9 = json.load(file9)
        for (key, value) in data9.items():
            listdata_x9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x9:
                print(str(value[x]["Date of end"]))
                date_end9 = (str(value[x]["Date of end"]))
                if date_end9 == word_ttstop9:
                    print(date_end9)
                    name_treat9 = (str(value[x]["Treatment"]))
                    print(name_treat9)
                    dose_ttt9 = (str(value[x]["Dosage"]))
                    print(dose_ttt9)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop9 + " " + \
                        'for : ' + "\n" + ttt_text9 + "Date of end : " + date_end9 + "\n" + name_treat9 + \
                        "\n" + dose_ttt9) 
    except IndexError as error_ttt9:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 9)", error_ttt9)
    except FileNotFoundError as info_ttt9:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 9)", info_ttt9)
    else:
        ("Error unknow 9")

    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile10:
            ttt_text10 = namefile10.readline()
    except FileNotFoundError as fileout10:
        print("No file entryfile10.txt exist", fileout10)

    try:
        word_ttstop10 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file10 = open('./ttt/doc_ttt10/convdose.json')
        data10 = json.load(file10)
        for (key, value) in data10.items():
            listdata_x10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x10:
                print(str(value[x]["Date of end"]))
                date_end10 = (str(value[x]["Date of end"]))
                if date_end10 == word_ttstop10:
                    print(date_end10)
                    name_treat10 = (str(value[x]["Treatment"]))
                    print(name_treat10)
                    dose_ttt10 = (str(value[x]["Dosage"]))
                    print(dose_ttt10)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop10 + " " + \
                        'for : ' + "\n" + ttt_text10 + "Date of end : " + date_end10 + "\n" + name_treat10 + \
                        "\n" + dose_ttt10) 
    except IndexError as error_ttt10:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 10)", error_ttt10)
    except FileNotFoundError as info_ttt10:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 10)", info_ttt10)
    else:
        ("Error unknow 10")

    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile11:
            ttt_text11 = namefile11.readline()
    except FileNotFoundError as fileout11:
        print("No file entryfile11.txt exist", fileout11)

    try:
        word_ttstop11 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file11 = open('./ttt/doc_ttt11/convdose.json')
        data11 = json.load(file11)
        for (key, value) in data11.items():
            listdata_x11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x11:
                print(str(value[x]["Date of end"]))
                date_end11 = (str(value[x]["Date of end"]))
                if date_end11 == word_ttstop11:
                    print(date_end11)
                    name_treat11 = (str(value[x]["Treatment"]))
                    print(name_treat11)
                    dose_ttt11 = (str(value[x]["Dosage"]))
                    print(dose_ttt11)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop11 + " " + \
                        'for : ' + "\n" + ttt_text11 + "Date of end : " + date_end11 + "\n" + name_treat11 + \
                        "\n" + dose_ttt11) 
    except IndexError as error_ttt11:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 11)", error_ttt11)
    except FileNotFoundError as info_ttt11:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 11)", info_ttt11)
    else:
        ("Error unknow 11")

    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile12:
            ttt_text12 = namefile12.readline()
    except FileNotFoundError as fileout12:
        print("No file entryfile12.txt exist", fileout12)

    try:
        word_ttstop12 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file12 = open('./ttt/doc_ttt12/convdose.json')
        data12 = json.load(file12)
        for (key, value) in data12.items():
            listdata_x12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x12:
                print(str(value[x]["Date of end"]))
                date_end12 = (str(value[x]["Date of end"]))
                if date_end12 == word_ttstop12:
                    print(date_end12)
                    name_treat12 = (str(value[x]["Treatment"]))
                    print(name_treat12)
                    dose_ttt12 = (str(value[x]["Dosage"]))
                    print(dose_ttt12)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop12 + " " + \
                        'for : ' + "\n" + ttt_text12 + "Date of end : " + date_end12 + "\n" + name_treat12 + \
                        "\n" + dose_ttt12) 
    except IndexError as error_ttt12:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 12)", error_ttt12)
    except FileNotFoundError as info_ttt12:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 12)", info_ttt12)
    else:
        ("Error unknow 12")

    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile13:
            ttt_text13 = namefile13.readline()
    except FileNotFoundError as fileout13:
        print("No file entryfile13.txt exist", fileout13)

    try:
        word_ttstop13 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file13 = open('./ttt/doc_ttt13/convdose.json')
        data13 = json.load(file13)
        for (key, value) in data13.items():
            listdata_x13 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x13:
                print(str(value[x]["Date of end"]))
                date_end13 = (str(value[x]["Date of end"]))
                if date_end13 == word_ttstop13:
                    print(date_end13)
                    name_treat13 = (str(value[x]["Treatment"]))
                    print(name_treat13)
                    dose_ttt13 = (str(value[x]["Dosage"]))
                    print(dose_ttt13)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop13 + " " + \
                        'for : ' + "\n" + ttt_text13 + "Date of end : " + date_end13 + "\n" + name_treat13 + \
                        "\n" + dose_ttt13) 
    except IndexError as error_ttt13:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 13)", error_ttt13)
    except FileNotFoundError as info_ttt13:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 13)", info_ttt13)
    else:
        ("Error unknow 13")

    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile14:
            ttt_text14 = namefile14.readline()
    except FileNotFoundError as fileout14:
        print("No file entryfile14.txt exist", fileout14)

    try:
        word_ttstop14 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file14 = open('./ttt/doc_ttt14/convdose.json')
        data14 = json.load(file14)
        for (key, value) in data14.items():
            listdata_x14 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x14:
                print(str(value[x]["Date of end"]))
                date_end14 = (str(value[x]["Date of end"]))
                if date_end14 == word_ttstop14:
                    print(date_end14)
                    name_treat14 = (str(value[x]["Treatment"]))
                    print(name_treat14)
                    dose_ttt14 = (str(value[x]["Dosage"]))
                    print(dose_ttt14)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop14 + " " + \
                        'for : ' + "\n" + ttt_text14 + "Date of end : " + date_end14 + "\n" + name_treat14 + \
                        "\n" + dose_ttt14) 
    except IndexError as error_ttt14:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 14)", error_ttt14)
    except FileNotFoundError as info_ttt14:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 14)", info_ttt14)
    else:
        ("Error unknow 14")

    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile15:
            ttt_text15 = namefile15.readline()
    except FileNotFoundError as fileout15:
        print("No file entryfile15.txt exist", fileout15)

    try:
        word_ttstop15 = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        file15 = open('./ttt/doc_ttt15/convdose.json')
        data15 = json.load(file15)
        for (key, value) in data15.items():
            listdata_x15 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            for x in listdata_x15:
                print(str(value[x]["Date of end"]))
                date_end15 = (str(value[x]["Date of end"]))
                if date_end15 == word_ttstop15:
                    print(date_end15)
                    name_treat15 = (str(value[x]["Treatment"]))
                    print(name_treat15)
                    dose_ttt15 = (str(value[x]["Dosage"]))
                    print(dose_ttt15)
                    MSBTTT2 = messagebox.showwarning('Warning',
                        'Look at TTT, there is a ttt to stop at' + " " + word_ttstop15 + " " + \
                        'for : ' + "\n" + ttt_text15 + "Date of end : " + date_end15 + "\n" + name_treat15 + \
                        "\n" + dose_ttt15) 
    except IndexError as error_ttt15:
        print("No date of end has been found for ttt into file intro_ttt.txt (patient 15)", error_ttt15)
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
        
# STOP HERE !!!
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
