import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
#открываем файл
rb = xlrd.open_workbook('zp.xlsx')
#выбираем активный лист
sheet = rb.sheet_by_index(0)
#Выбираем информацию по нужному сектору экономики
print ('Укажите сектор экономики')
s = input ()
l = 0
for row in range(1, sheet.nrows): #в цикле по количеству всех строк
    if s == sheet.cell_value(row,0):
        #Находим максимальную заработную плату в данном секторе экономики за период 1995-2015
        l = 1
        value = 0 #значение по которому будем искать
        maximum = []
        for col in range (1, sheet.ncols):
            data = sheet.cell_value(row,col) #получаем значение ячейки (row-строка, col-столбец)
            if type (data) != float:
                if data == 'NaN':
                    pass
            elif (value < data):
                value = data
        maximum.append(value)
        for col in range (0, sheet.ncols):
            for row in range(1, sheet.nrows):
                for i in range (0, len(maximum)):
                    if maximum[i] == sheet.cell_value(row,col):
                       print ('Максимальная заработная плата по данному сектору экономики была в',int(sheet.cell_value(0,col)),'году и составила', maximum[i], 'рублей')
if l == 0:
    print ('По указанному сектору экономики нет данных')
#Находим минимальную заработную плату в данном секторе экономики за период 1995-2015
for row in range(1, sheet.nrows): #в цикле по количеству всех строк
    if s == sheet.cell_value(row,0):
        value = 1000000 #значение по которому будем искать
        minimum = []
        for col in range (1, sheet.ncols):
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
                       print ('Минимальная заработная плата по данному сектору экономики была в',int(sheet.cell_value(0,col)),'году и составила', minimum[k], 'рублей')
#Построим график динамики значений по данному сектору экономики за период 1995-2015
masx = []
masy = []
for col in range (1, sheet.ncols):
    for row in range(1, sheet.nrows):
        if s == sheet.cell_value(row,0):
            val = sheet.cell_value(row,col)
            masy.append(val)
    data = int (sheet.cell_value(0,col))
    masx.append(int (data))
print (masx)
print (masy)

x = (masx)
y = (masy)
fig, ax = plt.subplots()
ax.plot(x, y, color="blue")
ax.set_title('The dinamic values of wages by years')
ax.set_xlabel("years")
ax.set_ylabel("wages")
plt.show()

