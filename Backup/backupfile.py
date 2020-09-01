#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import time
import shutil


# To backup all files
listeDate = ["01/05/2020", "01/06/2020", "01/07/2020",
"01/08/2020", "01/09/2020", "01/10/2020", "01/11/2020",
"01/12/2020"]

for i in listeDate:
    if time.strftime("%d/%m/%Y") == i:
        try:
            print("Backup of Main files !")
            shutil.copy('./param/Main.txt', './Backup/Files1/Backup_Mainparam.txt')
            shutil.copy('./param/Main2.txt', './Backup/Files2/Backup_Mainparam2.txt')
            shutil.copy('./param/Main3.txt', './Backup/Files3/Backup_Mainparam3.txt')
            shutil.copy('./param/Main4.txt', './Backup/Files4/Backup_Mainparam4.txt')
            shutil.copy('./param/Main5.txt', './Backup/Files5/Backup_Mainparam5.txt')
            shutil.copy('./param/Main6.txt', './Backup/Files6/Backup_Mainparam6.txt')
            shutil.copy('./param/Main7.txt', './Backup/Files7/Backup_Mainparam7.txt')
        except FileNotFoundError as infousr:
            print("Process interrupted", infousr)
        try:
            print("Backup of BMI files !")
            shutil.copy('./calBmi/bmi.txt', './Backup/Files1/Backup_Bmi.txt')
            shutil.copy('./calBmi/bmi2.txt', './Backup/Files2/Backup_Bmi2.txt')
            shutil.copy('./calBmi/bmi3.txt', './Backup/Files3/Backup_Bmi3.txt')
            shutil.copy('./calBmi/bmi4.txt', './Backup/Files4/Backup_Bmi4.txt')
            shutil.copy('./calBmi/bmi5.txt', './Backup/Files5/Backup_Bmi5.txt')
            shutil.copy('./calBmi/bmi6.txt', './Backup/Files6/Backup_Bmi6.txt')
            shutil.copy('./calBmi/bmi7.txt', './Backup/Files7/Backup_Bmi7.txt')
        except FileNotFoundError as infousr2:
            print("Process interrupted", infousr2)
        try:
            print("Backup of Treatments files !")
            shutil.copy('./ttt/doc_ttt/intro_ttt.txt', './Backup/Files1/Backup_ttt.txt')
            shutil.copy('./ttt/doc_ttt2/intro_ttt.txt', './Backup/Files2/Backup_ttt2.txt')
            shutil.copy('./ttt/doc_ttt3/intro_ttt.txt', './Backup/Files3/Backup_ttt3.txt')
            shutil.copy('./ttt/doc_ttt4/intro_ttt.txt', './Backup/Files4/Backup_ttt4.txt')
            shutil.copy('./ttt/doc_ttt5/intro_ttt.txt', './Backup/Files5/Backup_ttt5.txt')
            shutil.copy('./ttt/doc_ttt6/intro_ttt.txt', './Backup/Files6/Backup_ttt6.txt')
            shutil.copy('./ttt/doc_ttt7/intro_ttt.txt', './Backup/Files7/Backup_ttt7.txt')
            shutil.copy('./ttt/doc_ttt/intro_res.txt', './Backup/Files1/Backup_res.txt')
            shutil.copy('./ttt/doc_ttt2/intro_res.txt', './Backup/Files2/Backup_res2.txt')
            shutil.copy('./ttt/doc_ttt3/intro_res.txt', './Backup/Files3/Backup_res3.txt')
            shutil.copy('./ttt/doc_ttt4/intro_res.txt', './Backup/Files4/Backup_res4.txt')
            shutil.copy('./ttt/doc_ttt5/intro_res.txt', './Backup/Files5/Backup_res5.txt')
            shutil.copy('./ttt/doc_ttt6/intro_res.txt', './Backup/Files6/Backup_res6.txt')
            shutil.copy('./ttt/doc_ttt7/intro_res.txt', './Backup/Files7/Backup_res7.txt')
        except FileNotFoundError as infousr3:
            print("Process interrupted", infousr3)
        try:
            print("Backup of Diagnosis files !")
            shutil.copy('./diag/doc_diag/diagrecap1.txt', './Backup/Files1/Backup_diag1.txt')
            shutil.copy('./diag/doc_diag2/diagrecap2.txt', './Backup/Files2/Backup_diag2.txt')
            shutil.copy('./diag/doc_diag3/diagrecap3.txt', './Backup/Files3/Backup_diag3.txt')
            shutil.copy('./diag/doc_diag4/diagrecap4.txt', './Backup/Files4/Backup_diag4.txt')
            shutil.copy('./diag/doc_diag5/diagrecap5.txt', './Backup/Files5/Backup_diag5.txt')
            shutil.copy('./diag/doc_diag6/diagrecap6.txt', './Backup/Files6/Backup_diag6.txt')
            shutil.copy('./diag/doc_diag7/diagrecap7.txt', './Backup/Files7/Backup_diag7.txt')
        except FileNotFoundError as infousr4:
            print("Process interrupted", infousr4)
        try:
            print("Backup of Visit Med files !")
            shutil.copy('./vmed/doc_vmed/resultvmed.txt', './Backup/Files1/Backupv_med.txt')
            shutil.copy('./vmed/doc_vmed2/resultvmed.txt', './Backup/Files2/Backupv_med2.txt')
            shutil.copy('./vmed/doc_vmed3/resultvmed.txt', './Backup/Files3/Backupv_med3.txt')
            shutil.copy('./vmed/doc_vmed4/resultvmed.txt', './Backup/Files4/Backupv_med4.txt')
            shutil.copy('./vmed/doc_vmed5/resultvmed.txt', './Backup/Files5/Backupv_med5.txt')
            shutil.copy('./vmed/doc_vmed6/resultvmed.txt', './Backup/Files6/Backupv_med6.txt')
            shutil.copy('./vmed/doc_vmed7/resultvmed.txt', './Backup/Files7/Backupv_med7.txt')
        except FileNotFoundError as infousr5:
            print("Process interrupted", infousr5)
        try:
            print("Backup of Care and Monitoring files !")
            shutil.copy('./14besoins/doc_suivi/patient1_14b.txt', './Backup/Files1/Backup_careneeds1.txt')
            shutil.copy('./14besoins/doc_suivi2/patient2_14b.txt', './Backup/Files2/Backup_careneeds2.txt')
            shutil.copy('./14besoins/doc_suivi3/patient3_14b.txt', './Backup/Files3/Backup_careneeds3.txt')
            shutil.copy('./14besoins/doc_suivi4/patient4_14b.txt', './Backup/Files4/Backup_careneeds4.txt')
            shutil.copy('./14besoins/doc_suivi5/patient5_14b.txt', './Backup/Files5/Backup_careneeds5.txt')
            shutil.copy('./14besoins/doc_suivi6/patient6_14b.txt', './Backup/Files6/Backup_careneeds6.txt')
            shutil.copy('./14besoins/doc_suivi7/patient7_14b.txt', './Backup/Files7/Backup_careneeds7.txt')
        except FileNotFoundError as infousr6:
            print("Process interrupted", infousr6)
        try:
            print("Backup of Aux. Res. files !")
            shutil.copy('./auxsrc/doc_auxsrc/auxsrcfile1.txt', './Backup/Files1/Backup_auxsrc.txt')
            shutil.copy('./auxsrc/doc_auxsrc2/auxsrcfile2.txt', './Backup/Files2/Backup_auxsrc2.txt')
            shutil.copy('./auxsrc/doc_auxsrc3/auxsrcfile3.txt', './Backup/Files3/Backup_auxsrc3.txt')
            shutil.copy('./auxsrc/doc_auxsrc4/auxsrcfile4.txt', './Backup/Files4/Backup_auxsrc4.txt')
            shutil.copy('./auxsrc/doc_auxsrc5/auxsrcfile5.txt', './Backup/Files5/Backup_auxsrc5.txt')
            shutil.copy('./auxsrc/doc_auxsrc6/auxsrcfile6.txt', './Backup/Files6/Backup_auxsrc6.txt')
            shutil.copy('./auxsrc/doc_auxsrc7/auxsrcfile7.txt', './Backup/Files7/Backup_auxsrc7.txt')
        except FileNotFoundError as infousr7:
            print("Process interrupted", infousr7)
        try:
            print("Backup of Story Life files !")
            shutil.copy('./histv/doc_histv/Hvie_patient1.txt', './Backup/Files1/Back_upstory1.txt')
            shutil.copy('./histv/doc_histv2/Hvie_patient2.txt', './Backup/Files2/Back_upstory2.txt')
            shutil.copy('./histv/doc_histv3/Hvie_patient3.txt', './Backup/Files3/Back_upstory3.txt')
            shutil.copy('./histv/doc_histv4/Hvie_patient4.txt', './Backup/Files4/Back_upstory4.txt')
            shutil.copy('./histv/doc_histv5/Hvie_patient5.txt', './Backup/Files5/Back_upstory5.txt')
            shutil.copy('./histv/doc_histv6/Hvie_patient6.txt', './Backup/Files6/Back_upstory6.txt')
            shutil.copy('./histv/doc_histv7/Hvie_patient7.txt', './Backup/Files7/Back_upstory7.txt')
        except FileNotFoundError as infousr8:
            print("Process interrupted", infousr8)
    else:
        break
