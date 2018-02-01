import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
#Open file 
rb = xlrd.open_workbook('zp.xlsx')
#Select active sheet 
sheet = rb.sheet_by_index(0)
#Format names of economic sectors: make all letters in lower case, remove extra gaps and find the maximum wage in thе sector over the period 1995-2015
def max_value(s):
        data = ''
        l=0
        for row in range(1, sheet.nrows): #в цикле по количеству всех строк
                data = sheet.cell_value(row,0)
                clear_data = ' '.join(data.split())
                low_data = clear_data.lstrip().lower()
                if s == low_data:
                        l=1
                        value = 0 #значение по которому будем искать
                        for col in range (1, sheet.ncols):
                            data = sheet.cell_value(row,col) #получаем значение ячейки (row-строка, col-столбец)
                            if type (data) != float:
                                if data == 'NaN':
                                    pass
                            elif (value < data):
                                value = data
                        for col in range (1, sheet.ncols):
                                if value == sheet.cell_value(row,col):
                                       print ('Максимальная заработная плата по данному сектору экономики была в',int(sheet.cell_value(0,col)),'году и составила', value, 'рублей')
        if l == 0:
                print ('По указанному сектору экономики нет данных')
        return s
#Format names of economic sectors: make all letters in lower case, remove extra gaps and find the manimum wage in thе sector over the period 1995-2015
def min_value(s):
        data = ''
        for row in range(1, sheet.nrows): #в цикле по количеству всех строк
                data = sheet.cell_value(row,0)
                clear_data = ' '.join(data.split())
                low_data = clear_data.lstrip().lower()
                if s == low_data:
                        value = sheet.cell_value(row,1)#значение по которому будем искать (значение первой колонки данной строки)
                        for col in range (1, sheet.ncols):
                            data = sheet.cell_value(row,col) #получаем значение ячейки (row-строка, col-столбец)
                            if type (data) != float:
                                if data == 'NaN':
                                    pass
                            elif (value > data):
                                value = data
                        for col in range (1, sheet.ncols):
                                if value == sheet.cell_value(row,col):
                                        print ('Минимальная заработная плата по данному сектору экономики была в',int(sheet.cell_value(0,col)),'году и составила', value, 'рублей')
        
        return s
#The graph of the dynamics of values in the sector over the period 1995-2015
def graph(s):
        masx = []
        masy = []
        for col in range (1, sheet.ncols):
                for row in range(1, sheet.nrows):
                        data = sheet.cell_value(row,0)
                        clear_data = ' '.join(data.split())
                        low_data = clear_data.lstrip().lower()
                        if s == low_data:
                        #if s == sheet.cell_value(row,0):
                            val = sheet.cell_value(row,col)
                            masy.append(val)
                data = int (sheet.cell_value(0,col))
                masx.append(int (data))
        x = (masx)
        y = (masy)
        fig, ax = plt.subplots()
        ax.plot(x, y, color="blue")
        ax.set_title('The dinamic values of wages by years')
        ax.set_xlabel("years")
        ax.set_ylabel("wages")
        plt.show()
        return s
print ('Укажите сектор экономики')
k = input ()
#Format the string: make all letters in lower case, remove extra spaces
clear_k = ' '.join(k.split())
s = clear_k.lstrip().lower()
max_value(s)
min_value(s)
graph(s)

