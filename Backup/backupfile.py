#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
import time
import shutil


# To backup all files
listeDate = ["01/05/2020", "01/06/2020", "01/07/2020",
"01/08/2020", "06/09/2020", "01/10/2020", "01/11/2020",
"01/12/2020"]

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
            shutil.copy('./calBmi/bmi11.txt', './Backup/Files11/Backup_Bmi11.txt')
            shutil.copy('./calBmi/bmi12.txt', './Backup/Files12/Backup_Bmi12.txt')
            shutil.copy('./calBmi/bmi13.txt', './Backup/Files13/Backup_Bmi13.txt')
            shutil.copy('./calBmi/bmi14.txt', './Backup/Files14/Backup_Bmi14.txt')
            shutil.copy('./calBmi/bmi15.txt', './Backup/Files15/Backup_Bmi15.txt')
            shutil.copy('./calBmi/bmi16.txt', './Backup/Files16/Backup_Bmi16.txt')
            shutil.copy('./calBmi/bmi17.txt', './Backup/Files17/Backup_Bmi17.txt')
            shutil.copy('./calBmi/bmi18.txt', './Backup/Files18/Backup_Bmi18.txt')
            shutil.copy('./calBmi/bmi19.txt', './Backup/Files19/Backup_Bmi19.txt')
            shutil.copy('./calBmi/bmi20.txt', './Backup/Files20/Backup_Bmi20.txt')
            shutil.copy('./calBmi/bmi21.txt', './Backup/Files21/Backup_Bmi21.txt')
            shutil.copy('./calBmi/bmi22.txt', './Backup/Files22/Backup_Bmi22.txt')
            shutil.copy('./calBmi/bmi23.txt', './Backup/Files23/Backup_Bmi23.txt')
            shutil.copy('./calBmi/bmi24.txt', './Backup/Files24/Backup_Bmi24.txt')
        except FileNotFoundError as infoloop:
            print("Process interrupted", infoloop)
        try:
            print("Backup of Treatments files !")
            shutil.copy('./ttt/doc_ttt/intro_ttt.txt', './Backup/Files1/Backup_ttt.txt')
            shutil.copy('./ttt/doc_ttt2/intro_ttt.txt', './Backup/Files2/Backup_ttt2.txt')
            shutil.copy('./ttt/doc_ttt3/intro_ttt.txt', './Backup/Files3/Backup_ttt3.txt')
            shutil.copy('./ttt/doc_ttt4/intro_ttt.txt', './Backup/Files4/Backup_ttt4.txt')
            shutil.copy('./ttt/doc_ttt5/intro_ttt.txt', './Backup/Files5/Backup_ttt5.txt')
            shutil.copy('./ttt/doc_ttt6/intro_ttt.txt', './Backup/Files6/Backup_ttt6.txt')
            shutil.copy('./ttt/doc_ttt7/intro_ttt.txt', './Backup/Files7/Backup_ttt7.txt')
            shutil.copy('./ttt/doc_ttt8/intro_res.txt', './Backup/Files8/Backup_res8.txt')
            shutil.copy('./ttt/doc_ttt9/intro_res.txt', './Backup/Files9/Backup_res9.txt')
            shutil.copy('./ttt/doc_ttt10/intro_res.txt', './Backup/Files10/Backup_res10.txt')
            shutil.copy('./ttt/doc_ttt11/intro_res.txt', './Backup/Files11/Backup_res11.txt')
            shutil.copy('./ttt/doc_ttt12/intro_res.txt', './Backup/Files12/Backup_res12.txt')
            shutil.copy('./ttt/doc_ttt13/intro_res.txt', './Backup/Files13/Backup_res13.txt')
            shutil.copy('./ttt/doc_ttt14/intro_res.txt', './Backup/Files14/Backup_res14.txt')
            shutil.copy('./ttt/doc_ttt15/intro_res.txt', './Backup/Files15/Backup_res15.txt')
            shutil.copy('./ttt/doc_ttt16/intro_res.txt', './Backup/Files16/Backup_res16.txt')
            shutil.copy('./ttt/doc_ttt17/intro_res.txt', './Backup/Files17/Backup_res17.txt')
            shutil.copy('./ttt/doc_ttt18/intro_res.txt', './Backup/Files18/Backup_res18.txt')
            shutil.copy('./ttt/doc_ttt19/intro_res.txt', './Backup/Files19/Backup_res19.txt')
            shutil.copy('./ttt/doc_ttt20/intro_res.txt', './Backup/Files20/Backup_res20.txt')
            shutil.copy('./ttt/doc_ttt21/intro_res.txt', './Backup/Files21/Backup_res21.txt')
            shutil.copy('./ttt/doc_ttt22/intro_res.txt', './Backup/Files22/Backup_res22.txt')
            shutil.copy('./ttt/doc_ttt23/intro_res.txt', './Backup/Files23/Backup_res23.txt')
            shutil.copy('./ttt/doc_ttt24/intro_res.txt', './Backup/Files24/Backup_res24.txt')
        except FileNotFoundError as infoloop2:
            print("Process interrupted", infoloop2)
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
            shutil.copy('./diag/doc_diag11/diagrecap11.txt', './Backup/Files11/Backup_diag11.txt')
            shutil.copy('./diag/doc_diag12/diagrecap12.txt', './Backup/Files12/Backup_diag12.txt')
            shutil.copy('./diag/doc_diag13/diagrecap13.txt', './Backup/Files13/Backup_diag13.txt')
            shutil.copy('./diag/doc_diag14/diagrecap14.txt', './Backup/Files14/Backup_diag14.txt')
            shutil.copy('./diag/doc_diag15/diagrecap15.txt', './Backup/Files15/Backup_diag15.txt')
            shutil.copy('./diag/doc_diag16/diagrecap16.txt', './Backup/Files16/Backup_diag16.txt')
            shutil.copy('./diag/doc_diag17/diagrecap17.txt', './Backup/Files17/Backup_diag17.txt')
            shutil.copy('./diag/doc_diag18/diagrecap18.txt', './Backup/Files18/Backup_diag18.txt')
            shutil.copy('./diag/doc_diag19/diagrecap19.txt', './Backup/Files19/Backup_diag19.txt')
            shutil.copy('./diag/doc_diag20/diagrecap20.txt', './Backup/Files20/Backup_diag20.txt')
            shutil.copy('./diag/doc_diag21/diagrecap21.txt', './Backup/Files21/Backup_diag21.txt')
            shutil.copy('./diag/doc_diag22/diagrecap22.txt', './Backup/Files22/Backup_diag22.txt')
            shutil.copy('./diag/doc_diag23/diagrecap23.txt', './Backup/Files23/Backup_diag23.txt')
            shutil.copy('./diag/doc_diag24/diagrecap24.txt', './Backup/Files24/Backup_diag24.txt')
        except FileNotFoundError as infoloop3:
            print("Process interrupted", infoloop3)
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
            shutil.copy('./14besoins/doc_suivi11/patient11_14b.txt', './Backup/Files11/Backup_careneeds11.txt')
            shutil.copy('./14besoins/doc_suivi12/patient12_14b.txt', './Backup/Files12/Backup_careneeds12.txt')
            shutil.copy('./14besoins/doc_suivi13/patient13_14b.txt', './Backup/Files13/Backup_careneeds13.txt')
            shutil.copy('./14besoins/doc_suivi14/patient14_14b.txt', './Backup/Files14/Backup_careneeds14.txt')
            shutil.copy('./14besoins/doc_suivi15/patient15_14b.txt', './Backup/Files15/Backup_careneeds15.txt')
            shutil.copy('./14besoins/doc_suivi16/patient16_14b.txt', './Backup/Files16/Backup_careneeds16.txt')
            shutil.copy('./14besoins/doc_suivi17/patient17_14b.txt', './Backup/Files17/Backup_careneeds17.txt')
            shutil.copy('./14besoins/doc_suivi18/patient18_14b.txt', './Backup/Files18/Backup_careneeds18.txt')
            shutil.copy('./14besoins/doc_suivi19/patient19_14b.txt', './Backup/Files19/Backup_careneeds19.txt')
            shutil.copy('./14besoins/doc_suivi20/patient20_14b.txt', './Backup/Files20/Backup_careneeds20.txt')
            shutil.copy('./14besoins/doc_suivi21/patient21_14b.txt', './Backup/Files21/Backup_careneeds21.txt')
            shutil.copy('./14besoins/doc_suivi22/patient22_14b.txt', './Backup/Files22/Backup_careneeds22.txt')
            shutil.copy('./14besoins/doc_suivi23/patient23_14b.txt', './Backup/Files23/Backup_careneeds23.txt')
            shutil.copy('./14besoins/doc_suivi24/patient24_14b.txt', './Backup/Files24/Backup_careneeds24.txt')
        except FileNotFoundError as infoloop4:
            print("Process interrupted", infoloop4)
    else:
        break