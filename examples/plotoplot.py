#!/usr/bin/python3
# -*- coding:utf-8 -*-


import matplotlib
from matplotlib import dates
import matplotlib.pyplot as plt
import datetime


"""
list1 and list2 from file convert_kg.py ...
"""

#list3 = [int(list2) for list2 in list2]
list2 = list(map(float, list2))
list1 = list(map(str, list1))

converted_dates = list(map(datetime.datetime.strptime, list1, len(list1)*['%d-%m-%Y']))
x_axis = converted_dates
formatter = dates.DateFormatter('%d-%m-%Y')
y_axis = list2
show_grid = True
with plt.style.context('dark_background'):
    plt.plot(x_axis, y_axis, '-')
    ax = plt.gcf().axes[0] 
    ax.xaxis.set_major_formatter(formatter)
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg per date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)
    plt.gcf().autofmt_xdate(rotation=25)

    plt.show()


import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates

"""
list1 and list2 from file convert_kg.py ...
"""

list2 = list(map(float, list2))
list1 = list(map(str, list1))

# first example
converted_dates = matplotlib.dates.datestr2num(list1)
print(converted_dates)

show_grid = True
with plt.style.context('dark_background'):
    x_axis = (converted_dates)
    y_axis = range(0,8)
    plt.plot_date( x_axis, y_axis, '-' )
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg per date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)

    plt.show()


import matplotlib.pyplot as plt


"""
list1 and list2 from file convert_kg.py ...
"""


# or seaborn-darkgrid
show_grid = True
with plt.style.context('dark_background'):
    plt.plot(list1, list2)
    plt.ylabel('Kg')
    plt.xlabel('Dates')
    plt.title('Kg per date')
    plt.xticks(rotation=45)
    plt.grid(show_grid)

    plt.show()


import datetime 
import matplotlib.pyplot as plt 
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import AutoDateFormatter
from matplotlib.dates import date2num 


"""
list1 and list2 from file convert_kg.py ...
"""


print(list1[0])

list_data=str(list1[0])

list_convert = datetime.datetime.strptime(list_data, "%d-%m-%Y")
int_date = date2num(list_convert)

print(int_date)

figure, axes = plt.subplots() 
axes.bar(int_date, list2, label ="", color ="cyan") 

locator = AutoDateLocator() 
axes.xaxis.set_major_locator(locator) 
axes.xaxis.set_major_formatter(AutoDateFormatter(locator))

# apply autoformatter for displaying of dates 
min_date = date2num(datetime.datetime.strptime('01-01-20', "%d-%m-%Y")) 
max_date = date2num(datetime.datetime.strptime('28-12-20', "%d-%m-%Y")) 
axes.set_xlim([min_date, max_date]) 
figure.autofmt_xdate() 
  
# show plot:  
plt.show()
