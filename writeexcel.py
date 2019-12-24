#writeexcel.py
from openpyxl import Workbook

excelfile = Workbook() #สร้างไฟล์ excel ใน python

sheet = excelfile.active #เลือก worksheet ที่กำลังเปิดอยู่

sheet['C3'] = 'Hello'

sheet.cell(row=3,column=4).value = 'world'

#data = ['Uncle',100,'100']
#sheet.append(data)

excelfile.save('Result.xlsx')
print('Done!')

