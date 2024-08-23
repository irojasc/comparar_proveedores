import xlrd

def  read_excel_file(file_path, sheet_name):
    myList = []
    # Open Excel file
    workbook = xlrd.open_workbook(file_path)
    # Access sheet by index or name
    sheet = workbook.sheet_by_name(sheet_name)  
    # Read cell value
    for row in range(sheet.nrows):
        myList.append({"index": row, "content": sheet.cell_value(row, 0)})
    return myList

