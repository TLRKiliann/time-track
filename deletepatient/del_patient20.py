#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import os
import subprocess


def delFuncFile20():
    try:
        if os.path.getsize('./14besoins/doc_suivi20/main_14b.txt'):
            os.remove('./14besoins/doc_suivi20/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File main_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./14besoins/doc_suivi20/patient20_14b.txt'):
            os.remove('./14besoins/doc_suivi20/patient20_14b.txt')
            print("+ File patient20_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient20_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt20/convdose.json'):
            os.remove('./ttt/doc_ttt20/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convdose.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt20/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt20/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File intro_ttt.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt20/convres.json'):
            os.remove('./ttt/doc_ttt20/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc4:
        print("+ File convres.json does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt20/intro_res.txt'):
            os.remove('./ttt/doc_ttt20/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_res.txt does not exist", fileres5)

    try:
        if os.path.getsize('./calBmi/doc_BMI20/file_bmi.json'):
            os.remove('./calBmi/doc_BMI20/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_bmi.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/doc_BMI20/file_kg.json'):
            os.remove('./calBmi/doc_BMI20/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_kg.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/bmi20.txt'):
            os.remove('./calBmi/bmi20.txt')
            print("+ File bmi20.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi20.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./diag/doc_diag20/diagrecap.txt'):
            os.remove('./diag/doc_diag20/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File diagrecap.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./labo/doc_labo/result20.txt'):
            os.remove('./labo/doc_labo/result20.txt')
            print("+ File result20.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File result20.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events20/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File fixed_rdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events20/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File modifrdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events20/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_value.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events20/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events20/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_rdv.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events20/patient_calendar.txt'):
            os.remove('./patient_agenda/events20/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_calendar.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./allergy/allergyfile20.txt'):
            os.remove('./allergy/allergyfile20.txt')
            print("+ File allergyfile20.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File allergyfile20.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'w') as file:
                file.write("--------------------")
            print("+ File entryfile20.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile20.txt does not exist", filefunc28)
    print("!!! All files have been deleted !!!")
    