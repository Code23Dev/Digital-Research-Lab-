import openpyxl
excel_files = ['files path here']
values = ['C:\Users\laman\Desktop\excel\Section_1.xlsx']
for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['SalesOrders']
    cell_value = worksheet['G11'].value
    values.append(cell_value)

    print(cell_value)

##########################################
import openpyxl
excel_files = ['C:\Users\laman\Desktop\excel\Section_1.xlsx']
for file in excel_files:
    wb = openpyxl.load_workbook(file)
    worksheet = wb["SalesOrders"]
    worksheet['G46'] = '=AVERAGE(G3:G45)'
    wb.save(file)

