#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from tkinter import messagebox
import os


def get(Nompatient, entree):
    MsgBox = messagebox.askyesno('Save data', 'Do you want to delete ?')
    if MsgBox == 1:
        Nompatient = entree.get()
        print(Nompatient)
        if os.path.getsize('./newpatient/entryfile.txt'):
            with open('./newpatient/entryfile.txt', 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile1()
                    else:
                        print("Patient's Name does not exist")

        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'r') as file2:
                lines = file2.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile2()
                    else:
                        print("Patient's Name does not exist")

        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'r') as file3:
                lines = file3.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile3()
                    else:
                        print("Patient's Name does not exist")

        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'r') as file4:
                lines = file4.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile4()
                    else:
                        print("Patient's Name does not exist")

        if os.path.getsize('./newpatient/entryfile5.txt'):
            with open('./newpatient/entryfile5.txt', 'r') as file5:
                lines = file5.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile5()
                    else:
                        print("Patient's Name does not exist")

        if os.path.getsize('./newpatient/entryfile6.txt'):
            with open('./newpatient/entryfile6.txt', 'r') as file6:
                lines = file6.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile6()
                    else:
                        print("Patient's Name does not exist")

        if os.path.getsize('./newpatient/entryfile7.txt'):
            with open('./newpatient/entryfile7.txt', 'r') as file7:
                lines = file7.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile7()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile8.txt'):
            with open('./newpatient/entryfile8.txt', 'r') as file8:
                lines = file8.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile8()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile9.txt'):
            with open('./newpatient/entryfile9.txt', 'r') as file9:
                lines = file9.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile9()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile10.txt'):
            with open('./newpatient/entryfile10.txt', 'r') as file10:
                lines = file10.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile10()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile11.txt'):
            with open('./newpatient/entryfile11.txt', 'r') as file11:
                lines = file11.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile11()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile12.txt'):
            with open('./newpatient/entryfile12.txt', 'r') as file12:
                lines = file12.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile12()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile13.txt'):
            with open('./newpatient/entryfile13.txt', 'r') as file13:
                lines = file13.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile13()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile14.txt'):
            with open('./newpatient/entryfile14.txt', 'r') as file14:
                lines = file14.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile14()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile15.txt'):
            with open('./newpatient/entryfile15.txt', 'r') as file15:
                lines = file15.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile15()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile16.txt'):
            with open('./newpatient/entryfile16.txt', 'r') as file16:
                lines = file16.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile16()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile17.txt'):
            with open('./newpatient/entryfile17.txt', 'r') as file17:
                lines = file17.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile17()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile18.txt'):
            with open('./newpatient/entryfile18.txt', 'r') as file18:
                lines = file18.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile18()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile19.txt'):
            with open('./newpatient/entryfile19.txt', 'r') as file19:
                lines = file19.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile19()          
                    else:
                        print("End of test delete files.")

        if os.path.getsize('./newpatient/entryfile20.txt'):
            with open('./newpatient/entryfile20.txt', 'r') as file20:
                lines = file20.readlines()
                for i in range(0, len(lines)):
                    line = lines[i]
                    if Nompatient in line:
                        delFuncFile20()          
                    else:
                        print("End of test delete files.")
    else:           
        NoforQ = messagebox.showinfo('Return', 'None file was found !')

    gui.destroy()

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

def delFuncFile2():
    try:
        if os.path.getsize('./14besoins/doc_suivi2/main_14b.txt'):
            os.remove('./14besoins/doc_suivi2/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File main_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./14besoins/doc_suivi2/patient2_14b.txt'):
            os.remove('./14besoins/doc_suivi2/patient2_14b.txt')
            print("+ File patient2_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient2_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt2/convdose.json'):
            os.remove('./ttt/doc_ttt2/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convdose.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt2/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt2/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File intro_ttt.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt2/convres.json'):
            os.remove('./ttt/doc_ttt2/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc4:
        print("+ File convres.json does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt2/intro_res.txt'):
            os.remove('./ttt/doc_ttt2/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_res.txt does not exist", fileres5)

    try:
        if os.path.getsize('./calBmi/doc_BMI2/file_bmi.json'):
            os.remove('./calBmi/doc_BMI2/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_bmi.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/doc_BMI2/file_kg.json'):
            os.remove('./calBmi/doc_BMI2/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_kg.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/bmi2.txt'):
            os.remove('./calBmi/bmi2.txt')
            print("+ File bmi2.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi2.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./diag/doc_diag2/diagrecap.txt'):
            os.remove('./diag/doc_diag2/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File diagrecap.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./labo/doc_labo/result2.txt'):
            os.remove('./labo/doc_labo/result2.txt')
            print("+ File result2.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File result2.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File fixed_rdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File modifrdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events2/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_value.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events2/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events2/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_rdv.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events2/patient_calendar.txt'):
            os.remove('./patient_agenda/events2/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_calendar.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./allergy/allergyfile2.txt'):
            os.remove('./allergy/allergyfile2.txt')
            print("+ File allergyfile2.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File allergyfile2.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./newpatient/entryfile2.txt'):
            with open('./newpatient/entryfile2.txt', 'w') as file:
                file.write("--")
            print("+ File entryfile2.txt reborn")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile2.txt not exist", filefunc28)
    print("!!! All files have been deleted !!!")

def delFuncFile3():
    try:
        if os.path.getsize('./14besoins/doc_suivi3/main_14b.txt'):
            os.remove('./14besoins/doc_suivi3/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File main_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./14besoins/doc_suivi3/patient3_14b.txt'):
            os.remove('./14besoins/doc_suivi3/patient3_14b.txt')
            print("+ File patient3_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient3_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt3/convdose.json'):
            os.remove('./ttt/doc_ttt3/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convdose.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt3/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt3/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File intro_ttt.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt3/convres.json'):
            os.remove('./ttt/doc_ttt3/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc4:
        print("+ File convres.json does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt3/intro_res.txt'):
            os.remove('./ttt/doc_ttt3/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_res.txt does not exist", fileres5)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/file_bmi.json'):
            os.remove('./calBmi/doc_BMI3/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_bmi.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/doc_BMI3/file_kg.json'):
            os.remove('./calBmi/doc_BMI3/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_kg.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/bmi3.txt'):
            os.remove('./calBmi/bmi3.txt')
            print("+ File bmi3.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi3.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./diag/doc_diag3/diagrecap.txt'):
            os.remove('./diag/doc_diag3/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File diagrecap.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./labo/doc_labo/result3.txt'):
            os.remove('./labo/doc_labo/result3.txt')
            print("+ File result3.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File result3.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File fixed_rdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File modifrdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events3/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_value.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events3/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events3/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_rdv.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events3/patient_calendar.txt'):
            os.remove('./patient_agenda/events3/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_calendar.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./allergy/allergyfile3.txt'):
            os.remove('./allergy/allergyfile3.txt')
            print("+ File allergyfile3.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File allergyfile3.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./newpatient/entryfile3.txt'):
            with open('./newpatient/entryfile3.txt', 'w') as file:
                file.write("---")
            print("+ File entryfile3.txt reborn")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile3.txt does not exist", filefunc28)
    print("!!! All files have been deleted !!!")

def delFuncFile4():
    try:
        if os.path.getsize('./14besoins/doc_suivi4/main_14b.txt'):
            os.remove('./14besoins/doc_suivi4/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File main_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./14besoins/doc_suivi4/patient4_14b.txt'):
            os.remove('./14besoins/doc_suivi4/patient4_14b.txt')
            print("+ File patient4_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient4_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt4/convdose.json'):
            os.remove('./ttt/doc_ttt4/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convdose.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt4/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt4/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File intro_ttt.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt4/convres.json'):
            os.remove('./ttt/doc_ttt4/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc4:
        print("+ File convres.json does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt4/intro_res.txt'):
            os.remove('./ttt/doc_ttt4/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_res.txt does not exist", fileres5)

    try:
        if os.path.getsize('./calBmi/doc_BMI4/file_bmi.json'):
            os.remove('./calBmi/doc_BMI4/file_bmi.json')
            print("+ File bmi.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/doc_BMI4/file_kg.json'):
            os.remove('./calBmi/doc_BMI4/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_kg.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/bmi4.txt'):
            os.remove('./calBmi/bmi4.txt')
            print("+ File bmi4.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi4.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./diag/doc_diag4/diagrecap.txt'):
            os.remove('./diag/doc_diag4/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File diagrecap.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./labo/doc_labo/result4.txt'):
            os.remove('./labo/doc_labo/result4.txt')
            print("+ File result4.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File result4.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events4/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File fixed_rdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events4/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File modifrdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_value.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events4/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events4/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_rdv does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events4/patient_calendar.txt'):
            os.remove('./patient_agenda/events4/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_calendar.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./allergy/allergyfile4.txt'):
            os.remove('./allergy/allergyfile4.txt')
            print("+ File allergyfile4.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File allergyfile4.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./newpatient/entryfile4.txt'):
            with open('./newpatient/entryfile4.txt', 'w') as file:
                file.write("----")
            print("+ File entryfile4.txt reborn")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile4.txt does not exist", filefunc28)
    print("!!! All files have been deleted !!!")

def delFuncFile5():
    try:
        if os.path.getsize('./14besoins/doc_suivi5/main_14b.txt'):
            os.remove('./14besoins/doc_suivi5/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File main_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./14besoins/doc_suivi5/patient5_14b.txt'):
            os.remove('./14besoins/doc_suivi5/patient5_14b.txt')
            print("+ File patient5_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient5_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt5/convdose.json'):
            os.remove('./ttt/doc_ttt5/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convdose.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt5/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt5/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File intro_ttt.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt5/convres.json'):
            os.remove('./ttt/doc_ttt5/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convres.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt5/intro_res.txt'):
            os.remove('./ttt/doc_ttt5/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_res.txt does not exist", filefunc5)

    try:
        if os.path.getsize('./calBmi/doc_BMI5/file_bmi.json'):
            os.remove('./calBmi/doc_BMI5/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_bmi.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/doc_BMI5/file_kg.json'):
            os.remove('./calBmi/doc_BMI5/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_kg.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/bmi5.txt'):
            os.remove('./calBmi/bmi5.txt')
            print("+ File bmi5.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi5.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./diag/doc_diag5/diagrecap.txt'):
            os.remove('./diag/doc_diag5/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File diagrecap.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./labo/doc_labo/result5.txt'):
            os.remove('./labo/doc_labo/result5.txt')
            print("+ File result5.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File result5.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events5/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events5/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File fixed_rdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events5/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events5/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File modifrdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events5/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events5/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_value.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events5/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events5/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_rdv.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events5/patient_calendar.txt'):
            os.remove('./patient_agenda/events5/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_calendar.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./allergy/allergyfile5.txt'):
            os.remove('./allergy/allergyfile5.txt')
            print("+ File allergyfile5.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File allergyfile5.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./newpatient/entryfile5.txt'):
            with open('./newpatient/entryfile5.txt', 'w') as file:
                file.write("-----")
            print("+ File entryfile5.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile5.txt does not exist", filefunc28)
    print("!!! All files have been deleted !!!")

def delFuncFile6():
    try:
        if os.path.getsize('./14besoins/doc_suivi6/main_14b.txt'):
            os.remove('./14besoins/doc_suivi6/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File main_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize :
            os.remove('./14besoins/doc_suivi6/patient6_14b.txt')
            print("+ File patient6_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient6_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt6/convdose.json'):
            os.remove('./ttt/doc_ttt6/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convdose.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt6/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt6/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File intro_ttt.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt6/convres.json'):
            os.remove('./ttt/doc_ttt6/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc4:
        print("+ File convres.json does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt6/intro_res.txt'):
            os.remove('./ttt/doc_ttt6/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_res.txt does not exist", fileres5)

    try:
        if os.path.getsize('./calBmi/doc_BMI6/file_bmi.json'):
            os.remove('./calBmi/doc_BMI6/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_bmi.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/doc_BMI6/file_kg.json'):
            os.remove('./calBmi/doc_BMI6/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_kg.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/bmi6.txt'):
            os.remove('./calBmi/bmi6.txt')
            print("+ File bmi6.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi6.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./diag/doc_diag6/diagrecap.txt'):
            os.remove('./diag/doc_diag6/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File diagrecap.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./labo/doc_labo/result6.txt'):
            os.remove('./labo/doc_labo/result6.txt')
            print("+ File result6.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File result6.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events6/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File fixed_rdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events6/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events6/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File modifrdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events6/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events6/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_value.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events6/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events6/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_rdv.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events6/patient_calendar.txt'):
            os.remove('./patient_agenda/events6/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_calendar.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./allergy/allergyfile6.txt'):
            os.remove('./allergy/allergyfile6.txt')
            print("+ File allergyfile6 deleted")
    except FileNotFoundError as filefunc28:
        print("+ File allergyfile6 does not exist", filefunc28)

    try:
        if os.path.getsize('./newpatient/entryfile6.txt'):
            with open('./newpatient/entryfile6.txt', 'w') as file:
                file.write("------")
            print("+ File entryfile6.txt reborn")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile6.txt does not exist", filefunc28)
    print("!!! All files have been deleted !!!")

def delFuncFile7():
    try:
        if os.path.getsize('./14besoins/doc_suivi7/main_14b.txt'):
            os.remove('./14besoins/doc_suivi7/main_14b.txt')
            print("+ File main_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File main_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./14besoins/doc_suivi7/patient7_14b.txt'):
            os.remove('./14besoins/doc_suivi7/patient7_14b.txt')
            print("+ File patient7_14b.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient7_14b.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt7/convdose.json'):
            os.remove('./ttt/doc_ttt7/convdose.json')
            print("+ File convdose.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File convdose.json does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt7/intro_ttt.txt'):
            os.remove('./ttt/doc_ttt7/intro_ttt.txt')
            print("+ File intro_ttt.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File intro_ttt.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./ttt/doc_ttt7/convres.json'):
            os.remove('./ttt/doc_ttt7/convres.json')
            print("+ File convres.json deleted")
    except FileNotFoundError as filefunc4:
        print("+ File convres.json does not exist", filefunc4)

    try:
        if os.path.getsize('./ttt/doc_ttt7/intro_res.txt'):
            os.remove('./ttt/doc_ttt7/intro_res.txt')
            print("+ File intro_res.txt deleted")
    except FileNotFoundError as filefunc5:
        print("+ File intro_res.txt does not exist", fileres5)

    try:
        if os.path.getsize('./calBmi/doc_BMI7/file_bmi.json'):
            os.remove('./calBmi/doc_BMI7/file_bmi.json')
            print("+ File file_bmi.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_bmi.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/doc_BMI7/file_kg.json'):
            os.remove('./calBmi/doc_BMI7/file_kg.json')
            print("+ File file_kg.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File file_kg.json does not exist", filefunc28)

    try:
        if os.path.getsize('./calBmi/bmi7.txt'):
            os.remove('./calBmi/bmi7.txt')
            print("+ File bmi7.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File bmi7.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./diag/doc_diag7/diagrecap.txt'):
            os.remove('./diag/doc_diag7/diagrecap.txt')
            print("+ File diagrecap.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File diagrecap.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./labo/doc_labo/result7.txt'):
            os.remove('./labo/doc_labo/result7.txt')
            print("+ File result7.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File result7.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events7/doc_events/fix_agenda/fixed_rdv.txt'):
            os.remove('./patient_agenda/events7/doc_events/fix_agenda/fixed_rdv.txt')
            print("+ File fixed_rdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File fixed_rdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events7/doc_events/fix_agenda/modifrdv.txt'):
            os.remove('./patient_agenda/events7/doc_events/fix_agenda/modifrdv.txt')
            print("+ File modifrdv.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File modifrdv.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events7/doc_events/fix_agenda/patient_value.json'):
            os.remove('./patient_agenda/events7/doc_events/fix_agenda/patient_value.json')
            print("+ File patient_value.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_value.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events7/doc_events/patient_rdv.json'):
            os.remove('./patient_agenda/events7/doc_events/patient_rdv.json')
            print("+ File patient_rdv.json deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_rdv.json does not exist", filefunc28)

    try:
        if os.path.getsize('./patient_agenda/events7/patient_calendar.txt'):
            os.remove('./patient_agenda/events7/patient_calendar.txt')
            print("+ File patient_calendar.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File patient_calendar.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./allergy/allergyfile7.txt'):
            os.remove('./allergy/allergyfile7.txt')
            print("+ File allergyfile7.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File allergyfile7.txt does not exist", filefunc28)

    try:
        if os.path.getsize('./newpatient/entryfile7.txt'):
            with open('./newpatient/entryfile7.txt', 'w') as file:
                file.write("-------")
            print("+ File entryfile7.txt deleted")
    except FileNotFoundError as filefunc28:
        print("+ File entryfile7.txt does not exist", filefunc28)
    print("!!! All files have been deleted !!!")

gui=Tk()
gui.title("Enter new patient")
gui.configure(bg='gray17')
gui.geometry('300x200')

labelName = Label(gui)
labelName = Label(text='Enter Name to delete : ', font="Times 14 bold", 
    fg='cyan', bg='gray17')
labelName.pack(pady=10)

Nompatient=StringVar()
Nompatient.set('Firstname + Lastname')
entree = Entry(gui, textvariable=Nompatient, highlightbackground='gray', bd=4)
entree.pack()

bouton1 = Button(gui, text="Delete", width=8, fg='yellow', bg='navy',
    command = lambda: get(Nompatient, entree))
bouton1.pack(side=LEFT, padx=30, pady=10)

buttQuit=Button(gui, text="Quit", width=8, fg='cyan', bg='navy', 
    command=quit)
buttQuit.pack(side=LEFT, padx=15, pady=10)

gui.mainloop()
