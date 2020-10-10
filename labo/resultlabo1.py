#!/usr/bin/python3
# -*-coding:utf-8-*-


from tkinter import *
import tkinter
from tkinter import messagebox
import os
import subprocess
import platform
import time


def sheetLabo():
    """
    For openning file at pdf 
    format with a bit prog-sys code.
    For Linux, Windows and MAC.
    """
    becall = platform.system()
    print(platform.system())
    
    if becall == 'Linux':
        os.system('gio open "./labo/labosheet.pdf"') # Linux
    elif becall =='Darwin':
        subprocess.call('open', './labo/labosheet.pdf' ) # Mac
    else:
        os.startfile('./labo/labosheet.pdf') # Windows

def sheetMicrobio():
    """
    For openning file at pdf 
    format with a bit prog-sys code.
    For Linux, Windows and MAC.
    """
    callplatform = platform.system()
    print(platform.system())
    
    if callplatform == 'Linux':
        os.system('gio open "./labo/microbio.pdf"') # Linux
    elif callplatform =='Darwin':
        subprocess.call('open', './labo/microbio.pdf' ) # Mac
    else:
        os.startfile('./labo/microbio.pdf') # Windows

def printLabo():
    """
    Need to be modified in 
    function of platform's 
    user !!! Here, it's 
    for linux ! ;)
    """
    #lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
    #lpr.stdin.write('4.15.0-96-generic')
    pass

def recordTofile():
    MsgBox = messagebox.askyesno('Record', 'Results will be saved into Care and Monitoring, ok ?')

    if MsgBox == 1:
        print("Ok, data saved")
        recordOption()
        confRec()
        app.destroy()
    else:
        messagebox.showinfo('Return', 'Ok, nothing changed')

def recordOption():
    print("Date : " + time.strftime("%d/%m/%Y"))
    print("Nom du patient : ", entrytext.get())
    with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
        with open('./labo/doc_labo/result.txt', 'a+') as file2:
            file.write("\n\n----------------------------------------------------------\n")
            file.write("Date : ")
            file.write(time.strftime("%d/%m/%Y")+ '\n')
            file.write("Patient name : ")
            file.write(entrytext.get())
            file2.write("\n---------------------------------------------------------\n\n")
            file2.write("Date : ")
            file2.write(time.strftime("%d/%m/%Y")+ '\n')
            file2.write("Patient name : ")
            file2.write(entrytext.get())

    print(CheckVar1.get())
    if CheckVar1.get()==1:
        print("+ Abilify was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Abilify : (add result of dosage here)\n")
                file2.write("# Abilify : (add result of dosage here)\n")
    else:
        print("+ Abilify ok, nothing to do")
        
    print(CheckVar2.get())
    if CheckVar2.get()==1:
        print("+ Clopixol was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Clopixol : (add result of dosage here)\n")
                file2.write("# Clopixol : (add result of dosage here)\n")
    else:
        print("+ Clopixol ok, nothing to do")

    print(CheckVar3.get())
    if CheckVar3.get()==1:
        print("+ Clozapine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Clozapine : (add result of dosage here)\n")
                file2.write("# Clozapine : (add result of dosage here)\n")
    else:
        print("+ Clozapine ok, nothing to do")
        
    print(CheckVar4.get())
    if CheckVar4.get()==1:
        print("+ Dogmatil was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Dogmatil : (add result of dosage here)\n")
                file2.write("# Dogmatil : (add result of dosage here)\n")
    else:
        print("+ Dogmatil ok, nothing to do")

    print(CheckVar5.get())
    if CheckVar5.get()==1:
        print("+ Entumine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Entumine : (add result of dosage here)\n")
                file2.write("# Entumine : (add result of dosage here)\n")
    else:
        print("+ Entumine ok, nothing to do")

    print(CheckVar6.get())
    if CheckVar6.get()==1:
        print("+ Fluanxol was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Fluanxol : (add result of dosage here)\n")
                file2.write("# Fluanxol : (add result of dosage here)\n")
    else:
        print("+ Fluanxol ok, nothing to do")

    print(CheckVar7.get())
    if CheckVar7.get()==1:
        print("+ Haldol was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Haldol : (add result of dosage here)\n")
                file2.write("# Haldol : (add result of dosage here)\n")
    else:
        print("+ Haldol ok, nothing to do")

    print(CheckVar8.get())
    if CheckVar8.get()==1:
        print("+ Invega was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Invega : (add result of dosage here)\n")
                file2.write("# Invega : (add result of dosage here)\n")
    else:
        print("+ Invega ok, nothing to do")

    print(CheckVar9.get())
    if CheckVar9.get()==1:
        print("+ Nozinan was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Nozinan : (add result of dosage here)\n")
                file2.write("# Nozinan : (add result of dosage here)\n")
    else:
        print("+ Nozinan ok, nothing to do")

    print(CheckVar10.get())
    if CheckVar10.get()==1:
        print("+ Prazine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Prazine : (add result of dosage here)\n")
                file2.write("# Prazine : (add result of dosage here)\n")
    else:
        print("+ Prazine ok, nothing to do")

    print(CheckVar12.get())
    if CheckVar12.get()==1:
        print("+ Quetiapine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Quetiapine : (add result of dosage here)\n")
                file2.write("# Quetiapine : (add result of dosage here)\n")
    else:
        print("+ Quetiapine ok, nothing to do")

    print(CheckVar13.get())
    if CheckVar13.get()==1:
        print("+ Risperdal was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Risperdal : (add result of dosage here)\n")
                file2.write("# Risperdal : (add result of dosage here)\n")
    else:
        print("+ Risperdal ok, nothing to do")

    print(CheckVar14.get())
    if CheckVar14.get()==1:
        print("+ Serdolect was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Serdolect : (add result of dosage here)\n")
                file2.write("# Serdolect : (add result of dosage here)\n")
    else:
        print("+ Serdolect ok, nothing to do")

    print(CheckVar15.get())
    if CheckVar15.get()==1:
        print("+ Solian was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Solian : (add result of dosage here)\n")
                file2.write("# Solian : (add result of dosage here)\n")
    else:
        print("+ Solian ok, nothing to do")

    print(CheckVar16.get())
    if CheckVar16.get()==1:
        print("+ Tiapridal was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Tiapridal : (add result of dosage here)\n")
                file2.write("# Tiapridal : (add result of dosage here)\n")
    else:
        print("+ Tiapridal ok, nothing to do")

    print(CheckVar17.get())
    if CheckVar17.get()==1:
        print("+ Truxal was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Truxal : (add result of dosage here)\n")
                file2.write("# Truxal : (add result of dosage here)\n")
    else:
        print("+ Truxal ok, nothing to do")

    print(CheckVar18.get())
    if CheckVar18.get()==1:
        print("+ Zyprexa was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Zyprexa : (add result of dosage here)\n")
                file2.write("# Zyprexa : (add result of dosage here)\n")
    else:
        print("+ Zyprexa ok, nothing to do")

    print(CheckVar19.get())
    if CheckVar19.get()==1:
        print("+ Briviact was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Briviact : (add result of dosage here)\n")
                file2.write("# Briviact : (add result of dosage here)\n")
    else:
        print("+ Briviact ok, nothing to do")

    print(CheckVar20.get())
    if CheckVar20.get()==1:
        print("+ Carbamazepine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Carbamazepine : (add result of dosage here)\n")
                file2.write("# Carbamazepine : (add result of dosage here)\n")
    else:
        print("+ Carbamazepine ok, nothing to do")

    print(CheckVar21.get())
    if CheckVar21.get()==1:
        print("+ Depakine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Depakine : (add result of dosage here)\n")
                file2.write("# Depakine : (add result of dosage here)\n")
    else:
        print("+ Depakine ok, nothing to do")

    print(CheckVar22.get())
    if CheckVar22.get()==1:
        print("+ Ethosuximide was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Ethosuximide : (add result of dosage here)\n")
                file2.write("# Ethosuximide : (add result of dosage here)\n")
    else:
        print("+ Ethosuximide ok, nothing to do")

    print(CheckVar23.get())
    if CheckVar23.get()==1:
        print("+ Fycompa was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Fycompa : (add result of dosage here)\n")
                file2.write("# Fycompa : (add result of dosage here)\n")
    else:
        print("+ Fycompa ok, nothing to do")

    print(CheckVar24.get())
    if CheckVar24.get()==1:
        print("+ Gabitril was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Gabitril : (add result of dosage here)\n")
                file2.write("# Gabitril : (add result of dosage here)\n")
    else:
        print("+ Gabitril ok, nothing to do")

    print(CheckVar25.get())
    if CheckVar25.get()==1:
        print("+ Inovelon was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Inovelon : (add result of dosage here)\n")
                file2.write("# Inovelon : (add result of dosage here)\n")
    else:
        print("+ Inovelon ok, nothing to do")

    print(CheckVar26.get())
    if CheckVar26.get()==1:
        print("+ Keppra was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Keppra : (add result of dosage here)\n")
                file2.write("# Keppra : (add result of dosage here)\n")
    else:
        print("+ Keppra ok, nothing to do")

    print(CheckVar27.get())
    if CheckVar27.get()==1:
        print("+ Lamictal was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Lamictal : (add result of dosage here)\n")
                file2.write("# Lamictal : (add result of dosage here)\n")
    else:
        print("+ Lamictal ok, nothing to do")

    print(CheckVar28.get())
    if CheckVar28.get()==1:
        print("+ Lyrica was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Lyrica : (add result of dosage here)\n")
                file2.write("# Lyrica : (add result of dosage here)\n")
    else:
        print("+ Lyrica ok, nothing to do")

    print(CheckVar29.get())
    if CheckVar29.get()==1:
        print("+ Myzoline was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Myzoline : (add result of dosage here)\n")
                file2.write("# Myzoline : (add result of dosage here)\n")
    else:
        print("+ Myzoline ok, nothing to do")

    print(CheckVar30.get())
    if CheckVar30.get()==1:
        print("+ Neurontin was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Neurontin : (add result of dosage here)\n")
                file2.write("# Neurontin : (add result of dosage here)\n")
    else:
        print("+ Neurontin ok, nothing to do")

    print(CheckVar31.get())
    if CheckVar31.get()==1:
        print("+ Phenobarbital was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Phenobarbital : (add result of dosage here)\n")
                file2.write("# Phenobarbital : (add result of dosage here)\n")
    else:
        print("+ Phenobarbital ok, nothing to do")

    print(CheckVar32.get())
    if CheckVar32.get()==1:
        print("+ Phenytoine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Phenytoine : (add result of dosage here)\n")
                file2.write("# Phenytoine : (add result of dosage here)\n")
    else:
        print("+ Phenytoine ok, nothing to do")

    print(CheckVar33.get())
    if CheckVar33.get()==1:
        print("+ Sabril was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Sabril : (add result of dosage here)\n")
                file2.write("# Sabril : (add result of dosage here)\n")
    else:
        print("+ Sabril ok, nothing to do")

    print(CheckVar34.get())
    if CheckVar34.get()==1:
        print("+ Taloxa was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Taloxa : (add result of dosage here)\n")
                file2.write("# Taloxa : (add result of dosage here)\n")
    else:
        print("+ Taloxa ok, nothing to do")

    print(CheckVar35.get())
    if CheckVar35.get()==1:
        print("+ Topamax was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Topamax : (add result of dosage here)\n")
                file2.write("# Topamax : (add result of dosage here)\n")
    else:
        print("+ Topamax ok, nothing to do")

    print(CheckVar36.get())
    if CheckVar36.get()==1:
        print("+ Trileptal was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Trileptal : (add result of dosage here)\n")
                file2.write("# Trileptal : (add result of dosage here)\n")
    else:
        print("+ Trileptal ok, nothing to do")

    print(CheckVar37.get())
    if CheckVar37.get()==1:
        print("+ Trobalt was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Trobalt : (add result of dosage here)\n")
                file2.write("# Trobalt : (add result of dosage here)\n")
    else:
        print("+ Trobalt ok, nothing to do")

    print(CheckVar38.get())
    if CheckVar38.get()==1:
        print("+ Vimpat was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Vimpat : (add result of dosage here)\n")
                file2.write("# Vimpat : (add result of dosage here)\n")
    else:
        print("+ Vimpat ok, nothing to do")

    print(CheckVar39.get())
    if CheckVar39.get()==1:
        print("+ Zonegran was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Zonegran : (add result of dosage here)\n")
                file2.write("# Zonegran : (add result of dosage here)\n")
    else:
        print("+ Zonegran ok, nothing to do")

    print(CheckVar40.get())
    if CheckVar40.get()==1:
        print("+ Anafranil was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Anafranil : (add result of dosage here)\n")
                file2.write("# Anafranil : (add result of dosage here)\n")
    else:
        print("+ Anafranil ok, nothing to do")

    print(CheckVar41.get())
    if CheckVar41.get()==1:
        print("+ Citalopram was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Citalopram : (add result of dosage here)\n")
                file2.write("# Citalopram : (add result of dosage here)\n")
    else:
        print("+ Citalopram ok, nothing to do")

    print(CheckVar42.get())
    if CheckVar42.get()==1:
        print("+ Cipralex was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Cipralex : (add result of dosage here)\n")
                file2.write("# Cipralex : (add result of dosage here)\n")
    else:
        print("+ Cipralex ok, nothing to do")

    print(CheckVar43.get())
    if CheckVar43.get()==1:
        print("+ Cymbalta was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Cymbalta : (add result of dosage here)\n")
                file2.write("# Cymbalta : (add result of dosage here)\n")
    else:
        print("+ Cymbalta ok, nothing to do")

    print(CheckVar44.get())
    if CheckVar44.get()==1:
        print("+ Deroxat was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Deroxat : (add result of dosage here)\n")
                file2.write("# Deroxat : (add result of dosage here)\n")
    else:
        print("+ Deroxat ok, nothing to do")

    print(CheckVar45.get())
    if CheckVar45.get()==1:
        print("+ Effexor was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Effexor : (add result of dosage here)\n")
                file2.write("# Effexor : (add result of dosage here)\n")
    else:
        print("+ Effexor ok, nothing to do")

    print(CheckVar46.get())
    if CheckVar46.get()==1:
        print("+ Floxifral was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Floxifral : (add result of dosage here)\n")
                file2.write("# Floxifral : (add result of dosage here)\n")
    else:
        print("+ Floxifral ok, nothing to do")

    print(CheckVar47.get())
    if CheckVar47.get()==1:
        print("+ Fluctine was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Fluctine : (add result of dosage here)\n")
                file2.write("# Fluctine : (add result of dosage here)\n")
    else:
        print("+ Fluctine ok, nothing to do")

    print(CheckVar48.get())
    if CheckVar48.get()==1:
        print("+ Ludiomil was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Ludiomil : (add result of dosage here)\n")
                file2.write("# Ludiomil : (add result of dosage here)\n")
    else:
        print("+ Ludiomil ok, nothing to do")

    print(CheckVar49.get())
    if CheckVar49.get()==1:
        print("+ Remeron was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Remeron : (add result of dosage here)\n")
                file2.write("# Remeron : (add result of dosage here)\n")
    else:
        print("+ Remeron ok, nothing to do")

    print(CheckVar50.get())
    if CheckVar50.get()==1:
        print("+ Saroten was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Saroten : (add result of dosage here)\n")
                file2.write("# Saroten : (add result of dosage here)\n")
    else:
        print("+ Saroten ok, nothing to do")

    print(CheckVar51.get())
    if CheckVar51.get()==1:
        print("+ Sertraline was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Sertraline : (add result of dosage here)\n")
                file2.write("# Sertraline : (add result of dosage here)\n")
    else:
        print("+ Sertraline ok, nothing to do")

    print(CheckVar52.get())
    if CheckVar52.get()==1:
        print("+ Surmontil was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Surmontil : (add result of dosage here)\n")
                file2.write("# Surmontil : (add result of dosage here)\n")
    else:
        print("+ Surmontil ok, nothing to do")

    print(CheckVar53.get())
    if CheckVar53.get()==1:
        print("+ Wellbutrin was checked !")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as file:
            with open('./labo/doc_labo/result.txt', 'a+') as file2:
                file.write("# Wellbutrin : (add result of dosage here)\n")
                file2.write("# Wellbutrin : (add result of dosage here)\n")
    else:
        print("+ Wellbutrin ok, nothing to do")
        with open('./14besoins/doc_suivi/main_14b.txt', 'a+') as endfile:
            with open('./labo/doc_labo/result.txt', 'a+') as endfile2:
                endfile.write("---------------------------------------------------------\n")
                endfile2.write("---------------------------------------------------------\n")

def confRec():
    MsgBox2msg = messagebox.showinfo("Confirmation", "Record confirmed and finished !")

def comburTips():
    subprocess.call('./labo/combtest.py')

app = Tk()
app.title("Labo check")
app.configure(bg='RoyalBlue4')

#label_fra = LabelFrame(app, text="Patient 1",
#    font=('Times 16'),bg='yellow', fg='red', height=2, bd=3)
   
labeltite=Label(app, text='Labo check', 
    font="Times 18 bold", width=10,
    height=3, bg='RoyalBlue4', fg='aquamarine')
labeltite.grid(sticky='e', row=0, column=1, padx=20)

with open('./newpatient/entryfile.txt', 'r') as filename:
    line1 = filename.readline()

entrytext=StringVar()
entrytext.set(line1)
entryname=Entry(app, textvariable=entrytext, width=20)
entryname.grid(sticky='w', row=0, column=2)

# NL
labelresult=Label(app, text='--- Neuroleptiques ---', 
    font="Times 14 bold", width=97,
    height=1, bg='RoyalBlue3', fg='white')
labelresult.grid(row=1, column=0, columnspan=4)

CheckVar1 = IntVar()
C1 = Checkbutton(app, text="Abilify", fg='navy', 
    bg='cyan', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C1.grid(sticky='w', row=2, column=0, padx=10)

CheckVar2 = IntVar()
C2 = Checkbutton(app, text="Clopixol", fg='navy', 
    bg='cyan', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C2.grid(sticky='w', row=3, column=0, padx=10)

CheckVar3 = IntVar()
C3 = Checkbutton(app, text="Clozapine", fg='navy', 
    bg='cyan', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C3.grid(sticky='w', row=4, column=0, padx=10)

CheckVar4 = IntVar()
C4 = Checkbutton(app, text="Dogmatil", fg='navy', 
    bg='cyan', variable=CheckVar4, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C4.grid(sticky='w', row=5, column=0, padx=10)

CheckVar5 = IntVar()
C5 = Checkbutton(app, text="Entumine", fg='navy', 
    bg='cyan', variable=CheckVar5, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C5.grid(sticky='w', row=6, column=0, padx=10)

CheckVar6 = IntVar()
C6 = Checkbutton(app, text="Fluanxol", fg='navy', 
    bg='cyan', variable=CheckVar6, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C6.grid(sticky='w', row=2, column=1, padx=30)

CheckVar7 = IntVar()
C7 = Checkbutton(app, text="Haldol", fg='navy', 
    bg='cyan', variable=CheckVar7, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C7.grid(sticky='w', row=3, column=1, padx=30)

CheckVar8 = IntVar()
C8 = Checkbutton(app, text="Invega", fg='navy', 
    bg='cyan', variable=CheckVar8, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C8.grid(sticky='w', row=4, column=1, padx=30)

CheckVar9 = IntVar()
C9 = Checkbutton(app, text="Nozinan", fg='navy', 
    bg='cyan', variable=CheckVar9, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C9.grid(sticky='w', row=5, column=1, padx=30)

CheckVar10 = IntVar()
C10 = Checkbutton(app, text="Prazine", fg='navy', 
    bg='cyan', variable=CheckVar10, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C10.grid(sticky='w', row=6, column=1, padx=30)

# second column
CheckVar12 = IntVar()
C12 = Checkbutton(app, text="Quetiapine", fg='navy', 
    bg='cyan', variable=CheckVar12, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C12.grid(sticky='w', row=2, column=2, padx=20)

CheckVar13 = IntVar()
C13 = Checkbutton(app, text="Risperdal", fg='navy', 
    bg='cyan', variable=CheckVar13, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C13.grid(sticky='w', row=3, column=2, padx=20)

CheckVar14 = IntVar()
C14 = Checkbutton(app, text="Serdolect", fg='navy', 
    bg='cyan', variable=CheckVar14, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C14.grid(sticky='w', row=4, column=2, padx=20)

CheckVar15 = IntVar()
C15 = Checkbutton(app, text="Solian", fg='navy', 
    bg='cyan', variable=CheckVar15, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C15.grid(sticky='w', row=5, column=2, padx=20)

CheckVar16 = IntVar()
C16 = Checkbutton(app, text="Tiapridal", fg='navy', 
    bg='cyan', variable=CheckVar16, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C16.grid(sticky='w', row=6, column=2, padx=20)

CheckVar17 = IntVar()
C17 = Checkbutton(app, text="Truxal", fg='navy', 
    bg='cyan', variable=CheckVar17, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C17.grid(sticky='e', row=2, column=3, padx=10)

CheckVar18 = IntVar()
C18 = Checkbutton(app, text="Zyprexa", fg='navy', 
    bg='cyan', variable=CheckVar18, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C18.grid(sticky='e', row=3, column=3, padx=10)

# MAE
labelresult2=Label(app, text='--- Médicaments anti-épileptiques ---', 
    font="Times 14 bold", width=97,
    height=1, bg='RoyalBlue3', fg='white')
labelresult2.grid(sticky='w', row=7, column=0, columnspan=4, padx=10)

#separator = Label(app, height=5, bd=2, relief=SUNKEN)
#separator.grid(sticky='ns', row=2, column=1)

CheckVar19 = IntVar()
C19 = Checkbutton(app, text="Briviact", fg='navy', 
    bg='cyan', variable=CheckVar19, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C19.grid(sticky='w', row=8, column=0, padx=10)

CheckVar20 = IntVar()
C20 = Checkbutton(app, text="Carbamazepine", fg='navy', 
    bg='cyan', variable=CheckVar20, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C20.grid(sticky='w', row=9, column=0, padx=10)

CheckVar21 = IntVar()
C21 = Checkbutton(app, text="Depakine", fg='navy', 
    bg='cyan', variable=CheckVar21, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C21.grid(sticky='w', row=10, column=0, padx=10)

CheckVar22 = IntVar()
C22 = Checkbutton(app, text="Ethosuximide", fg='navy', 
    bg='cyan', variable=CheckVar22, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C22.grid(sticky='w', row=11, column=0, padx=10)

CheckVar23 = IntVar()
C23 = Checkbutton(app, text="Fycompa", fg='navy',
	bg='cyan', variable=CheckVar23, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C23.grid(sticky='w', row=12, column=0, padx=10)

CheckVar24 = IntVar()
C24 = Checkbutton(app, text="Gabitril", fg='navy', 
    bg='cyan', variable=CheckVar24, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C24.grid(sticky='w', row=13, column=0, padx=10)

CheckVar25 = IntVar()
C25 = Checkbutton(app, text="Inovelon", fg='navy', 
    bg='cyan', variable=CheckVar25, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C25.grid(sticky='w', row=8, column=1, padx=30)

CheckVar26 = IntVar()
C26 = Checkbutton(app, text="Keppra", fg='navy', 
    bg='cyan', variable=CheckVar26, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C26.grid(sticky='w', row=9, column=1, padx=30)

CheckVar27 = IntVar()
C27 = Checkbutton(app, text="Lamictal", fg='navy', 
    bg='cyan', variable=CheckVar27, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C27.grid(sticky='w', row=10, column=1, padx=30)

CheckVar28 = IntVar()
C28 = Checkbutton(app, text="Lyrica", fg='navy', 
    bg='cyan', variable=CheckVar28, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C28.grid(sticky='w', row=11, column=1, padx=30)

CheckVar29 = IntVar()
C29 = Checkbutton(app, text="Myzoline", fg='navy', 
    bg='cyan', variable=CheckVar29, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C29.grid(sticky='w', row=12, column=1, padx=30)

CheckVar30 = IntVar()
C30 = Checkbutton(app, text="Neurontin", fg='navy', 
    bg='cyan', variable=CheckVar30, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C30.grid(sticky='w', row=13, column=1, padx=30)

CheckVar31 = IntVar()
C31 = Checkbutton(app, text="Phenobarbital", fg='navy', 
    bg='cyan', variable=CheckVar31, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C31.grid(sticky='w', row=8, column=2, padx=20)

CheckVar32 = IntVar()
C32 = Checkbutton(app, text="Phenytoïne", fg='navy', 
    bg='cyan', variable=CheckVar32, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C32.grid(sticky='w', row=9, column=2, padx=20)

CheckVar33 = IntVar()
C33 = Checkbutton(app, text="Sabril", fg='navy', 
    bg='cyan', variable=CheckVar33, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C33.grid(sticky='w', row=10, column=2, padx=20)

CheckVar34 = IntVar()
C34 = Checkbutton(app, text="Taloxa", fg='navy', 
    bg='cyan', variable=CheckVar34, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C34.grid(sticky='w', row=11, column=2, padx=20)

CheckVar35 = IntVar()
C35 = Checkbutton(app, text="Topamax", fg='navy', 
    bg='cyan', variable=CheckVar35, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C35.grid(sticky='w', row=12, column=2, padx=20)

CheckVar36 = IntVar()
C36 = Checkbutton(app, text="Trileptal", fg='navy', 
    bg='cyan', variable=CheckVar36, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C36.grid(sticky='w', row=13, column=2, padx=20)

CheckVar37 = IntVar()
C37 = Checkbutton(app, text="Trobalt", fg='navy', 
    bg='cyan', variable=CheckVar37, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C37.grid(sticky='e', row=8, column=3, padx=10)

CheckVar38 = IntVar()
C38 = Checkbutton(app, text="Vimpat", fg='navy', 
    bg='cyan', variable=CheckVar38, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C38.grid(sticky='e', row=9, column=3, padx=10)

CheckVar39 = IntVar()
C39 = Checkbutton(app, text="Zonegran", fg='navy', 
    bg='cyan', variable=CheckVar39, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C39.grid(sticky='e', row=10, column=3, padx=10)

# ATD
labelinf=Label(app, text='--- Antidépresseurs ---',
    font="Times 14 bold", width=97,
    height=1, bg='RoyalBlue3', fg='white')
labelinf.grid(sticky='w', row=14, column=0, columnspan=4, padx=10)

CheckVar40 = IntVar()
C40 = Checkbutton(app, text="Anafranil", fg='navy', 
    bg='cyan', variable=CheckVar40, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C40.grid(sticky='w', row=15, column=0, padx=10)

CheckVar41 = IntVar()
C41 = Checkbutton(app, text="Citalopram", fg='navy', 
    bg='cyan', variable=CheckVar41, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C41.grid(sticky='w', row=16, column=0, padx=10)

CheckVar42 = IntVar()
C42 = Checkbutton(app, text="Cipralex", fg='navy', 
    bg='cyan', variable=CheckVar42, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C42.grid(sticky='w', row=17, column=0, padx=10)

CheckVar43 = IntVar()
C43 = Checkbutton(app, text="Cymbalta", fg='navy', 
    bg='cyan', variable=CheckVar43, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C43.grid(sticky='w', row=18, column=0, padx=10)

CheckVar44 = IntVar()
C44 = Checkbutton(app, text="Deroxat", fg='navy', 
    bg='cyan', variable=CheckVar44, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C44.grid(sticky='w', row=15, column=1, padx=30)

CheckVar45 = IntVar()
C45 = Checkbutton(app, text="Effexor", fg='navy', 
    bg='cyan', variable=CheckVar45, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C45.grid(sticky='w', row=16, column=1, padx=30)

CheckVar46 = IntVar()
C46 = Checkbutton(app, text="Floxifral", fg='navy', 
    bg='cyan', variable=CheckVar46, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C46.grid(sticky='w', row=17, column=1, padx=30)

CheckVar47 = IntVar()
C47 = Checkbutton(app, text="Fluctine", fg='navy', 
    bg='cyan', variable=CheckVar47, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C47.grid(sticky='w', row=18, column=1, padx=30)

CheckVar48 = IntVar()
C48 = Checkbutton(app, text="Ludiomil", fg='navy', 
    bg='cyan', variable=CheckVar48, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C48.grid(sticky='w', row=15, column=2, padx=20)

CheckVar49 = IntVar()
C49 = Checkbutton(app, text="Remeron", fg='navy', 
    bg='cyan', variable=CheckVar49, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C49.grid(sticky='w', row=16, column=2, padx=20)

CheckVar50 = IntVar()
C50 = Checkbutton(app, text="Saroten", fg='navy', 
    bg='cyan', variable=CheckVar50, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C50.grid(sticky='w', row=17, column=2, padx=20)

CheckVar51 = IntVar()
C51 = Checkbutton(app, text="Sertraline", fg='navy', 
    bg='cyan', variable=CheckVar51, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C51.grid(sticky='w', row=18, column=2, padx=20)

CheckVar52 = IntVar()
C52 = Checkbutton(app, text="Surmontil", fg='navy', 
    bg='cyan', variable=CheckVar52, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C52.grid(sticky='e', row=15, column=3, padx=10)

CheckVar53 = IntVar()
C53 = Checkbutton(app, text="Wellbutrin", fg='navy', 
    bg='cyan', variable=CheckVar53, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C53.grid(sticky='e', row=16, column=3, padx=10)


# Printable sheet
labelinfuri=Label(app, text='--- Printable ---', 
    font="Times 14 bold", width=46,
    height=1, bg='grey30', fg='cyan')
labelinfuri.grid(sticky='w', row=29, column=0, columnspan=2, padx=10)

# Printable sheet
labeltest=Label(app, text='--- Printable2 ---', 
    font="Times 14 bold", width=45,
    height=1, bg='grey30', fg='cyan')
labeltest.grid(sticky='e', row=29, column=2, columnspan=2, padx=10)

# Buttons printable sheet
buttonsheet=Button(app, text="Complete lab sheet", width=15,
    fg='cyan', bg='navy', command=sheetLabo)
buttonsheet.grid(row=30, column=0, padx=10, pady=10)

buttonsheet=Button(app, text="Microbiology sheet", width=15,
    fg='cyan', bg='navy', command=sheetMicrobio)
buttonsheet.grid(row=30, column=1, padx=10, pady=10)

# Button save and quit
buttonsave=Button(app, text="Save", width=10, bd=3,
    fg='yellow', bg='RoyalBlue3', activebackground='dark turquoise',
    highlightbackground='RoyalBlue4', command=recordTofile)
buttonsave.grid(sticky='e', row=44, column=2, pady=10)

buttonquit=Button(app, text='Quit', width=10, bd=3,
    fg='white', bg='RoyalBlue3', activebackground='dark turquoise',
    highlightbackground='RoyalBlue4', command=quit)
buttonquit.grid(sticky='e', row=44, column=3, padx=10, pady=10)

app.mainloop()
