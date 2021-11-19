import openpyxl as xl
w=xl.load_workbook('t.xlsx')
sheet=w['Sheet1']
cell=sheet.cell(1,1)
print(cell.value)