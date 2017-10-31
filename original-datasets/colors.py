import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('FS_01_DOWN_ANNOT.xlsx')
    sh = wb.sheet_by_name('Hoja1')
    your_csv_file = open('FS_01_DOWN_ANNOT.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
    	wr.writerow([unicode(c).encode('utf8') for c in sh.row_values(rownum)])
    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()