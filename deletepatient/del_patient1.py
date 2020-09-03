#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import subprocess


def delFuncFile1():
    try:
        if os.path.getsize('./14besoins/doc_suivi/main_14b.txt'):
            os.remove('./14besoins/doc_suivi/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc2:
        print("+ File main_14b.txt does not exist", filefunc2)

    try:
        if os.path.getsize('./14besoins/doc_suivi/patient1_14b.txt'):
            os.remove('./14besoins/doc_suivi/patient1_14b.txt')
            print("+ File patient1_14b.txt deleted")
    except FileNotFoundError as filefunc3:
        print("+ File patient1_14b.txt does not exist", filefunc3)

    try:
        if os.path.getsize('./ttt/doc_ttt/convdose.json'):
            os.remove('./ttt/doc_ttt/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc4:
        print("+ File convdose.json does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_ttt.txt does not exist", filefunc5)

    try:
        if os.path.getsize('./ttt/doc_ttt/convres.json'):
            os.remove('./ttt/doc_ttt/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc61:
        print("+ File convres.json does not exist", filefunc61)

    try:
        if os.path.getsize('./ttt/doc_ttt/intro_res.txt'):
            os.remove('./ttt/doc_ttt/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc62:
        print("+ File intro_res.txt does not exist", filefunc62)

    try:
        if os.path.getsize('./calBmi/doc_BMI/file_bmi.json'):
            os.remove('./calBmi/doc_BMI/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc14:
        print("+ File file_bmi.json does not exist", filefunc14)

    try:
        if os.path.getsize('./calBmi/doc_BMI/file_kg.json'):
            os.remove('./calBmi/doc_BMI/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc15:
        print("+ File file_kg.json does not exist", filefunc15)

    try:
        if os.path.getsize('./calBmi/bmi.txt'):
            os.remove('./calBmi/bmi.txt')
            print("+ File bmi.txt deleted")
    except FileNotFoundError as filefunc16:
        print("+ File bmi.txt does not exist", filefunc16)

    try:
        if os.path.getsize('./diag/doc_diag/diagrecap.txt'):
            os.remove('./diag/doc_diag/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc18:
        print("+ File diagrecap.txt does not exist", filefunc18)

    try:
        if os.path.getsize('./labo/doc_labo/result.txt'):
            os.remove('./labo/doc_labo/result.txt')
            print("+ File result.txt deleted")
    except FileNotFoundError as filefunc19:
        print("+ File result.txt does not exist", filefunc19)

    try:
        if os.path.getsize('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc22:
        print("+ File fixed_rdv.txt does not exist", filefunc22)

    try:
        if os.path.getsize('./patient_agenda/events/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc23:
        print("+ File modifrdv.txt does not exist", filefunc23)

    try:
        if os.path.getsize('./patient_agenda/events/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc24:
        print("+ File patient_value.json does not exist", filefunc24)

    try:
        if os.path.getsize('./patient_agenda/events/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc25:
        print("+ File patient_rdv.json does not exist", filefunc25)

    try:
        if os.path.getsize('./patient_agenda/events/patient_calendar.txt'):
            os.remove('./patient_agenda/events/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc26:
        print("+ File patient_calendar.txt does not exist", filefunc26)

    try:
        if os.path.getsize('./allergy/allergyfile.txt'):
            os.remove('./allergy/allergyfile.txt')
            print("+ File allergyfile.txt deleted")
    except FileNotFoundError as filefunc27:
        print("+ File allergyfile.txt does not exist", filefunc27)

    try:
        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'w') as file:
                file.write("-")
            print("+ File entryfile.txt reborn")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile.txt does not exist", filefunc28)
    print("!!! All files have been deleted !!!")
