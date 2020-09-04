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
