import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
"""Open file
"""
rb = xlrd.open_workbook('zp.xlsx')
"""Select active sheet
"""
sheet = rb.sheet_by_index(0)


def main():
    lst = []
    maximum = max_value(lst)
    minimum = min_value(lst)
    graph(lst)


def max_value(lst):
    """Find the maximum value by sector in each year
    """
    lst = []
    print('Максимальное значение по секторам экономики в каждом году')
    for col in range(1, sheet.ncols):
        value = sheet.cell_value(1, col)
        for row in range(1, sheet.nrows):
            data = sheet.cell_value(row, col)
            if type(data) != float:
                if data == 'NaN':
                    pass
            elif (value < data):
                value = data
        lst.append(value)
    for col in range(0, sheet.ncols):
        for row in range(1, sheet.nrows):
            for i in range(0, len(lst)):
                if lst[i] == sheet.cell_value(row, col):
                    print (
                        'Год: ', int(sheet.cell_value(0, col)),
                        'сектор экономики: ', sheet.cell_value(row, 0),
                        'значение: ', lst[i])
    return lst


def min_value(lst):
    """Find the minimum value by sector in each year
    """
    lst = []
    print('Минимальное значение по секторам экономики в каждом году')
    for col in range(1, sheet.ncols):
        value = sheet.cell_value(1, col)
        for row in range(1, sheet.nrows):
            data = sheet.cell_value(row, col)
            if type(data) != float:
                if data == 'NaN':
                    pass
            elif (value > data):
                value = data
        lst.append(value)
    for col in range(0, sheet.ncols):
        for row in range(1, sheet.nrows):
            for i in range(0, len(lst)):
                if lst[i] == sheet.cell_value(row, col):
                    print (
                        'Год: ', int(sheet.cell_value(0, col)),
                        'сектор экономики: ', sheet.cell_value(row, 0),
                        'значение: ', lst[i])
    return lst

            
def graph(lst):
    N = 17
    lst = []
    max_means = max_value(lst)
    """the x locations for the groups
    """
    ind = np.arange(N)
    """the width of the bars
    """
    width = 0.5
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, max_means, width, color='g')
    min_means = min_value(lst)
    rects2 = ax.bar(ind, min_means, width, color='r')
    """add some text for labels, title and axes ticks
    """
    ax.set_ylabel('Wages')
    ax.set_title('The highest and lowest wages by years')
    ax.set_xticks(ind)
    ax.set_xticklabels((
        '1995 ', '2000 ', '2001 ', '2002 ', '2003 ', '2004 ', '2005 ',
        '2006 ', '2007 ', '2008 ', '2009 ', '2010 ', '2011 ', '2012 ', '2013 ',
        '2014 ', '2015 '))
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
    return lst

if __name__ == "__main__":
        main()
