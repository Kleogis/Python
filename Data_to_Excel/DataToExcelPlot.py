# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:22:36 2020

@author: Kleogis
"""

import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('chart_scatter.xlsx')
worksheet = workbook.add_worksheet()

start = 190
end = 822

j = 0

for i in range (start, end):
    if i % 2 == 0:
        worksheet.write(j, 0, i)
        j = j + 1

k = 0
for line in open ('C:/Users/Kleogis/Desktop/Working_Scripts/ForRittik/6.DX'):
    for i in range (start, end):
       if line.startswith(str(start)):
          line.split()
          worksheet.write(k, 1, float(line[4:]))
          k = k + 1
          start = start + 2




# Create a chart object.
chart1 = workbook.add_chart({'type': 'scatter'})

# Configure the series of the chart.
chart1.add_series({
   'categories': ['Sheet1', 0, 0, 315, 0],
   'values':     ['Sheet1', 0, 1, 315, 1],
})      


# Insert the chart into the worksheet.
worksheet.insert_chart('K2', chart1)

# Close the Pandas Excel writer and output the Excel file.
workbook.close()