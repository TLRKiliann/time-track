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
        messagebox.showinfo('Return', 'You will return back')

def recordOption():
    print("Date : " + time.strftime("%d/%m/%Y"))
    print("Nom du patient : ", entrytext.get())
    with open('./labo/doc_labo/result5.txt', 'a+') as file:
        file.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        file.write("\nDate : ")
        file.write(time.strftime("%d/%m/%Y")+ '\n')
        file.write("Nom du patient : ")
        file.write(entrytext.get())

    print(CheckVar1.get())
    if CheckVar1.get()==1:
        print("+ Na value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Na value and treatment : (add what the patient needs)\n")
    else:
        print("+ Na value ok, nothing to do")
        
    print(CheckVar2.get())
    if CheckVar2.get()==1:
        print("+ K value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# K value and treatment : (add what the patient needs)\n")
    else:
        print("+ K value ok, nothing to do")

    print(CheckVar3.get())
    if CheckVar3.get()==1:
        print("+ Ca value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Ca value and treatment : (add what the patient needs)\n")
    else:
        print("+ Ca value ok, nothing to do")
        
    print(CheckVar4.get())
    if CheckVar4.get()==1:
        print("+ Mg value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Mg value and treatment : (add what the patient needs)\n")
    else:
        print("+ Mg value ok, nothing to do")

    print(CheckVar5.get())
    if CheckVar5.get()==1:
        print("+ Cl value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Cl value and treatment : (add what the patient needs)\n")
    else:
        print("+ Cl value ok, nothing to do")

    print(CheckVar6.get())
    if CheckVar6.get()==1:
        print("+ Phosphates value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Phosphates value and treatment : (add what the patient needs)\n")
    else:
        print("+ Phosphates value ok, nothing to do")

    print(CheckVar7.get())
    if CheckVar7.get()==1:
        print("+ Bicarbonates value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Bicarbonates value and treatment : (add what the patient needs)\n")
    else:
        print("+ Bicarbonates value ok, nothing to do")

    print(CheckVar8.get())
    if CheckVar8.get()==1:
        print("+ Cardiac workup value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Cardiac workup value and treatment : (add what the patient needs)\n")
    else:
        print("+ Cardiac workup value ok, nothing to do")

    print(CheckVar9.get())
    if CheckVar9.get()==1:
        print("+ CK-MB value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# CK-MB value and treatment : (add what the patient needs)\n")
    else:
        print("+ CK-MB value ok, nothing to do")

    print(CheckVar10.get())
    if CheckVar10.get()==1:
        print("+ Troponin value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Troponin value and treatment : (add what the patient needs)\n")
    else:
        print("+ Troponin value ok, nothing to do")

    print(CheckVar12.get())
    if CheckVar12.get()==1:
        print("+ Cholesterol total value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Cholesterol total value and treatment : (add what the patient needs)\n")
    else:
        print("+ Cholesterol total value ok, nothing to do")

    print(CheckVar13.get())
    if CheckVar13.get()==1:
        print("+ HDL value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# HDL value and treatment : (add what the patient needs)\n")
    else:
        print("+ HDL value ok, nothing to do")

    print(CheckVar14.get())
    if CheckVar14.get()==1:
        print("+ LDL value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# LDL value and treatment : (add what the patient needs)\n")
    else:
        print("+ LDL value ok, nothing to do")

    print(CheckVar15.get())
    if CheckVar15.get()==1:
        print("+ Triglycerides value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Triglycerides value and treatment : (add what the patient needs)\n")
    else:
        print("+ Triglycerides value ok, nothing to do")

    print(CheckVar16.get())
    if CheckVar16.get()==1:
        print("+ ASAT value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# ASAT value and treatment : (add what the patient needs)\n")
    else:
        print("+ ASAT value ok, nothing to do")

    print(CheckVar17.get())
    if CheckVar17.get()==1:
        print("+ ALAT value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# ALAT value and treatment : (add what the patient needs)\n")
    else:
        print("+ ALAT value ok, nothing to do")

    print(CheckVar18.get())
    if CheckVar18.get()==1:
        print("+ Gamma-GT value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Gamma-GT value and treatment : (add what the patient needs)\n")
    else:
        print("+ Gamma-GT value ok, nothing to do")

    print(CheckVar19.get())
    if CheckVar19.get()==1:
        print("+ Alkaline phosphatase value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Alkaline phosphatase value and treatment : (add what the patient needs)\n")
    else:
        print("+ Alkaline phosphatase value ok, nothing to do")

    print(CheckVar20.get())
    if CheckVar20.get()==1:
        print("+ Bilirubin direct value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Bilirubin direct value and treatment : (add what the patient needs)\n")
    else:
        print("+ Bilirubin direct value ok, nothing to do")

    print(CheckVar21.get())
    if CheckVar21.get()==1:
        print("+ Bilirubin indirect value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Bilirubin indirect value and treatment : (add what the patient needs)\n")
    else:
        print("+ Bilirubin indirect value ok, nothing to do")

    print(CheckVar22.get())
    if CheckVar22.get()==1:
        print("+ LDH value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# LDH value and treatment : (add what the patient needs)\n")
    else:
        print("+ LDH value ok, nothing to do")

    print(CheckVar23.get())
    if CheckVar23.get()==1:
        print("+ Uric acid value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Uric acid value and treatment : (add what the patient needs)\n")
    else:
        print("+ Uric acid value ok, nothing to do")

    print(CheckVar24.get())
    if CheckVar24.get()==1:
        print("+ TP value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# TP value and treatment : (add what the patient needs)\n")
    else:
        print("+ TP value ok, nothing to do")

    print(CheckVar25.get())
    if CheckVar25.get()==1:
        print("+ INR value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# INR value and treatment : (add what the patient needs)\n")
    else:
        print("+ INR value ok, nothing to do")

    print(CheckVar26.get())
    if CheckVar26.get()==1:
        print("+ Fasting glucose value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Fasting glucose value and treatment : (add what the patient needs)\n")
    else:
        print("+ Fasting glucose value ok, nothing to do")

    print(CheckVar27.get())
    if CheckVar27.get()==1:
        print("+ Postprandial glucose value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Postprandial glucose value and treatment : (add what the patient needs)\n")
    else:
        print("+ Postprandial glucose value ok, nothing to do")

    print(CheckVar28.get())
    if CheckVar28.get()==1:
        print("+ HbA1c value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# HbA1c value and treatment : (add what the patient needs)\n")
    else:
        print("+ HbA1c value ok, nothing to do")

    print(CheckVar29.get())
    if CheckVar29.get()==1:
        print("+ Iron value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Iron value and treatment : (add what the patient needs)\n")
    else:
        print("+ Iron value ok, nothing to do")

    print(CheckVar30.get())
    if CheckVar30.get()==1:
        print("+ Ferritine value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Ferritine value and treatment : (add what the patient needs)\n")
    else:
        print("+ Ferritine value ok, nothing to do")

    print(CheckVar31.get())
    if CheckVar31.get()==1:
        print("+ Vitamin B12 value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Vitamin B12 value and treatment : (add what the patient needs)\n")
    else:
        print("+ Vitamin B12 value ok, nothing to do")

    print(CheckVar32.get())
    if CheckVar32.get()==1:
        print("+ Folates (B9) value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Folates (B9) value and treatment : (add what the patient needs)\n")
    else:
        print("+ Folates (B9) value ok, nothing to do")

    print(CheckVar33.get())
    if CheckVar33.get()==1:
        print("+ Urea value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Urea value and treatment : (add what the patient needs)\n")
    else:
        print("+ Urea value ok, nothing to do")

    print(CheckVar34.get())
    if CheckVar34.get()==1:
        print("+ Creat value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Creat value and treatment : (add what the patient needs)\n")
    else:
        print("+ Creat value ok, nothing to do")

    print(CheckVar35.get())
    if CheckVar35.get()==1:
        print("+ Sediment. velocity value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Sediment. velocity value and treatment : (add what the patient needs)\n")
    else:
        print("+ Sediment. velocity value ok, nothing to do")

    print(CheckVar36.get())
    if CheckVar36.get()==1:
        print("+ C-react. protein value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# C-react. protein value and treatment : (add what the patient needs)\n")
    else:
        print("+ C-react. protein value ok, nothing to do")

    print(CheckVar37.get())
    if CheckVar37.get()==1:
        print("+ Albumina value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Albumina value and treatment : (add what the patient needs)\n")
    else:
        print("+ Albumina value ok, nothing to do")

    print(CheckVar38.get())
    if CheckVar38.get()==1:
        print("+ Cortisol value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Cortisol value and treatment : (add what the patient needs)\n")
    else:
        print("+ Cortisol value ok, nothing to do")

    print(CheckVar39.get())
    if CheckVar39.get()==1:
        print("+ ACTH value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# ACTH value and treatment : (add what the patient needs)\n")
    else:
        print("+ ACTH value ok, nothing to do")

    print(CheckVar40.get())
    if CheckVar40.get()==1:
        print("+ TSH value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# TSH value and treatment : (add what the patient needs)\n")
    else:
        print("+ TSH value ok, nothing to do")

    print(CheckVar41.get())
    if CheckVar41.get()==1:
        print("+ free T4 value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# free T4 value and treatment : (add what the patient needs)\n")
    else:
        print("+ free T4 value ok, nothing to do")

    print(CheckVar42.get())
    if CheckVar42.get()==1:
        print("+ free free T3 value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# free free T3 value and treatment : (add what the patient needs)\n")
    else:
        print("+ free free T3 value ok, nothing to do")

    print(CheckVar43.get())
    if CheckVar43.get()==1:
        print("+ free total T3 value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# free total T3 value and treatment : (add what the patient needs)\n")
    else:
        print("+ free total T3 value ok, nothing to do")

    print(CheckVar44.get())
    if CheckVar44.get()==1:
        print("+ Stix (strip) was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Stix (strip) and treatment will be... : (add what the patient needs)\n")
    else:
        print("+ Stix (strip) ok, nothing to do")

    print(CheckVar45.get())
    if CheckVar45.get()==1:
        print("+ Uricult done value was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Uricult done and treatment : (add what the patient needs)\n")
    else:
        print("+ Uricult ok, nothing to do")

    print(CheckVar46.get())
    if CheckVar46.get()==1:
        print("+ Coproculture was checked !")
        with open('./labo/doc_labo/result5.txt', 'a+') as file:
            file.write("# Coproculture and treatment : (add what the patient needs)\n")
    else:
        print("+ Coproculture ok, nothing to do")
    with open('./labo/doc_labo/result.txt', 'a+') as endfile:
        endfile.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
 
def confRec():
    MsgBox2msg = messagebox.showinfo("Confirmation", "Record confirmed and finished !")

def comburTips():
    subprocess.call('./labo/combtest5.py')

app = Tk()
app.title("Labo check")
app.configure(bg='#82193e')

#label_fra = LabelFrame(app, text="Patient 1",
#    font=('Times 16'),bg='yellow', fg='red', height=2, bd=3)
   
labeltite=Label(app, text='Labo check', 
    font="Times 18 bold", width=10,
    height=3, bg='#82193e', fg='aquamarine')
labeltite.grid(sticky='e', row=0, column=1, padx=20)

with open('./newpatient/entryfile5.txt', 'r') as filename:
    line1 = filename.readline()

entrytext=StringVar()
entrytext.set(line1)
entryname=Entry(app, textvariable=entrytext, width=20)
entryname.grid(sticky='w', row=0, column=2)

# Electrolytes
labelresult=Label(app, text='--- Electrolytes ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelresult.grid(sticky='w', row=1, column=0, columnspan=2, padx=10)

CheckVar1 = IntVar()
C1 = Checkbutton(app, text="Na⁺", fg='navy', 
    bg='cyan', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C1.grid(sticky='w', row=2, column=0, padx=10)

CheckVar2 = IntVar()
C2 = Checkbutton(app, text="K⁺", fg='navy', 
    bg='cyan', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C2.grid(sticky='w', row=3, column=0, padx=10)

CheckVar3 = IntVar()
C3 = Checkbutton(app, text="Ca⁺ (total)", fg='navy', 
    bg='cyan', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C3.grid(sticky='w', row=2, column=1, padx=30)

CheckVar4 = IntVar()
C4 = Checkbutton(app, text="Mg⁺", fg='navy', 
    bg='cyan', variable=CheckVar4, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C4.grid(sticky='w', row=3, column=1, padx=30)

CheckVar5 = IntVar()
C5 = Checkbutton(app, text="Cl⁻", fg='navy', 
    bg='cyan', variable=CheckVar5, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C5.grid(sticky='w', row=4, column=1, padx=30)

CheckVar6 = IntVar()
C6 = Checkbutton(app, text="Phosphates (HPO4²⁻)", fg='navy', 
    bg='cyan', variable=CheckVar6, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C6.grid(sticky='w', row=4, column=0, padx=10)

CheckVar7 = IntVar()
C7 = Checkbutton(app, text="Bicarbonates (HCO₃⁻)", fg='navy', 
    bg='cyan', variable=CheckVar7, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C7.grid(sticky='w', row=5, column=0, padx=10)

# Cardio-vasc
labelcardio=Label(app, text='--- Cardiovascular ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelcardio.grid(row=1, column=2, padx=10)

CheckVar8 = IntVar()
C8 = Checkbutton(app, text="Cardiac workup", fg='navy', 
    bg='cyan', variable=CheckVar8, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C8.grid(sticky='w', row=2, column=2, padx=10)

CheckVar9 = IntVar()
C9 = Checkbutton(app, text="CK-MB", fg='navy', 
    bg='cyan', variable=CheckVar9, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C9.grid(sticky='w', row=3, column=2, padx=10)

CheckVar10 = IntVar()
C10 = Checkbutton(app, text="Troponin", fg='navy', 
    bg='cyan', variable=CheckVar10, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C10.grid(sticky='w', row=4, column=2, padx=10)

# second column
CheckVar12 = IntVar()
C12 = Checkbutton(app, text="Cholesterol total", fg='navy', 
    bg='cyan', variable=CheckVar12, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C12.grid(sticky='e', row=2, column=2, padx=20)

CheckVar13 = IntVar()
C13 = Checkbutton(app, text="HDL", fg='navy', 
    bg='cyan', variable=CheckVar13, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C13.grid(sticky='e', row=3, column=2, padx=20)

CheckVar14 = IntVar()
C14 = Checkbutton(app, text="LDL", fg='navy', 
    bg='cyan', variable=CheckVar14, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C14.grid(sticky='e', row=4, column=2, padx=20)

CheckVar15 = IntVar()
C15 = Checkbutton(app, text="Triglycerides", fg='navy', 
    bg='cyan', variable=CheckVar15, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C15.grid(sticky='e', row=5, column=2, padx=20)

# Hepatologia
labelresult2=Label(app, text='--- Hepathology ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelresult2.grid(sticky='w', row=7, column=0, columnspan=2, padx=10)

#separator = Label(app, height=5, bd=2, relief=SUNKEN)
#separator.grid(sticky='ns', row=2, column=1)

CheckVar16 = IntVar()
C16 = Checkbutton(app, text="ASAT", fg='navy', 
    bg='cyan', variable=CheckVar16, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C16.grid(sticky='w', row=8, column=0, padx=10)

CheckVar17 = IntVar()
C17 = Checkbutton(app, text="ALAT", fg='navy', 
    bg='cyan', variable=CheckVar17, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C17.grid(sticky='w', row=9, column=0, padx=10)

CheckVar18 = IntVar()
C18 = Checkbutton(app, text="Gamma-GT", fg='navy', 
    bg='cyan', variable=CheckVar18, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C18.grid(sticky='w', row=10, column=0, padx=10)

CheckVar19 = IntVar()
C19 = Checkbutton(app, text="Alkaline phosphatase", fg='navy', 
    bg='cyan', variable=CheckVar19, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C19.grid(sticky='w', row=11, column=0, padx=10)

CheckVar20 = IntVar()
C20 = Checkbutton(app, text="Bilirubin direct", fg='navy', 
    bg='cyan', variable=CheckVar20, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C20.grid(sticky='w', row=10, column=1, padx=30)

CheckVar21 = IntVar()
C21 = Checkbutton(app, text="Bilirubin indirect", fg='navy', 
    bg='cyan', variable=CheckVar21, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C21.grid(sticky='w', row=11, column=1, padx=30)

CheckVar22 = IntVar()
C22 = Checkbutton(app, text="LDH", fg='navy', 
    bg='cyan', variable=CheckVar22, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C22.grid(sticky='w', row=8, column=1, padx=30)

CheckVar23 = IntVar()
C23 = Checkbutton(app, text="Uric acid", fg='navy', 
    bg='cyan', variable=CheckVar23, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C23.grid(sticky='w', row=9, column=1, padx=30)

# Coagulation
labelresult3=Label(app, text='--- Coagulation ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelresult3.grid(row=7, column=2, padx=10)

CheckVar24 = IntVar()
C24 = Checkbutton(app, text="TP", fg='navy', 
    bg='cyan', variable=CheckVar24, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C24.grid(sticky='w', row=8, column=2, padx=10)

CheckVar25 = IntVar()
C25 = Checkbutton(app, text="INR", fg='navy', 
    bg='cyan', variable=CheckVar25, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C25.grid(sticky='w', row=9, column=2, padx=10)

# Glucids
labelgluco=Label(app, text='--- Carbohydrates ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelgluco.grid(sticky='w', row=12, column=0, columnspan=2, padx=10)

CheckVar26 = IntVar()
C26 = Checkbutton(app, text="Fasting glucose", fg='navy', 
    bg='cyan', variable=CheckVar26, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C26.grid(sticky='w', row=13, column=0, padx=10)

CheckVar27 = IntVar()
C27 = Checkbutton(app, text="Postprandial glucose", fg='navy', 
    bg='cyan', variable=CheckVar27, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C27.grid(sticky='w', row=14, column=0, padx=10)

CheckVar28 = IntVar()
C28 = Checkbutton(app, text="HbA1c", fg='navy', 
    bg='cyan', variable=CheckVar28, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C28.grid(sticky='w', row=15, column=0, padx=10)

# Anemia
labelanemia=Label(app, text='--- Anemia ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelanemia.grid(row=12, column=2, padx=10)

CheckVar29 = IntVar()
C29 = Checkbutton(app, text="Iron", fg='navy', 
    bg='cyan', variable=CheckVar29, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C29.grid(sticky='w', row=13, column=2, padx=10)

CheckVar30 = IntVar()
C30 = Checkbutton(app, text="Ferritin", fg='navy', 
    bg='cyan', variable=CheckVar30, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C30.grid(sticky='w', row=14, column=2, padx=10)

CheckVar31 = IntVar()
C31 = Checkbutton(app, text="Vitamin B12", fg='navy', 
    bg='cyan', variable=CheckVar31, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C31.grid(sticky='e', row=13, column=2, padx=10)

CheckVar32 = IntVar()
C32 = Checkbutton(app, text="Folates (B9)", fg='navy', 
    bg='cyan', variable=CheckVar32, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C32.grid(sticky='e', row=14, column=2, padx=10)

# Reins
labelinf=Label(app, text='--- Renal ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelinf.grid(sticky='w', row=17, column=0, columnspan=2, padx=10)

CheckVar33 = IntVar()
C33 = Checkbutton(app, text="Urea", fg='navy', 
    bg='cyan', variable=CheckVar33, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C33.grid(sticky='w', row=18, column=0, padx=10)

CheckVar34 = IntVar()
C34 = Checkbutton(app, text="Creat.", fg='navy', 
    bg='cyan', variable=CheckVar34, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C34.grid(sticky='w', row=19, column=0, padx=10)

# Inflammation
labelinf=Label(app, text='--- Inflammation ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelinf.grid(row=17, column=2, padx=10)

CheckVar35 = IntVar()
C35 = Checkbutton(app, text="Sediment. velocity", fg='navy', 
    bg='cyan', variable=CheckVar35, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C35.grid(sticky='w', row=18, column=2, padx=10)

CheckVar36 = IntVar()
C36 = Checkbutton(app, text="C-react. protein", fg='navy', 
    bg='cyan', variable=CheckVar36, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C36.grid(sticky='w', row=19, column=2, padx=10)

CheckVar37 = IntVar()
C37 = Checkbutton(app, text="Albumina", fg='navy', 
    bg='cyan', variable=CheckVar37, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C37.grid(sticky='w', row=20, column=2, padx=10)

CheckVar38 = IntVar()
C38 = Checkbutton(app, text="Cortisol", fg='navy', 
    bg='cyan', variable=CheckVar38, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C38.grid(sticky='e', row=18, column=2, padx=10)

CheckVar39 = IntVar()
C39 = Checkbutton(app, text="ACTH", fg='navy', 
    bg='cyan', variable=CheckVar39, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C39.grid(sticky='e', row=19, column=2, padx=10)

# Endocrinology
labelinf=Label(app, text='--- Endocrinology ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelinf.grid(sticky='w', row=23, column=0, columnspan=2, padx=10)

CheckVar40 = IntVar()
C40 = Checkbutton(app, text="TSH", fg='navy', 
    bg='cyan', variable=CheckVar40, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C40.grid(sticky='w', row=24, column=0, padx=10)

CheckVar41 = IntVar()
C41 = Checkbutton(app, text="free T4", fg='navy', 
    bg='cyan', variable=CheckVar41, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C41.grid(sticky='w', row=25, column=0, padx=10)

CheckVar42 = IntVar()
C42 = Checkbutton(app, text="free T3", fg='navy', 
    bg='cyan', variable=CheckVar42, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C42.grid(sticky='w', row=24, column=1, padx=30)

CheckVar43 = IntVar()
C43 = Checkbutton(app, text="total T3", fg='navy', 
    bg='cyan', variable=CheckVar43, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C43.grid(sticky='w', row=25, column=1, padx=30)

# Urinary infection
labelinfuri=Label(app, text='--- Urinary infection ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labelinfuri.grid(sticky='w', row=26, column=0, columnspan=2, padx=10)

CheckVar44 = IntVar()
C44 = Checkbutton(app, text="Stix (strip)", fg='navy', 
    bg='cyan', variable=CheckVar44, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C44.grid(sticky='w', row=27, column=0, padx=10)

# Stix
ButtStix=Button(app, text='- Combur -', width=20,
    height=1, bg='navy', fg='cyan', command=comburTips)
ButtStix.grid(row=27, column=1, padx=20)

CheckVar45 = IntVar()
C45 = Checkbutton(app, text="Uricult", fg='navy', 
    bg='cyan', variable=CheckVar45, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C45.grid(sticky='w', row=28, column=0, padx=10)

# Coproculture
labecopro=Label(app, text='--- Coproculture ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='white')
labecopro.grid(row=26, column=2, padx=10)

CheckVar46 = IntVar()
C46 = Checkbutton(app, text="Check", fg='navy', 
    bg='cyan', variable=CheckVar46, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor="w")
C46.grid(sticky='w', row=27, column=2, padx=10)

# Printable sheet
labelinfuri=Label(app, text='--- Printable ---', 
    font="Times 14 bold", width=46,
    height=1, bg='gray30', fg='cyan')
labelinfuri.grid(sticky='w', row=29, column=0, columnspan=2, padx=10)

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
    highlightbackground='#82193e', command=recordTofile)
buttonsave.grid(row=44, column=2, pady=10)

buttonquit=Button(app, text='Quit', width=10, bd=3,
    fg='white', bg='RoyalBlue3', activebackground='dark turquoise',
    highlightbackground='#82193e', command=quit)
buttonquit.grid(sticky='e', row=44, column=2, padx=10, pady=10)

app.mainloop()
