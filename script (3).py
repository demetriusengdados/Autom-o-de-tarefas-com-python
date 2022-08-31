from openpyxl import load_workbook

#Escolhe o arquivo
dest_filename = 'book.xlsx'
wb = load_workbook(filename = dest_filename)
sheet = wb['Data']

#Move a linha 2 (DE A ATÉ Z) uma para cima
sheet.move_range("A2:Z2", rows=-1)

#Move a celula F8:F8 para duas para a direita 
sheet.move_range("F8:F8", cols=2)

#Move a celula F10:F10 para duas para a esquerda 
sheet.move_range("F10:F10", cols=-2)

#Move a celula C14:E16 duas para a esquerda e 1 para cima
sheet.move_range("C14:E16", cols=-2, rows=-1)

wb.save(filename = dest_filename)
