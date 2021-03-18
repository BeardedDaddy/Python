import openpyxl

excel_files = ['"C:\Users\owner\Documents\AHU Supply Return Daily Report.xlsm"']

values = []

for files in excel_files:
    workbook = openpyxl_load_workbook(file)
    worksheet = workbook[""]
    cell_value = worksheet [''].value
    values.append(cell_value)

    print(cell_value)