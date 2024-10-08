import xlrd

def  read_excel_file(file_path, sheet_name, column: int = 0):
    myList = []
    # Open Excel file
    workbook = xlrd.open_workbook(file_path)
    # Access sheet by index or name
    sheet = workbook.sheet_by_name(sheet_name)  
    # Read cell value
    for row in range(sheet.nrows):
        myList.append({"index": row, "content": f'{row}-{sheet.cell_value(row, column)}', "isSelected": False, 'content_root': 'xxxxx'})
    return myList

def read_excel_ubigeo(file_path, sheet_name):
    myList = []
    departamentoList = []
    # Open Excel file
    workbook = xlrd.open_workbook(file_path)
    # Access sheet by index or name
    sheet = workbook.sheet_by_name(sheet_name)  
    # Read cell value
    for row in range(sheet.nrows):
        tmp = {}
        departamento = sheet.cell_value(row, 0)
        departamentoList.append(departamento)
        departamento = departamento + '_dp'
        provincia = sheet.cell_value(row, 1)
        provincia = provincia + '_pr'
        distrito = sheet.cell_value(row, 2)
        distrito = distrito + '_dt'
        tmp.update({departamento: sheet.cell_value(row, 3)})
        tmp.update({provincia: sheet.cell_value(row, 4)})
        tmp.update({distrito: sheet.cell_value(row, 5)})
        myList.append(tmp)
    
    return  myList, list(dict.fromkeys(departamentoList))