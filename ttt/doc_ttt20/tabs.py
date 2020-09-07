#!/usr/bin/python3
# -*-encoding:Utf-8-*-


from tkinter import *
from string import ascii_lowercase
import json
import os


# To create list of start date
with open('./ttt/doc_ttt20/convdose.json') as file:
    data = json.load(file)
for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))

data_liststart = []
for value in zip(value):
    data_liststart.append(value[0]['Date of introduction'])

with open('./ttt/doc_ttt20/data_start.json', 'a+') as datafile:
    json.dump(data_liststart, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nListstart = Start of process :")
print("--------------")
fileStart = open('./ttt/doc_ttt20/data_start.json')
liststart = json.load(fileStart)

for start in liststart:
    print("liststart: " + start)

# To create list of end date
with open('./ttt/doc_ttt20/convdose.json') as file:
    data = json.load(file)
for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))

data_listend = []
for value in zip(value):
    data_listend.append(value[0]['Date of end'])

with open('./ttt/doc_ttt20/data_end.json', 'a+') as datafile:
    json.dump(data_listend, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nListend = End of process :")
print("--------------")
filend = open('./ttt/doc_ttt20/data_end.json')
listend = json.load(filend)

for end in listend:
    print("listend: " + end)

# To create list of ttt
with open('./ttt/doc_ttt20/convdose.json') as file:
    data = json.load(file)
for (key, value) in data.items():
    print("Key: " + key)
    print("Valeur: " + str(value))

data_list1 = []
for value in zip(value):
    data_list1.append(value[0]['Treatment'])

with open('./ttt/doc_ttt20/data_ttt.json', 'a+') as datafile:
    json.dump(data_list1, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nListe1 = ttt :")
print("--------------")
fileA = open('./ttt/doc_ttt20/data_ttt.json')
list1 = json.load(fileA)

for tttintro in list1:
    print("list1: " + tttintro)

# To create list of dose
data_list2 = []
for value in zip(value):
    data_list2.append(value[0]['Dosage'])

with open('./ttt/doc_ttt20/data_dose.json', 'a+') as datafile:
    json.dump(data_list2, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList2 = Dosage :")
print("--------------------")
fileB = open('./ttt/doc_ttt20/data_dose.json')
list2 = json.load(fileB)

for dose in list2:
    print("list2: " + dose)

# To create list of Morning
data_list3 = []
for value in zip(value):
    data_list3.append(value[0]['Matin'])

with open('./ttt/doc_ttt20/data_matin.json', 'a+') as datafile:
    json.dump(data_list3, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList3 = Matin :")
print("--------------------")
fileC = open('./ttt/doc_ttt20/data_matin.json')
list3 = json.load(fileC)

for morn in list3:
    print("list3: " + morn)

# To create list of noon
data_list4 = []
for value in zip(value):
    data_list4.append(value[0]['Midi'])

with open('./ttt/doc_ttt20/data_midi.json', 'a+') as datafile:
    json.dump(data_list4, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList4 = Midi :")
print("--------------------")
fileD = open('./ttt/doc_ttt20/data_midi.json')
list4 = json.load(fileD)

for noon in list4:
    print("list4: " + noon)

# To create list of evening
data_list5 = []
for value in zip(value):
    data_list5.append(value[0]['Soir'])

with open('./ttt/doc_ttt20/data_soir.json', 'a+') as datafile:
    json.dump(data_list5, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList5 = Soir :")
print("--------------------")
fileE = open('./ttt/doc_ttt20/data_soir.json')
list5 = json.load(fileE)

for eve in list5:
    print("list5: " + eve)

# To create list of night
data_list6 = []
for value in zip(value):
    data_list6.append(value[0]['Nuit'])

with open('./ttt/doc_ttt20/data_nuit.json', 'a+') as datafile:
    json.dump(data_list6, datafile, indent=4)

for (key, value) in data.items():
    print(key, value)
    print("\n")

print("\nList6 = Nuit :")
print("--------------------")
fileF = open('./ttt/doc_ttt20/data_nuit.json')
list6 = json.load(fileF)

for nightm in list6:
    print("list6: " + nightm)

print("\nThat seems correct!\n")

class app(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.text_name=StringVar()
        self.labelo=Label(master, text="Treatments for : ", width=20,
            font='Times 18 bold', fg='cyan', bg='gray17')
        self.labelo.grid(sticky='w', row=0, column=0, padx=30, pady=5)
        with open('./newpatient/entryfile20.txt', 'r') as file:
            line1=file.readline()
        self.text_name.set(line1)
        self.entryName=Entry(master, textvariable=self.text_name)
        self.entryName.grid(sticky='w', row=0, column=0, padx=250, pady=5)
        self.labelallergy=Label(master, text="Allergy : ",
            font='Arial 18 bold', fg='coral', bg='gray17')
        self.labelallergy.grid(row=0, column=0, padx=10, pady=5)
        with open('./allergy/allergyfile20.txt', 'r') as allerfile:
            lineA1=allerfile.readline()
            lineA2=allerfile.readline()
            lineA3=allerfile.readline()
            lineA4=allerfile.readline()
            lineA5=allerfile.readline()
            lineA6=allerfile.readline()
            lineA7=allerfile.readline()
        self.text_all=StringVar()
        self.text_all.set(lineA1 + ', ' + lineA3 + ', ' + lineA5 + ', ' + lineA7)
        self.Entryall=Entry(master, textvariable=self.text_all, width=60)
        self.Entryall.grid(sticky='e', row=0, column=0, padx=120, pady=5)
        self.buttQuit=Button(master, text="Close", bg='gray30', fg='cyan', command=quit)
        self.buttQuit.grid(sticky='e', row=0, column=0, padx=10)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        To create table
        """
        self.entries = {}
        self.tableheight = 16
        self.tablewidth = 8
        counter = 0
        for row in range(self.tableheight):
            for column in range(self.tablewidth):
                self.entries[counter] = Entry(self, width=20, fg='cyan', bg='black')
                self.entries[counter].grid(row=row, column=column)
                counter += 1
        # Exemple
        #self.entries[0].insert(0, list1[0])
        self.entries[0].insert(0, 'Start of process')
        self.entries[1].insert(0, 'Date of end')
        self.entries[2].insert(0, 'Treatment')
        self.entries[3].insert(0, 'Dosage')
        self.entries[4].insert(0, 'Morning')
        self.entries[5].insert(0, 'Noon')
        self.entries[6].insert(0, 'Evening')
        self.entries[7].insert(0, 'Night')
        try:
            if list1[:] is not False:
                self.entries[8].insert(0, liststart[0])
                self.entries[9].insert(0, listend[0])
                self.entries[10].insert(0, list1[0])
                self.entries[11].insert(0, list2[0])
                self.entries[12].insert(0, list3[0])
                self.entries[13].insert(0, list4[0])
                self.entries[14].insert(0, list5[0])
                self.entries[15].insert(0, list6[0])

                self.entries[16].insert(0, liststart[1])
                self.entries[17].insert(0, listend[1])
                self.entries[18].insert(0, list1[1])
                self.entries[19].insert(0, list2[1])
                self.entries[20].insert(0, list3[1])
                self.entries[21].insert(0, list4[1])
                self.entries[22].insert(0, list5[1])
                self.entries[23].insert(0, list6[1]) 

                self.entries[24].insert(0, liststart[2])
                self.entries[25].insert(0, listend[2])
                self.entries[26].insert(0, list1[2])
                self.entries[27].insert(0, list2[2])
                self.entries[28].insert(0, list3[2])
                self.entries[29].insert(0, list4[2])
                self.entries[30].insert(0, list5[2])
                self.entries[31].insert(0, list6[2])

                self.entries[32].insert(0, liststart[3])
                self.entries[33].insert(0, listend[3])
                self.entries[34].insert(0, list1[3])
                self.entries[35].insert(0, list2[3])
                self.entries[36].insert(0, list3[3])
                self.entries[37].insert(0, list4[3])
                self.entries[38].insert(0, list5[3])
                self.entries[39].insert(0, list6[3])

                self.entries[40].insert(0, liststart[4])
                self.entries[41].insert(0, listend[4])
                self.entries[42].insert(0, list1[4])
                self.entries[43].insert(0, list2[4])
                self.entries[44].insert(0, list3[4])
                self.entries[45].insert(0, list4[4])
                self.entries[46].insert(0, list5[4])
                self.entries[47].insert(0, list6[4])

                self.entries[48].insert(0, liststart[5])
                self.entries[49].insert(0, listend[5])
                self.entries[50].insert(0, list1[5])
                self.entries[51].insert(0, list2[5])
                self.entries[52].insert(0, list3[5])
                self.entries[53].insert(0, list4[5])
                self.entries[54].insert(0, list5[5])
                self.entries[55].insert(0, list6[5])

                self.entries[56].insert(0, liststart[6])
                self.entries[57].insert(0, listend[6])
                self.entries[58].insert(0, list1[6])
                self.entries[59].insert(0, list2[6])
                self.entries[60].insert(0, list3[6])
                self.entries[61].insert(0, list4[6])
                self.entries[62].insert(0, list5[6])
                self.entries[63].insert(0, list6[6])

                self.entries[64].insert(0, liststart[7])
                self.entries[65].insert(0, listend[7])
                self.entries[66].insert(0, list1[7])
                self.entries[67].insert(0, list2[7])
                self.entries[68].insert(0, list3[7])
                self.entries[69].insert(0, list4[7])
                self.entries[70].insert(0, list5[7])
                self.entries[71].insert(0, list6[7])

                self.entries[72].insert(0, liststart[8])
                self.entries[73].insert(0, listend[8])
                self.entries[74].insert(0, list1[8])
                self.entries[75].insert(0, list2[8])
                self.entries[76].insert(0, list3[8])
                self.entries[77].insert(0, list4[8])
                self.entries[78].insert(0, list5[8])
                self.entries[79].insert(0, list6[8])

                self.entries[80].insert(0, liststart[9])
                self.entries[81].insert(0, listend[9])
                self.entries[82].insert(0, list1[9])
                self.entries[83].insert(0, list2[9])
                self.entries[84].insert(0, list3[9])
                self.entries[85].insert(0, list4[9])
                self.entries[86].insert(0, list5[9])
                self.entries[87].insert(0, list6[9])

                self.entries[88].insert(0, liststart[10])
                self.entries[89].insert(0, listend[10])
                self.entries[90].insert(0, list1[10])
                self.entries[91].insert(0, list2[10])
                self.entries[92].insert(0, list3[10])
                self.entries[93].insert(0, list4[10])
                self.entries[94].insert(0, list5[10])
                self.entries[95].insert(0, list6[10])

                self.entries[96].insert(0, liststart[11])
                self.entries[97].insert(0, listend[11])
                self.entries[98].insert(0, list1[11])
                self.entries[99].insert(0, list2[11])
                self.entries[100].insert(0, list3[11])
                self.entries[101].insert(0, list4[11])
                self.entries[102].insert(0, list5[11])
                self.entries[103].insert(0, list6[11])

                self.entries[104].insert(0, liststart[12])
                self.entries[105].insert(0, listend[12])
                self.entries[106].insert(0, list1[12])
                self.entries[107].insert(0, list2[12])
                self.entries[108].insert(0, list3[12])
                self.entries[109].insert(0, list4[12])
                self.entries[110].insert(0, list5[12])
                self.entries[111].insert(0, list6[12])

                self.entries[112].insert(0, liststart[13])
                self.entries[113].insert(0, listend[13])
                self.entries[114].insert(0, list1[13])
                self.entries[115].insert(0, list2[13])
                self.entries[116].insert(0, list3[13])
                self.entries[117].insert(0, list4[13])
                self.entries[118].insert(0, list5[13])
                self.entries[119].insert(0, list6[13])

                self.entries[120].insert(0, liststart[14])
                self.entries[121].insert(0, listend[14])
                self.entries[122].insert(0, list1[14])
                self.entries[123].insert(0, list2[14])
                self.entries[124].insert(0, list3[14])
                self.entries[125].insert(0, list4[14])
                self.entries[126].insert(0, list5[14])
                self.entries[127].insert(0, list6[14])
        except IndexError as infottt:
            print("End of medication reached, there are more tbas than ttt !", infottt)
        else:
            print("Error unknow")

os.remove('./ttt/doc_ttt20/data_ttt.json')
os.remove('./ttt/doc_ttt20/data_dose.json')
os.remove('./ttt/doc_ttt20/data_matin.json')
os.remove('./ttt/doc_ttt20/data_midi.json')
os.remove('./ttt/doc_ttt20/data_soir.json')
os.remove('./ttt/doc_ttt20/data_nuit.json')
os.remove('./ttt/doc_ttt20/data_start.json')
os.remove('./ttt/doc_ttt20/data_end.json')

prog = app()
prog.master.title('Medication')
prog.master.configure(bg='gray17')
prog.mainloop()
