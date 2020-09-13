#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os
import time
import datetime


def dispResFunc():
    """
    To search the end date into the intro_res.txt 
    and display alert to stop reserve !
    """
    # Patient 1
    try:
        with open('./newpatient/entryfile.txt', 'r') as namefile:
            res_text1=namefile.readline()
    except FileNotFoundError as callfile:
        print("File entryfile.txt doesn't exist !", callfile)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text1)
    except FileNotFoundError as info_res1:
        print("No date of end has been found for reserve into file convres.json (patient 1)", info_res1)
    else:
        ("Error unknow")

    # Patient 2
    try:
        with open('./newpatient/entryfile2.txt', 'r') as namefile:
            res_text2=namefile.readline()
    except FileNotFoundError as callfile2:
        print("File entryfile2.txt doesn't exist !", callfile2)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt2/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text2)
    except FileNotFoundError as info_res2:
        print("No date of end has been found for reserve into file convres.json (patient 2)", info_res2)
    else:
        ("Error unknow")

    # Patient 3
    try:
        with open('./newpatient/entryfile3.txt', 'r') as namefile:
            res_text3=namefile.readline()
    except FileNotFoundError as callfile3:
        print("File entryfile3.txt doesn't exist !", callfile3)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt3/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text3)
    except FileNotFoundError as info_res3:
        print("No date of end has been found for reserve into file convres.json (patient 3)", info_res3)
    else:
        ("Error unknow")

    # Patient 4
    try:
        with open('./newpatient/entryfile4.txt', 'r') as namefile:
            res_text4=namefile.readline()
    except FileNotFoundError as callfile4:
        print("File entryfile4.txt doesn't exist !", callfile4)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt4/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text4)
    except FileNotFoundError as info_res4:
        print("No date of end has been found for reserve into file convres.json (patient 4)", info_res4)
    else:
        ("Error unknow")

    # Patient 5
    try:
        with open('./newpatient/entryfile5.txt', 'r') as namefile:
            res_text5=namefile.readline()
    except FileNotFoundError as callfile5:
        print("File entryfile5.txt doesn't exist !", callfile5)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt5/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text5)
    except FileNotFoundError as info_res5:
        print("No date of end has been found for reserve into file convres.json (patient 5)", info_res5)
    else:
        ("Error unknow")

    # Patient 6
    try:
        with open('./newpatient/entryfile6.txt', 'r') as namefile:
            res_text6=namefile.readline()
    except FileNotFoundError as callfile6:
        print("File entryfile6.txt doesn't exist !", callfile6)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt6/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text6)
    except FileNotFoundError as info_res6:
        print("No date of end has been found for reserve into file convres.json (patient 6)", info_res6)
    else:
        ("Error unknow")

    # Patient 7
    try:
        with open('./newpatient/entryfile7.txt', 'r') as namefile:
            res_text7=namefile.readline()
    except FileNotFoundError as callfile7:
        print("File entryfile7.txt doesn't exist !", callfile7)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt7/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text7)
    except FileNotFoundError as info_res7:
        print("No date of end has been found for reserve into file convres.json (patient 7)", info_res7)
    else:
        ("Error unknow")

    # Patient 8
    try:
        with open('./newpatient/entryfile8.txt', 'r') as namefile:
            res_text8=namefile.readline()
    except FileNotFoundError as callfile8:
        print("File entryfile8.txt doesn't exist !", callfile8)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt8/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text8)
    except FileNotFoundError as info_res8:
        print("No date of end has been found for reserve into file convres.json (patient 8)", info_res8)
    else:
        ("Error unknow")

    # Patient 9
    try:
        with open('./newpatient/entryfile9.txt', 'r') as namefile:
            res_text9=namefile.readline()
    except FileNotFoundError as callfile9:
        print("File entryfile9.txt doesn't exist !", callfile9)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt9/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text9)
    except FileNotFoundError as info_res9:
        print("No date of end has been found for reserve into file convres.json (patient 9)", info_res9)
    else:
        ("Error unknow")

    # Patient 10
    try:
        with open('./newpatient/entryfile10.txt', 'r') as namefile:
            res_text10=namefile.readline()
    except FileNotFoundError as callfile10:
        print("File entryfile10.txt doesn't exist !", callfile10)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt10/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text10) 
    except FileNotFoundError as info_res10:
        print("No date of end has been found for reserve into file convres.json (patient 10)", info_res10)
    else:
        ("Error unknow")

    # Patient 11
    try:
        with open('./newpatient/entryfile11.txt', 'r') as namefile:
            res_text11=namefile.readline()
    except FileNotFoundError as callfile11:
        print("File entryfile11.txt doesn't exist !", callfile11)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt11/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text11) 
    except FileNotFoundError as info_res11:
        print("No date of end has been found for reserve into file convres.json (patient 11)", info_res11)
    else:
        ("Error unknow")

    # Patient 12
    try:
        with open('./newpatient/entryfile12.txt', 'r') as namefile:
            res_text12=namefile.readline()
    except FileNotFoundError as callfile12:
        print("File entryfile12.txt doesn't exist !", callfile12)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt12/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text12) 
    except FileNotFoundError as info_res12:
        print("No date of end has been found for reserve into file convres.json (patient 12)", info_res12)
    else:
        ("Error unknow")

    # Patient 13
    try:
        with open('./newpatient/entryfile13.txt', 'r') as namefile:
            res_text13=namefile.readline()
    except FileNotFoundError as callfile13:
        print("File entryfile13.txt doesn't exist !", callfile13)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt13/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text13) 
    except FileNotFoundError as info_res13:
        print("No date of end has been found for reserve into file convres.json (patient 13)", info_res13)
    else:
        ("Error unknow")

    # Patient 14
    try:
        with open('./newpatient/entryfile14.txt', 'r') as namefile:
            res_text14=namefile.readline()
    except FileNotFoundError as callfile14:
        print("File entryfile14.txt doesn't exist !", callfile14)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt14/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text14) 
    except FileNotFoundError as info_res14:
        print("No date of end has been found for reserve into file convres.json (patient 14)", info_res14)
    else:
        ("Error unknow")

    # Patient 15
    try:
        with open('./newpatient/entryfile15.txt', 'r') as namefile:
            res_text15=namefile.readline()
    except FileNotFoundError as callfile15:
        print("File entryfile15.txt doesn't exist !", callfile15)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt15/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text15) 
    except FileNotFoundError as info_res15:
        print("No date of end has been found for reserve into file convres.json (patient 15)", info_res15)
    else:
        ("Error unknow")

    # Patient 16
    try:
        with open('./newpatient/entryfile16.txt', 'r') as namefile:
            res_text16=namefile.readline()
    except FileNotFoundError as callfile16:
        print("File entryfile16.txt doesn't exist !", callfile16)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt16/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text16)
    except FileNotFoundError as info_res16:
        print("No date of end has been found for reserve into file convres.json (patient 16)", info_res16)
    else:
        ("Error unknow")

    # Patient 17
    try:
        with open('./newpatient/entryfile17.txt', 'r') as namefile:
            res_text17=namefile.readline()
    except FileNotFoundError as callfile17:
        print("File entryfile17.txt doesn't exist !", callfile17)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt17/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text17)
    except FileNotFoundError as info_res17:
        print("No date of end has been found for reserve into file convres.json (patient 17)", info_res17)
    else:
        ("Error unknow")

    # Patient 18
    try:
        with open('./newpatient/entryfile18.txt', 'r') as namefile:
            res_text18=namefile.readline()
    except FileNotFoundError as callfile18:
        print("File entryfile18.txt doesn't exist !", callfile18)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt18/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text18)
    except FileNotFoundError as info_res18:
        print("No date of end has been found for reserve into file convres.json (patient 18)", info_res18)
    else:
        ("Error unknow")

    # Patient 19
    try:
        with open('./newpatient/entryfile19.txt', 'r') as namefile:
            res_text19=namefile.readline()
    except FileNotFoundError as callfile19:
        print("File entryfile19.txt doesn't exist !", callfile19)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt19/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text19)
    except FileNotFoundError as info_res19:
        print("No date of end has been found for reserve into file convres.json (patient 19)", info_res19)
    else:
        ("Error unknow")

    # Patient 20
    try:
        with open('./newpatient/entryfile20.txt', 'r') as namefile:
            res_text20=namefile.readline()
    except FileNotFoundError as callfile20:
        print("File entryfile20.txt doesn't exist !", callfile20)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt20/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text20)
    except FileNotFoundError as info_res20:
        print("No date of end has been found for reserve into file convres.json (patient 20)", info_res20)
    else:
        ("Error unknow")

    # Patient 21
    try:
        with open('./newpatient/entryfile21.txt', 'r') as namefile:
            res_text21=namefile.readline()
    except FileNotFoundError as callfile21:
        print("File entryfile21.txt doesn't exist !", callfile21)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt21/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text21)
    except FileNotFoundError as info_res21:
        print("No date of end has been found for reserve into file convres.json (patient 21)", info_res21)
    else:
        ("Error unknow")

    # Patient 22
    try:
        with open('./newpatient/entryfile22.txt', 'r') as namefile:
            res_text22=namefile.readline()
    except FileNotFoundError as callfile22:
        print("File entryfile22.txt doesn't exist !", callfile22)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt22/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text22)
    except FileNotFoundError as info_res22:
        print("No date of end has been found for reserve into file convres.json (patient 22)", info_res22)
    else:
        ("Error unknow")

    # Patient 23
    try:
        with open('./newpatient/entryfile23.txt', 'r') as namefile:
            res_text23=namefile.readline()
    except FileNotFoundError as callfile23:
        print("File entryfile23.txt doesn't exist !", callfile23)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt23/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text23)
    except FileNotFoundError as info_res23:
        print("No date of end has been found for reserve into file convres.json (patient 23)", info_res23)
    else:
        ("Error unknow")

    # Patient 24
    try:
        with open('./newpatient/entryfile24.txt', 'r') as namefile:
            res_text24=namefile.readline()
    except FileNotFoundError as callfile24:
        print("File entryfile24.txt doesn't exist !", callfile24)

    try:
        word_treattostop = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        res_initword = "Date of end : "
        with open('./ttt/doc_ttt24/intro_res.txt', 'r') as filedate:
            lines=filedate.readlines()
            for i in range(0, len(lines)):
                line = lines[i]
                if res_initword in line:
                    print(line)
                    if word_treattostop in line:
                        print(line)
                        MSBRES2 = messagebox.showwarning('Info',
                            'Look at TTT, there is a reserve to stop tomorrow for : ' + res_text24)
    except FileNotFoundError as info_res24:
        print("No date of end has been found for reserve into file convres.json (patient 24)", info_res24)
    else:
        ("Error unknow")
