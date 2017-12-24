import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
#открываем файл
rb = xlrd.open_workbook('zp.xlsx')
#выбираем активный лист
sheet = rb.sheet_by_index(0)
#Находим максимальное значение по секторам экономики в каждом году
value = 0 #значение по которому будем искать
lst = []
for col in range (1, sheet.ncols):
    for row in range(1, sheet.nrows): #в цикле по количеству всех строк 
        data = sheet.cell_value(row,col) #получаем значение ячейки (row-строка, col-столбец)
        if type (data) != float:
            if data == 'NaN':
                pass
        elif (value < data):
            value = data
    lst.append(value)
for col in range (0, sheet.ncols):
    for row in range(1, sheet.nrows):
        for i in range (0, len(lst)):
            if lst[i] == sheet.cell_value(row,col):
                print (int(sheet.cell_value(0,col)),sheet.cell_value(row,0), lst[i])
#Находим минимальное значение по секторам экономики в каждом году
value = 1000000 #значение по которому будем искать
minimum = []
for col in range (1, sheet.ncols):
    for row in range(1, sheet.nrows): #в цикле по количеству всех строк 
        data = sheet.cell_value(row,col) #получаем значение ячейки (row-строка, col-столбец)
        if type (data) != float:
            if data == 'NaN':
                pass
        elif (value > data):
            value = data
    minimum.append(value)
    value=1000000
for col in range (0, sheet.ncols):
    for row in range(1, sheet.nrows):
        for k in range (0, len(minimum)):
            if minimum[k] == sheet.cell_value(row,col):
                print (int(sheet.cell_value(0,col)),sheet.cell_value(row,0), minimum[k])
N = 17
max_means = (lst)

ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, max_means, width, color='g')

min_means = (minimum)
rects2 = ax.bar(ind, min_means, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Wages')
ax.set_title('The highest and lowest wages by years')
ax.set_xticks(ind)
ax.set_xticklabels(('1995 ', '2000 ', '2001 ', '2002 ', '2003 ', '2004 ', '2005 ', '2006 ', '2007 ', '2008 ', '2009 ', '2010 ', '2011 ', '2012 ', '2013 ', '2014 ', '2015 '))
ax.legend((rects1[0], rects2[0]), ('Max', 'Min'))

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
