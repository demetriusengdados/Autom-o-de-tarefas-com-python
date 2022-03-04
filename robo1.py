from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...\n")

driver = webdriver.Chrome('/home/gabriel/Desktop/Robos/chromedriver')
driver.get("https://registro.br/")

pesquisa = driver.find_element_by_id("is-avail-field")
pesquisa.clear() #Limpando a barra de pesquisa
dominio = "roboscompython.com.br"
pesquisa.send_keys(dominio)

pesquisa.send_keys(Keys.RETURN)
time.sleep(2)

resultados = driver.find_elements_by_tag_name("strong")
print("Domínio %s %s" % (dominio, resultados[4].text))


time.sleep(8) #Dormindo
driver.close()