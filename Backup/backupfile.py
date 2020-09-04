#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import time
import shutil


# To backup all files
listeDate = ["01/08/2020", "01/09/2020", "01/10/2020", "01/11/2020",
"01/12/2020", "01/01/2021", "01/02/2021", "01/03/2021", "01/04/2021",
"01/05/2021", "01/06/2021", "01/07/2021", "01/08/2021", "01/09/2021", 
"01/10/2021", "01/11/2021", "01/12/2021", "01/01/2022", "01/02/2022"]

for i in listeDate:
    if time.strftime("%d/%m/%Y") == i:
        try:
            print("Backup of BMI files !")
            shutil.copy('./calBmi/bmi.txt', './Backup/Files1/Backup_Bmi.txt')
            shutil.copy('./calBmi/bmi2.txt', './Backup/Files2/Backup_Bmi2.txt')
            shutil.copy('./calBmi/bmi3.txt', './Backup/Files3/Backup_Bmi3.txt')
            shutil.copy('./calBmi/bmi4.txt', './Backup/Files4/Backup_Bmi4.txt')
            shutil.copy('./calBmi/bmi5.txt', './Backup/Files5/Backup_Bmi5.txt')
            shutil.copy('./calBmi/bmi6.txt', './Backup/Files6/Backup_Bmi6.txt')
            shutil.copy('./calBmi/bmi7.txt', './Backup/Files7/Backup_Bmi7.txt')
            shutil.copy('./calBmi/bmi8.txt', './Backup/Files8/Backup_Bmi8.txt')
            shutil.copy('./calBmi/bmi9.txt', './Backup/Files9/Backup_Bmi9.txt')
            shutil.copy('./calBmi/bmi10.txt', './Backup/Files10/Backup_Bmi10.txt')
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
            shutil.copy('./ttt/doc_ttt8/intro_res.txt', './Backup/Files8/Backup_res8.txt')
            shutil.copy('./ttt/doc_ttt9/intro_res.txt', './Backup/Files9/Backup_res9.txt')
            shutil.copy('./ttt/doc_ttt10/intro_res.txt', './Backup/Files10/Backup_res10.txt')
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
            shutil.copy('./diag/doc_diag8/diagrecap8.txt', './Backup/Files8/Backup_diag8.txt')
            shutil.copy('./diag/doc_diag9/diagrecap9.txt', './Backup/Files9/Backup_diag9.txt')
            shutil.copy('./diag/doc_diag10/diagrecap10.txt', './Backup/Files10/Backup_diag10.txt')
        except FileNotFoundError as infousr4:
            print("Process interrupted", infousr4)
        try:
            print("Backup of Care and Monitoring files !")
            shutil.copy('./14besoins/doc_suivi/patient1_14b.txt', './Backup/Files1/Backup_careneeds1.txt')
            shutil.copy('./14besoins/doc_suivi2/patient2_14b.txt', './Backup/Files2/Backup_careneeds2.txt')
            shutil.copy('./14besoins/doc_suivi3/patient3_14b.txt', './Backup/Files3/Backup_careneeds3.txt')
            shutil.copy('./14besoins/doc_suivi4/patient4_14b.txt', './Backup/Files4/Backup_careneeds4.txt')
            shutil.copy('./14besoins/doc_suivi5/patient5_14b.txt', './Backup/Files5/Backup_careneeds5.txt')
            shutil.copy('./14besoins/doc_suivi6/patient6_14b.txt', './Backup/Files6/Backup_careneeds6.txt')
            shutil.copy('./14besoins/doc_suivi7/patient7_14b.txt', './Backup/Files7/Backup_careneeds7.txt')
            shutil.copy('./14besoins/doc_suivi8/patient8_14b.txt', './Backup/Files8/Backup_careneeds8.txt')
            shutil.copy('./14besoins/doc_suivi9/patient9_14b.txt', './Backup/Files9/Backup_careneeds9.txt')
            shutil.copy('./14besoins/doc_suivi10/patient10_14b.txt', './Backup/Files10/Backup_careneeds10.txt')
        except FileNotFoundError as infousr6:
            print("Process interrupted", infousr6)
    else:
        print("There is no date for backup !!!")
        break
