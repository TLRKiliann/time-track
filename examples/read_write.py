#!/usr/bin/python3
# -*- coding:utf-8 -*-


# to read one file and write in 2 files :
magicword = regexpi_var.get()
with open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'r') as fr:
    with open('./patient_agenda/events/doc_events/fix_agenda/modifrdv.txt', 'a+') as fw1:
        with open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'a+') as fw2:
        for line in fr.readlines():
            if magicword in line:
                fw1.writelines(str("+++ Changes about rdv +++\n"))
                fw1.writelines(textBox.get("0.0", "end-1c") + "\n")
                fw2.writelines(str("+++ Changes about rdv +++\n"))
                fw2.writelines(textBox.get("0.0", "end-1c") + "\n")
                print("Modification finish")
                break
            else:
                print("None file has been writted")

# to read a file since a textbox :
mot = regexpi_var.get()
with open('./patient_agenda/events/doc_events/fix_agenda/fixed_rdv.txt', 'r') as textfile1:
    lines = textfile1.readlines()
    for i in range(len(lines)):
        line = lines[i]
        if mot in line:
            print("Nous y voici !") 
            print(lines[i])
            print(lines[i+1])
            textBox.insert(INSERT, lines[i])
            textBox.insert(INSERT, lines[i+1])
            textBox.insert(INSERT, lines[i+2])
