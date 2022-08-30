from openpyxl import Workbook

print("Iniciando nosso robô...")

print("Lendo dados do arquivo de texto...")

f = open("gastos.txt", "r", encoding="utf-8")
arquivo = f.read()

lista_dados = arquivo.splitlines()

for i in range(0, len(lista_dados)):
    lista_dados[i] = lista_dados[i].split(',')

#Criando nosso arquivo
wb = Workbook()
ws = wb.active

print("Escrevendo no nosso arquivo excel gastos.xlsx")
for linha in lista_dados:
    ws.append(linha)

wb.save(filename="gastos.xlsx")