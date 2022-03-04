from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd
print("Iniciando nosso robo\n")
arq = open("resultado.txt", "w")

dominios = []
#lendo do excel
workbook = xlrd.open_workbook('Dominios.xlsx')
sheet = workbook.sheet_by_index(0)
for linha in range(0,10):
    dominios.append(sheet.cell_value(linha,0))


drive = webdriver.Chrome('c:usuarios/meuusuario/documentos/Automação Python/Udemy/chromedriver_win64') #colocar o caminho da pasta onde esta localizado o executavel que fez o download
driver.get("https://registro.br") #usei o site como exemplo, quando quiser fazer em outro site so copiar a url dele e colar 


for dominio in dominios: 
    pesquisa = driver.find_element_by_id("is-avail-field") #entar no site com botão esquerdo mouse clicar em inspecionar e procurar o ponto que voce quer, nesse caso peguei a barra de pesquisa 
    #e copiei o xpath do site e colei
    pesquisa.clear() #limpando a barra de pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_Keys(Keys.RETURN)
    time.sleep(5)

    resultados = driver.find_elements_by_tag_name("strong")
    texto = "Dominio %s %s\n" % (dominios, resultados[4].text)
    arq.write(texto)

arq.close()
driver.close()

