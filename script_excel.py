from openpyxl import Workbook

wb = Workbook()

nome_arquivo = "meu_primeiro_arquivo.xlsx"

ws1 = wb.active
ws1.title = "Planilha 1"

dados = [
    ['Ano','Lucro','Custos'],
    [2015, '30%', '40%'],
    [2016, '50%', '40%'],
    [2017, '70%', '40%']
]

for linha in dados:
    ws1.append(linha)

ws2 = wb.create_sheet(title="Pi")
ws2['F5'] = 3.14

wb.save(filename=nome_arquivo)

