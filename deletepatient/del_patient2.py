#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import subprocess


def delFuncFile2():
    try:
        if os.path.getsize('./14besoins/doc_suivi2/main_14b.txt'):
            os.remove('./14besoins/doc_suivi2/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc1:
        print("+ File main_14b.txt does not exist", filefunc1)

    try:
        if os.path.getsize('./14besoins/doc_suivi2/patient2_14b.txt'):
            os.remove('./14besoins/doc_suivi2/patient2_14b.txt')
            print("+ File patient2_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File patient2_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./ttt/doc_ttt2/convdose.json'):
            os.remove('./ttt/doc_ttt2/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc3:
        print("+ File convdose.json does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt2/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt2/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc4:
        print("+ File intro_ttt.txt does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt2/convres.json'):
            os.remove('./ttt/doc_ttt2/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc5:
        print("+ File convres.json does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt2/intro_res.txt'):
            os.remove('./ttt/doc_ttt2/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc6:
        print("+ File intro_res.txt does not exist", filefunc6)

    try:
        if os.path.getsize('./calBmi/doc_BMI2/file_bmi.json'):
            os.remove('./calBmi/doc_BMI2/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc7:
        print("+ File file_bmi.json does not exist", filefunc7)

    try:
        if os.path.getsize('./calBmi/doc_BMI2/file_kg.json'):
            os.remove('./calBmi/doc_BMI2/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc8:
        print("+ File file_kg.json does not exist", filefunc8)

    try:
        if os.path.getsize('./calBmi/bmi2.txt'):
            os.remove('./calBmi/bmi2.txt')
            print("+ File bmi2.txt deleted")
    except FileNotFoundError as filefunc9:
        print("+ File bmi2.txt does not exist", filefunc9)

    try:
        if os.path.getsize('./diag/doc_diag2/diagrecap.txt'):
            os.remove('./diag/doc_diag2/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc10:
        print("+ File diagrecap.txt does not exist", filefunc10)

    try:
        if os.path.getsize('./labo/doc_labo/result2.txt'):
            os.remove('./labo/doc_labo/result2.txt')
            print("+ File result2.txt deleted")
    except FileNotFoundError as filefunc11:
        print("+ File result2.txt does not exist", filefunc11)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc12:
        print("+ File fixed_rdv.txt does not exist", filefunc12)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc13:
        print("+ File modifrdv.txt does not exist", filefunc13)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File patient_value.json does not exist", filefunc14)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events2/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File patient_rdv.json does not exist", filefunc15)

    try:
        if os.path.getsize('./patient_agenda/events2/patient_calendar.txt'):
            os.remove('./patient_agenda/events2/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File patient_calendar.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./allergy/allergyfile2.txt'):
            os.remove('./allergy/allergyfile2.txt')
            print("+ File allergyfile2.txt deleted")
    except FileNotFoundError as filefunc17:
        print("+ File allergyfile2.txt does not exist", filefunc17)

    try:
        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'w') as file:
                file.write("--")
            print("+ File entryfile2.txt reborn")
    except FileNotFoundError as filefunc18:
        print("+ File entryfile2.txt not exist", filefunc18)
    print("!!! All files have been deleted !!!")
    