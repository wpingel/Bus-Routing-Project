import xlsxwriter

workbook = xlsxwriter.Workbook('new.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Yes, really. You just made this workbook, worksheet, and cell data with a Python script.')

workbook.close()