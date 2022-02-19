import openpyxl

excel_files = ["C:\Users\grevy\OneDrive\Documents\DCI Work Orders\ 2021 Maintenance\Quarter 2\April 2021 Maintenance\April 2021 Daily Reports\AHU Supply Return Daily Report WO# 02164 April 15 Thursday.xlsm"]

values = []

for file in excel_files:
    workbook = openpyxl.load_workbook(files)
    worksheet = workbook['AHU Supply Return Daily Report']
    cell_value = worksheet[L12].value
    value.append(cell_value)
    
    print(cell)