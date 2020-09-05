#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import time
import datetime


def treatmentFunc(self):
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

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt8/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             8 which is stopped today!')
    except FileNotFoundError as info_ttt8:
        print("No date of end has been found for ttt into file convdose.json (patient 8)", info_ttt8)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt9/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             9 which is stopped today!')
    except FileNotFoundError as info_ttt9:
        print("No date of end has been found for ttt into file convdose.json (patient 9)", info_ttt9)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt10/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             10 which is stopped today!')
    except FileNotFoundError as info_ttt10:
        print("No date of end has been found for ttt into file convdose.json (patient 10)", info_ttt10)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt11/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             11 which is stopped today!')
    except FileNotFoundError as info_ttt11:
        print("No date of end has been found for ttt into file convdose.json (patient 11)", info_ttt11)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt12/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             12 which is stopped today!')
    except FileNotFoundError as info_ttt12:
        print("No date of end has been found for ttt into file convdose.json (patient 12)", info_ttt12)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt13/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             13 which is stopped today!')
    except FileNotFoundError as info_ttt13:
        print("No date of end has been found for ttt into file convdose.json (patient 13)", info_ttt13)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt14/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             14 which is stopped today!')
    except FileNotFoundError as info_ttt14:
        print("No date of end has been found for ttt into file convdose.json (patient 14)", info_ttt14)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt15/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             15 which is stopped today!')
    except FileNotFoundError as info_ttt15:
        print("No date of end has been found for ttt into file convdose.json (patient 15)", info_ttt15)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt16/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             16 which is stopped today!')
    except FileNotFoundError as info_ttt16:
        print("No date of end has been found for ttt into file convdose.json (patient 16)", info_ttt16)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt17/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             17 which is stopped today!')
    except FileNotFoundError as info_ttt17:
        print("No date of end has been found for ttt into file convdose.json (patient 17)", info_ttt17)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt18/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             18 which is stopped today!')
    except FileNotFoundError as info_ttt18:
        print("No date of end has been found for ttt into file convdose.json (patient 18)", info_ttt18)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt19/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             19 which is stopped today!')
    except FileNotFoundError as info_ttt19:
        print("No date of end has been found for ttt into file convdose.json (patient 19)", info_ttt19)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt20/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             20 which is stopped today!')
    except FileNotFoundError as info_ttt20:
        print("No date of end has been found for ttt into file convdose.json (patient 20)", info_ttt20)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt21/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             21 which is stopped today!')
    except FileNotFoundError as info_ttt21:
        print("No date of end has been found for ttt into file convdose.json (patient 21)", info_ttt21)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt22/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             22 which is stopped today!')
    except FileNotFoundError as info_ttt22:
        print("No date of end has been found for ttt into file convdose.json (patient 22)", info_ttt22)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt23/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             23 which is stopped today!')
    except FileNotFoundError as info_ttt23:
        print("No date of end has been found for ttt into file convdose.json (patient 23)", info_ttt23)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        initword = "Date of end : "
        with open('./ttt/doc_ttt24/convdose.json', 'r') as filedate:
            lines = filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBTTT2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a ttt for patient \
                             24 which is stopped today!')
    except FileNotFoundError as info_ttt24:
        print("No date of end has been found for ttt into file convdose.json (patient 24)", info_ttt24)
    else:
        ("Error unknow")

def reserveFunc(self):
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

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt8/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 8 which is stopped today!')
    except FileNotFoundError as info_res8:
        print("No date of end has been found for reserve into file convres.json (patient 8)", info_res8)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt9/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 9 which is stopped today!')
    except FileNotFoundError as info_res9:
        print("No date of end has been found for reserve into file convres.json (patient 9)", info_res9)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt10/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 10 which is stopped today!')
    except FileNotFoundError as info_res10:
        print("No date of end has been found for reserve into file convres.json (patient 10)", info_res10)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt11/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 11 which is stopped today!')
    except FileNotFoundError as info_res11:
        print("No date of end has been found for reserve into file convres.json (patient 11)", info_res11)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt12/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 12 which is stopped today!')
    except FileNotFoundError as info_res12:
        print("No date of end has been found for reserve into file convres.json (patient 12)", info_res12)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt13/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 13 which is stopped today!')
    except FileNotFoundError as info_res13:
        print("No date of end has been found for reserve into file convres.json (patient 13)", info_res13)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt14/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 14 which is stopped today!')
    except FileNotFoundError as info_res14:
        print("No date of end has been found for reserve into file convres.json (patient 14)", info_res14)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt15/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 15 which is stopped today!')
    except FileNotFoundError as info_res15:
        print("No date of end has been found for reserve into file convres.json (patient 15)", info_res15)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt16/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 16 which is stopped today!')
    except FileNotFoundError as info_res16:
        print("No date of end has been found for reserve into file convres.json (patient 16)", info_res16)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt17/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 17 which is stopped today!')
    except FileNotFoundError as info_res17:
        print("No date of end has been found for reserve into file convres.json (patient 17)", info_res17)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt18/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 18 which is stopped today!')
    except FileNotFoundError as info_res18:
        print("No date of end has been found for reserve into file convres.json (patient 18)", info_res18)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt19/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 19 which is stopped today!')
    except FileNotFoundError as info_res19:
        print("No date of end has been found for reserve into file convres.json (patient 19)", info_res19)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt20/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 20 which is stopped today!')
    except FileNotFoundError as info_res20:
        print("No date of end has been found for reserve into file convres.json (patient 20)", info_res20)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt21/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 21 which is stopped today!')
    except FileNotFoundError as info_res21:
        print("No date of end has been found for reserve into file convres.json (patient 21)", info_res21)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt22/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 22 which is stopped today!')
    except FileNotFoundError as info_res22:
        print("No date of end has been found for reserve into file convres.json (patient 22)", info_res22)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt23/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 23 which is stopped today!')
    except FileNotFoundError as info_res23:
        print("No date of end has been found for reserve into file convres.json (patient 23)", info_res23)
    else:
        ("Error unknow")

    try:
        dateagenda = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt24/conv_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if dateagenda in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at RESERVE onto TTT, there is a RESERVE \
                             for patient 24 which is stopped today!')
    except FileNotFoundError as info_res24:
        print("No date of end has been found for reserve into file convres.json (patient 24)", info_res24)
    else:
        ("Error unknow")
