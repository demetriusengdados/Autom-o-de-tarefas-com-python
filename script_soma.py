from openpyxl import load_workbook

wb = load_workbook(filename="nomes.xlsx")

planilha = wb['Planilha1']

for i in range(2,5):
    print("%s tem %s anos." % (planilha['A%s' % i].value, planilha['B%s' % i].value ) )

planilha['B5'] = "=SUM(B2:B4)"

wb.save(filename="nomes.xlsx")