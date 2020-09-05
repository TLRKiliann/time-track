#!/usr/bin/python3
# -*-encoding:Utf-8-*-


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import os
import json
import subprocess


def callbackDay(event):
    print(comboDay.get())

def callbackMonth(event):
    print(comboMonth.get())

def callbackYear(event):
    print(comboYear.get())

def callbackFinishDay(event):
    print(comboFinishDay.get())

def callbackFinishMonth(event):
    print(comboFinishMonth.get())

def callbackFinishYear(event):
    print(comboFinishYear.get())

def showTreat():
    """
    To display tabs of ttt, convdose.json 
    file must be existing.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt6/convdose.json'):
            subprocess.call('./ttt/doc_ttt6/tabs.py')
    except FileNotFoundError as no_tabs:
        print("+ Sorry, it's not possible to show tab of ttt, \
convdose.json file missing !")
        tttTabs()

def tttTabs():
    MSBTABS = messagebox.showinfo("Info", "No ttt recorded for \
patient 6, convdose.json file missing !") 

def showReserve():
    """
    To display tabs of reserve, convres.json 
    file must be existing.
    """
    try:
        if os.path.getsize('./ttt/doc_ttt6/convres.json'):
            subprocess.call('./ttt/doc_ttt6/tabres.py')
    except FileNotFoundError as no_tabs:
        print("+ Sorry, it's not possible to show tab of reserve, \
convres.json file missing !")
        reserveTabs()

def reserveTabs():
    MSBTABS = messagebox.showinfo("Info", "No reserve recorded for \
patient 6, convres.json file missing !")

def deleteTreatment():
    """
    To earase one line in array
    for one treatment
    """
    MSB = messagebox.askyesno('Delete ttt', 'Are you sure ?')
    if MSB == 1:
        print("Ok, ttt has been ejected !")
        messagebox.showinfo('info BOX', 'Treatment is away !')
        try:
            if os.path.getsize('./ttt/doc_ttt6/convdose.json'):
                print("+ File 'convdose' exist !")
                with open('./ttt/doc_ttt6/convdose.json', 'r') as datafile:
                    datastore = json.load(datafile)
                
                dataDose = datastore
                for key, value in dataDose.items():
                    if deleteTreat.get() == value[0]['Treatment']:
                        del value[0]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[1]['Treatment']:
                        del value[1]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[2]['Treatment']:
                        del value[2]
                        print("+ TTT earased !")
                        
                    elif deleteTreat.get() == value[3]['Treatment']:
                        del value[3]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[4]['Treatment']:
                        del value[4]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[5]['Treatment']:
                        del value[5]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[6]['Treatment']:
                        del value[6]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[7]['Treatment']:
                        del value[7]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[8]['Treatment']:
                        del value[8]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[9]['Treatment']:
                        del value[9]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[10]['Treatment']:
                        del value[10]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[11]['Treatment']:
                        del value[11]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[12]['Treatment']:
                        del value[12]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[13]['Treatment']:
                        del value[13]
                        print("+ TTT earased !")

                    elif deleteTreat.get() == value[14]['Treatment']:
                        del value[14]
                        print("+ TTT earased !")
                    else:
                        print("Treatment is not present into medication")

                    if deleteTreat.get() == '':
                        print("None treatment checked")
                    else:
                        print("---Ok VALUE 'Treatment' earased---")
                        with open('./ttt/doc_ttt6/convdose.json', 'w') as datafile2:
                            json.dump(dataDose, datafile2, indent=4)
        except FileNotFoundError as outcom:
            print('+ Sorry, file convdose.json not exist !', outcom)
    else:           
        NoforQ = messagebox.showinfo('Return', 'Treatment not earased')

def deleteReserve():
    """
    To earase one line in array
    for one Reserve
    """
    MSB2 = messagebox.askyesno('Delete Reserve', 'Are you sure ?')
    if MSB2 == 1:
        print("Ok, Reserve has been ejected !")
        messagebox.showinfo('info BOX', 'Reserve is away !')
        try:
            if os.path.getsize('./ttt/doc_ttt6/convres.json'):
                print("+ File 'convres' exist !")
                with open('./ttt/doc_ttt6/convres.json', 'r') as datafile:
                    datastore = json.load(datafile)
                
                dataRes = datastore
                for key, value in dataRes.items():
                    if deleteRes.get() == value[0]['Treatment']:
                        del value[0]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[1]['Treatment']:
                        del value[1]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[2]['Treatment']:
                        del value[2]
                        print("+ Reserve earased !")
                        
                    elif deleteRes.get() == value[3]['Treatment']:
                        del value[3]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[4]['Treatment']:
                        del value[4]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[5]['Treatment']:
                        del value[5]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[6]['Treatment']:
                        del value[6]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[7]['Treatment']:
                        del value[7]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[8]['Treatment']:
                        del value[8]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[9]['Treatment']:
                        del value[9]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[10]['Treatment']:
                        del value[10]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[11]['Treatment']:
                        del value[11]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[12]['Treatment']:
                        del value[12]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[13]['Treatment']:
                        del value[13]
                        print("+ Reserve earased !")

                    elif deleteRes.get() == value[14]['Treatment']:
                        del value[14]
                        print("+ Reserve earased !")
                    else:
                        print("Reserve is not present into medication")

                    if deleteRes.get() == '':
                        print("None Reserve checked")
                    else:
                        print("---Ok VALUE 'Reserve' earased---")
                        with open('./ttt/doc_ttt6/convres.json', 'w') as datafile2:
                            json.dump(dataRes, datafile2, indent=4)
        except FileNotFoundError as outinfo:
            print('+ Sorry, file convres.json not exist !', outinfo)
    else:           
        NoforQ = messagebox.showinfo('Return', 'Reserve not earased')

def copyTttMess():
    """
    MessageBox to ensure if it's well done.
    """
    MsgBox = messagebox.askyesno('Record', 'Do you want to save ?')
    if MsgBox == 1:
        print("Ok to save")
        copyToFile()
        #app.destroy()
    else:
        messagebox.showinfo('Return', 'You will return to the application')

def copyToFile():
    """
    To write all data to intro_ttt.json
    to reuse them after.
    """
    with open('./ttt/doc_ttt6/intro_ttt.txt', '+a') as file:
        file.write(str("Date : "))
        file.write(textDate.get() + '\n')
        file.write(str("Heure : "))
        file.write(textHour.get() + '\n')
        file.write(str("Name : "))
        file.write(textName.get() + '\n')
        file.write(str("Date of introduction : "))
        file.write(comboDay.get())
        file.write(comboMonth.get())
        file.write(comboYear.get())
        file.write(str('\n'))
        file.write(str("Nom du ttt : "))
        file.write(textTreat.get() + '\n')
        file.write(str("Dosage du ttt : "))
        file.write(textDosage.get() + '\n')
        if CheckVarMatin.get()==1:
            file.write(str("Matin : "))
        file.write(Entmatin.get() + '\n')
        if CheckVarMidi.get()==1:
            file.write(str("Midi : "))
        file.write(Entmidi.get() + '\n')
        if CheckVarSoir.get()==1:
            file.write(str("Soir : "))
        file.write(Entsoir.get() + '\n')
        if CheckVarNuit.get()==1:
            file.write(str("Nuit : "))
        file.write(Entnuit.get() + '\n')
        file.write(str("Date of end : "))
        file.write(comboFinishDay.get())
        file.write('/' + comboFinishMonth.get() + '/')
        file.write(comboFinishYear.get())
        file.write(str('\n'))
        file.write(str("Signature : "))
        file.write(textSign.get())
        file.write(str('\n\n'))
    try:
        if os.path.getsize('./ttt/doc_ttt6/convdose.json'):
            print("+ File 'convdose' exist !")
            with open('./ttt/doc_ttt6/convdose.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataDose = datastore
            dataDose['data'].append({'Date' : textDate.get(), \
                'Date of introduction' : comboDay.get() + comboMonth.get() + \
                comboYear.get(), 'Date of end' : comboFinishDay.get() + \
                '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
                'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
                'Matin' : Entmatin.get(), 'Midi' : Entmidi.get(), \
                'Soir' : Entsoir.get(), 'Nuit' : Entnuit.get()})
            if textTreat.get() == "":
                print("---No value 'Treatment' introduced---")
            else:
                print("---Ok value 'Treatment' introduced---")
                with open('./ttt/doc_ttt6/convdose.json', 'w') as datafile2:
                    json.dump(dataDose, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file convdose.json not exist !')
        print(str(outcom))
        print("+ File convdose.json created !")
        dataDose = {}
        dataDose['data'] = []
        dataDose['data'].append({'Date' : textDate.get(), \
            'Date of introduction' : comboDay.get() + comboMonth.get() + \
            comboYear.get(), 'Date of end' : comboFinishDay.get() + \
            '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
            'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
            'Matin' : Entmatin.get(), 'Midi' : Entmidi.get(), \
            'Soir' : Entsoir.get(), 'Nuit' : Entnuit.get()})
        if textTreat.get() == "":
            print("---No value 'Treatment' introduced---")
        else:
            print("---Ok value 'Treatment' introduced---")
            with open('./ttt/doc_ttt6/convdose.json', 'w') as datafile:
                json.dump(dataDose, datafile, indent=4)

def copyResMess():
    """
    MessageBox to ensure if it's well done.
    """
    MsgBox = messagebox.askyesno('Record', 'Do you want to save ?')
    if MsgBox == 1:
        print("Ok to save")
        copyToReserve()
        #app.destroy()
    else:
        messagebox.showinfo('Return', 'You will return to the application')

def copyToReserve():
    """
    To write all data to intro_res.txt
    to reuse them after.
    """
    with open('./ttt/doc_ttt6/intro_res.txt', '+a') as file:
        file.write(str("Date : "))
        file.write(textDate.get() + '\n')
        file.write(str("Heure : "))
        file.write(textHour.get() + '\n')
        file.write(str("Name : "))
        file.write(textName.get() + '\n')
        file.write(str("Date of introduction : "))
        file.write(comboDay.get())
        file.write(comboMonth.get())
        file.write(comboYear.get())
        file.write(str('\n'))
        file.write(str("Nom du ttt : "))
        file.write(textTreat.get() + '\n')
        file.write(str("Dosage du ttt : "))
        file.write(textDosage.get() + '\n')
        if CheckVar1.get()==1:
            file.write(str("Réserve : "))
            file.write(str("Oui\n"))
        if CheckVar2.get()==1:
            file.write(str("1ère intention : "))
            file.write(str("Oui\n"))
        if CheckVar3.get()==1:
            file.write(str("2ème intention : "))
            file.write(str("Oui\n"))
        if Rnbre.get()=='':
            print("Pas de réserves!")
            file.write(Rnbre.get() + '\n')
        file.write(str("Date of end : "))
        file.write(comboFinishDay.get())
        file.write('/' + comboFinishMonth.get() + '/')
        file.write(comboFinishYear.get())
        file.write(str('\n'))
        file.write(str("Signature : "))
        file.write(textSign.get())
        file.write(str('\n\n'))
    try:
        if os.path.getsize('./ttt/doc_ttt6/convres.json'):
            print("+ File 'convres' exist !")
            with open('./ttt/doc_ttt6/convres.json', 'r') as datafile:
                datastore = json.load(datafile)
                print(datastore)
            dataDose = datastore
            dataDose['data'].append({'Date' : textDate.get(), \
                'Date of introduction' : comboDay.get() + comboMonth.get() + \
                comboYear.get(), 'Date of end' : comboFinishDay.get() + \
                '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
                'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
                'Reserve' : CheckVar1.get(), 'First-line' : CheckVar2.get(), \
                'Second-line' : CheckVar3.get(), 'Number/24h' : Rnbre.get()})
            if textTreat.get() == "":
                print("---No value 'Treatment' introduced---")
            else:
                print("---Ok value 'Treatment' introduced---")
                with open('./ttt/doc_ttt6/convres.json', 'w') as datafile2:
                    json.dump(dataDose, datafile2, indent=4)
    except FileNotFoundError as outcom:
        print('+ Sorry, file convres.json not exist !')
        print(str(outcom))
        print("+ File convres.json created !")
        dataDose = {}
        dataDose['data'] = []
        dataDose['data'].append({'Date' : textDate.get(), \
            'Date of introduction' : comboDay.get() + comboMonth.get() + \
            comboYear.get(), 'Date of end' : comboFinishDay.get() + \
            '/' + comboFinishMonth.get() + '/' + comboFinishYear.get(), \
            'Treatment' : textTreat.get(), 'Dosage' : textDosage.get(), \
            'Reserve' : CheckVar1.get(), 'First-line' : CheckVar2.get(), \
            'Second-line' : CheckVar3.get(), 'Number/24h' : Rnbre.get()})
        if textTreat.get() == "":
            print("+ No value 'Treatment' introduced---")
        elif CheckVar2.get() == 0:
            print("+ There is not First-line reserve marked---")
        elif CheckVar2.get() != 0:
            print("+ There is First-line reserve marked---")
        elif CheckVar3.get() == 0:
            print("+ There is not Second-line reserve marked---")
        elif CheckVar3.get() != 0:
            print("+ There is Second-line reserve marked---")
        else:
            print("Problem with reserve registration")
        print("+ Ok, value 'Treatment' introduced---")
        with open('./ttt/doc_ttt6/convres.json', 'w') as datafile:
            json.dump(dataDose, datafile, indent=4)

app = tk.Tk()
app.title("Introduction of treatement (ttt)")
app.configure(bg='RoyalBlue4')

textLab = tk.Label(app, text="Introduction of treatement (ttt)",
    font=('Times 22 bold'), fg='aquamarine', bg='RoyalBlue4')
textLab.grid(row=0, column=0, columnspan=4, pady=10)

labelallergy=tk.Label(app, text="Allergy",
    font='Arial 18 bold', fg='coral', bg='RoyalBlue4')
labelallergy.grid(row=1, column=0, columnspan=4)

# To read allergy for entry widget
with open('./allergy/allergyfile6.txt', 'r') as filename2:
    line1=filename2.readline()
    line2=filename2.readline()
    line3=filename2.readline()
    line4=filename2.readline()
    line5=filename2.readline()
    line6=filename2.readline()
    line7=filename2.readline()

entrytext=tk.StringVar()
entrytext.set(line1 + ', ' + line3 + ', ' + line5 + ', ' + line7)
entryName=tk.Entry(app, textvariable=entrytext, width=60)
entryName.grid(row=2, column=0, columnspan=4, pady=10)

LabDate = tk.Label(app, text="Date : ", width=20, font=12,
    fg='cyan', bg='RoyalBlue4', anchor='e')
LabDate.grid(row=3, column=0)

LabHour = tk.Label(app, text="Hour : ", width=20, font=12,
    fg='cyan', bg='RoyalBlue4', anchor='e')
LabHour.grid(row=4, column=0)

LabName = tk.Label(app, text="Patient's name : ", width=20, font=12,
    fg='cyan', bg='RoyalBlue4', anchor='e')
LabName.grid(row=5, column=0)

LabTreat = tk.Label(app, text='Name of drug : ', width=20, 
    font=12, fg='cyan', bg='RoyalBlue4', anchor='e')
LabTreat.grid(row=6, column=0)

LabDose = tk.Label(app, text="Dose : ", width=20, font=12,
    fg='cyan', bg='RoyalBlue4', anchor='e')
LabDose.grid(row=7, column=0)

textDate = tk.Entry(app)
time_string = tk.IntVar()
textDate = tk.Entry(textvariable=time_string,
    highlightbackground='grey', bd=4)
time_string.set(time.strftime("%d/%m/%Y"))
textDate.grid(row=3, column=1)

textHour = tk.Entry(app)
time_Htring = tk.IntVar()
textHour = tk.Entry(textvariable=time_Htring,
    highlightbackground='grey', bd=4)
time_Htring.set(time.strftime("%H:%M:%S"))
textHour.grid(row=4, column=1)

# To read name of patient for entry widget
with open('./newpatient/entryfile6.txt', 'r') as filename:
    line1=filename.readline()

textName = tk.Entry(app)
name_text = tk.StringVar()
textName = tk.Entry(textvariable=name_text,
    highlightbackground='grey', bd=4)
name_text.set(line1)
textName.grid(row=5, column=1)

textTreat = tk.Entry(app)
ttt_name = tk.StringVar()
textTreat = tk.Entry(textvariable=ttt_name,
    highlightbackground='grey', bd=4)
ttt_name.set("Drug")
textTreat.grid(row=6, column=1)

textDosage = tk.Entry(app)
tttDosage = tk.StringVar()
textDosage = tk.Entry(textvariable=tttDosage,
    highlightbackground='grey', bd=4)
tttDosage.set("mcg/ml/mg/UI/gttes")
textDosage.grid(row=7, column=1)

deleteTreat = tk.Entry(app)
delete_text = tk.StringVar()
delete_text.set("Enter ttt to stop")
deleteTreat = tk.Entry(textvariable=delete_text,
    highlightbackground='red', bd=4)
deleteTreat.grid(row=3, column=2)
# TTT to stop
buttStopttt = tk.Button(app, text="Stop ttt", width=10, fg='yellow',
    bg='red', bd=3, highlightbackground='RoyalBlue4',
    activebackground='coral', command=deleteTreatment)
buttStopttt.grid(row=3, column=3, padx=10)

deleteRes = tk.Entry(app)
delete_res = tk.StringVar()
delete_res.set("Enter R to stop")
deleteRes = tk.Entry(textvariable=delete_res,
    highlightbackground='red', bd=4)
deleteRes.grid(row=5, column=2)
# Reserves to stop
buttStopttt = tk.Button(app, text="Stop R", width=10, fg='yellow',
    bg='red', bd=3, highlightbackground='RoyalBlue4',
    activebackground='coral', command=deleteReserve, padx=10)
buttStopttt.grid(row=5, column=3)

buttShowttt = tk.Button(app, text="Show ttt", width=10, fg='cyan',
    bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
    activebackground='dark turquoise', command=showTreat)
buttShowttt.grid(row=7, column=2)

buttShowttt = tk.Button(app, text="Show R", width=10, fg='cyan',
    bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
    activebackground='dark turquoise', command=showReserve)
buttShowttt.grid(row=7, column=3)

textDateS = tk.Label(app, text="Processing start date :", 
    font=('Arial 14 bold'), fg='aquamarine', bg='RoyalBlue4', width=40, anchor='w')
textDateS.grid(row=8, column=0, columnspan=2, pady=10)

def changeDay():
    comboDay["values"] = ['01', '02', '03', '04',
                          '05', '06', '07', '08',
                          '09', '10', '11', '12',
                          '13', '14', '15', '15',
                          '16', '17', '18', '19',
                          '20', '21', '22', '23',
                          '24', '25', '26', '27',
                          '28', '29', '30', '31']

labelDay = tk.Label(app,
    text = "Choose the day :", font=12, fg='cyan', bg='RoyalBlue4')
labelDay.grid(row=9, column=0)

comboDay = ttk.Combobox(app,
    values=['01', '02', '03', '04',
            '05', '06', '07', '08',
            '09', '10', '11', '12',
            '13', '14', '15', '15',
            '16', '17', '18', '19',
            '20', '21', '22', '23',
            '24', '25', '26', '27',
            '28', '29', '30', '31'], postcommand=changeDay)
comboDay.bind("<<ComboboxSelected>>", callbackDay)
comboDay.grid(row=10, column=0, pady=10)

def changeMonth():
    comboMonth["values"] = [' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December']

labelMonth = tk.Label(app,
    text = "Choose the month :", font=12, fg='cyan', bg='RoyalBlue4')
labelMonth.grid(row=9, column=1)

comboMonth = ttk.Combobox(app,
    values=[' January',  
          ' February', 
          ' March', 
          ' April', 
          ' May', 
          ' June', 
          ' July', 
          ' August', 
          ' September', 
          ' October', 
          ' November', 
          ' December'], postcommand=changeMonth)
comboMonth.bind("<<ComboboxSelected>>", callbackMonth)
comboMonth.grid(row=10, column=1, pady=10)

def changeYear():
    comboYear["values"] = [' 2000', ' 2001', ' 2002', ' 2003',
                          ' 2004', ' 2005', ' 2006', ' 2007',
                          ' 2008', ' 2009', ' 2010', ' 2011',
                          ' 2012', ' 2013', ' 2014', ' 2015',
                          ' 2016', ' 2017', ' 2018', ' 2019',
                          ' 2020', ' 2021', ' 2022', ' 2023',
                          ' 2024', ' 2025', ' 2026', ' 2027',
                          ' 2028', ' 2029', ' 2030', ' 2031',
                          ' 2032', ' 2033', ' 2034', ' 2035']

labelYear = tk.Label(app,
    text = "Choose the year :", font=12, fg='cyan', bg='RoyalBlue4')
labelYear.grid(row=9, column=2)

comboYear = ttk.Combobox(app,
    values=[' 2000', ' 2001', ' 2002', ' 2003',
            ' 2004', ' 2005', ' 2006', ' 2007',
            ' 2008', ' 2009', ' 2010', ' 2011',
            ' 2012', ' 2013', ' 2014', ' 2015',
            ' 2016', ' 2017', ' 2018', ' 2019',
            ' 2020', ' 2021', ' 2022', ' 2023',
            ' 2024', ' 2025', ' 2026', ' 2027',
            ' 2028', ' 2029', ' 2030', ' 2031',
            ' 2032', ' 2033', ' 2034', ' 2035'], postcommand=changeYear)
comboYear.bind("<<ComboboxSelected>>", callbackYear)
comboYear.grid(row=10, column=2, pady=10)
comboYear.current(20)

# Date of finish
textDateF = tk.Label(app, text="Processing end date :", 
    font=('Arial 14 bold'), fg='aquamarine', bg='RoyalBlue4', width=40, anchor='w')
textDateF.grid(row=11, column=0, columnspan=2, pady=10)

def finishDay():
    comboFinishDay["values"] = ['01', '02', '03', '04',
                                '05', '06', '07', '08',
                                '09', '10', '11', '12',
                                '13', '14', '15', '15',
                                '16', '17', '18', '19',
                                '20', '21', '22', '23',
                                '24', '25', '26', '27',
                                '28', '29', '30', '31']

labelFinishDay = tk.Label(app,
    text = "Choose the day :", font=12, fg='cyan', bg='RoyalBlue4')
labelFinishDay.grid(row=12, column=0)

comboFinishDay = ttk.Combobox(app,
    values=['01', '02', '03', '04',
            '05', '06', '07', '08',
            '09', '10', '11', '12',
            '13', '14', '15', '15',
            '16', '17', '18', '19',
            '20', '21', '22', '23',
            '24', '25', '26', '27',
            '28', '29', '30', '31'], postcommand=finishDay)
comboFinishDay.bind("<<ComboboxSelected>>", callbackFinishDay)
comboFinishDay.grid(row=13, column=0, pady=10)

def finishMonth():
    comboFinishMonth["values"] = ['01',  
                                '02', 
                                '03', 
                                '04', 
                                '05', 
                                '06', 
                                '07', 
                                '08', 
                                '09', 
                                '10', 
                                '11', 
                                '12']

labelMonth = tk.Label(app,
    text = "Choose the month :", font=12, fg='cyan', bg='RoyalBlue4')
labelMonth.grid(row=12, column=1)

comboFinishMonth = ttk.Combobox(app,
    values=['01',  
            '02', 
            '03', 
            '04', 
            '05', 
            '06', 
            '07', 
            '08', 
            '09', 
            '10', 
            '11', 
            '12'], postcommand=finishMonth)
comboFinishMonth.bind("<<ComboboxSelected>>", callbackFinishMonth)
comboFinishMonth.grid(row=13, column=1, pady=10)

def finishYear():
    comboFinishYear["values"] = ['2020', '2021', '2022', '2023',
                                 '2024', '2025', '2026', '2027',
                                 '2028', '2029', '2030', '2031',
                                 '2032', '2033', '2034', '2035']

labelFinishYear = tk.Label(app,
    text = "Choose the year :", font=12, fg='cyan', bg='RoyalBlue4')
labelFinishYear.grid(row=12, column=2)

comboFinishYear = ttk.Combobox(app,
    values=['2020', '2021', '2022', '2023',
            '2024', '2025', '2026', '2027',
            '2028', '2029', '2030', '2031',
            '2032', '2033', '2034', '2035'], postcommand=finishYear)
comboFinishYear.bind("<<ComboboxSelected>>", callbackFinishYear)
comboFinishYear.grid(row=13, column=2, pady=10)
comboFinishYear.current(0)

checkLab = tk.Label(app, text="Doses :", font=('Arial 14 bold'), 
    fg='aquamarine', bg='RoyalBlue4')
checkLab.grid(row=14, column=0, pady=10)

DosaLab = tk.Label(app, text="Unity :", font=('Arial 14 bold'), 
    fg='aquamarine', bg='RoyalBlue4')
DosaLab.grid(row=14, column=2, pady=10)

# CheckBox
CheckVarMatin = tk.IntVar()
Cma = tk.Checkbutton(app, text="Morning --->", fg='navy', 
    bg='cyan', variable=CheckVarMatin, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Cma.grid(row=16, column=0)

LabDose = tk.Label(app, text='Morning dose : ', font=12,
    width=20, fg='cyan', bg='RoyalBlue4')
LabDose.grid(row=16, column=1)

Entmatin = tk.Entry(app)
Entmatin = tk.Entry(highlightbackground='grey', bd=4)
Entmatin.grid(row=16, column=2)

CheckVarMidi = tk.IntVar()
Cmi = tk.Checkbutton(app, text="Noon --->", fg='navy', 
    bg='cyan', variable=CheckVarMidi, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Cmi.grid(row=17, column=0)

LabDose = tk.Label(app, text='Take of noon : ', font=12, 
    width=20, fg='cyan', bg='RoyalBlue4')
LabDose.grid(row=17, column=1)

Entmidi = tk.Entry(app)
Entmidi = tk.Entry(highlightbackground='grey', bd=4)
Entmidi.grid(row=17, column=2)

CheckVarSoir = tk.IntVar()
Csoir = tk.Checkbutton(app, text="Evening --->", fg='navy', 
    bg='cyan', variable=CheckVarSoir, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Csoir.grid(row=18, column=0)

LabDose = tk.Label(app, text='Evening outlet : ', font=12,
    width=20, fg='cyan', bg='RoyalBlue4')
LabDose.grid(row=18, column=1)

Entsoir = tk.Entry(app)
Entsoir = tk.Entry(highlightbackground='grey', bd=4)
Entsoir.grid(row=18, column=2)

CheckVarNuit = tk.IntVar()
Cnuit = tk.Checkbutton(app, text="Night --->", fg='navy', 
    bg='cyan', variable=CheckVarNuit, 
    onvalue=1, offvalue=0, height=1, 
    width=15, anchor='w')
Cnuit.grid(row=19, column=0)

# Entry nbre de x/24h
LabDose = tk.Label(app, text='Take of night : ', font=12,
    width=20, fg='cyan', bg='RoyalBlue4')
LabDose.grid(row=19, column=1)

Entnuit = tk.Entry(app)
Entnuit = tk.Entry(highlightbackground='grey', bd=4)
Entnuit.grid(row=19, column=2)

CheckVar1 = tk.IntVar()
C1 = tk.Checkbutton(app, text="Reserve", fg='navy', 
    bg='pale green', variable=CheckVar1, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor='w')
C1.grid(row=20, column=0, pady=10)

CheckVar2 = tk.IntVar()
C2 = tk.Checkbutton(app, text="First-line", fg='navy', 
    bg='pale green', variable=CheckVar2, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor='w')
C2.grid(row=20, column=1, pady=10)

CheckVar3 = tk.IntVar()
C3 = tk.Checkbutton(app, text="Second-line", fg='navy', 
    bg='pale green', variable=CheckVar3, 
    onvalue=1, offvalue=0, height=1, 
    width=20, anchor='w')
C3.grid(row=20, column=2, pady=10)

# Buttons with functions
buttCopy = tk.Button(app, text="Save ttt", width=10, fg='yellow',
    bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
    activebackground='dark turquoise', command=copyTttMess)
buttCopy.grid(row=21, column=0)

buttCopy = tk.Button(app, text="Save R", width=10, fg='yellow',
    bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
    activebackground='dark turquoise', command=copyResMess)
buttCopy.grid(row=22, column=0)

LabelR = tk.Label(app, text='Number of R/24h : ', font=12, 
    width=20, fg='cyan', bg='RoyalBlue4')
LabelR.grid(row=21, column=1)

Rnbre = tk.Entry(app)
Rnbre = tk.Entry(highlightbackground='grey', bd=4)
Rnbre.grid(row=21, column=2)

LabSign = tk.Label(app, text='Signature :', font=12, 
    width=15, fg='red', bg='pale green')
LabSign.grid(row=22, column=1, pady=10)

textSign = tk.Entry(app)
textSign = tk.Entry(highlightbackground='grey', bd=4)
textSign.grid(row=22, column=2, pady=10)

# Buttons with functions
buttQuit = tk.Button(app, text="Quit", width=10, fg='white',
    bg='RoyalBlue3', bd=3, highlightbackground='RoyalBlue4', 
    activebackground='dark turquoise', command=quit)
buttQuit.grid(row=22, column=3)

app.mainloop()
