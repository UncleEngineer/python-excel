#fullname.py
from openpyxl import Workbook

excelfile = Workbook()
sheet = excelfile.active
allname = ['Prayut',
           'Taksin',
           'Parina',
           'Mongkolkit',
           'Prawit',
           'Tanatorn',
           'Chatchat',
           'Sudarat',
           'Anuthin',
           'Somchai']

checkname = {} #นับว่าแต่ละตัวอักษรมีเท่าไร

for nm in allname:
    #print(nm[0])

    if nm[0] not in checkname.keys():
        checkname[nm[0]] = 1
        sheet[nm[0]+'1'] =  nm
    else:
        checkname[nm[0]] = checkname[nm[0]] + 1
        sheet[nm[0] + str(checkname[nm[0]])] = nm

print(checkname)

excelfile.save('Allname.xlsx')
        
        


