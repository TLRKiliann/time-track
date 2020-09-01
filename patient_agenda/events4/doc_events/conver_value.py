#!/usr/bin/python3
# -*- coding:utf-8 -*-


import os
import json
import subprocess


try:
    with open('./patient_agenda/events4/doc_events/patient_rdv.json') as file:
        data=json.load(file)
except FileNotFoundError as fileout:
    print("File 4 patient_rdv.json not created", fileout)

for value in data:
    print(value)

data_list1 = []
for value in data:
    data_list1.append(value[1])

data_day = data_list1[0]
data_month = data_list1[1]
data_year = data_list1[2]

try:
    if data_month < 10:
        extradala = '0' +''+ str(data_month)
    elif data_month >= 10:
        extradala = str(data_month)
    else:
        pass
except ValueError as valout:
    print("Value is a problem", valout)

initword = "Appointment set for :"
final_data =  initword +' '+ str(data_day) +'/'+ extradala +'/'+ str(data_year) +' :'
print(final_data)

try:
    if os.path.getsize('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json'):
        print("+ File 'value' exist !")   
        with open('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json','w') as partytime:
            json.dump(final_data, partytime)
except FileNotFoundError as msg:
    print("File doesn't exist, but it has been created !")
    with open('./patient_agenda/events4/doc_events/fix_agenda/patient_value.json','w') as partyleft:
    	json.dump(final_data, partyleft)

subprocess.call('./patient_agenda/events4/doc_events/fix_agenda/extend_agenda.py')
