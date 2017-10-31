import xlrd
import csv
from unidecode import unidecode

def csv_from_excel():
    wb = xlrd.open_workbook('FS_01_DOWN_COLORS.xlsx')
    sh = wb.sheet_by_name('Hoja1')
    your_csv_file = open('output_colors.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
    	text = unidecode(unicode(sh.row_values(rownum), encoding = "utf-8"))
    	print text
    	wr.writerow(text)

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()