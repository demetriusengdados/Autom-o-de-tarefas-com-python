#Bot para internet usando o selenium
#Os drivers que são necessários para rodar o selenium são chromedriver para google chrome e geckodriver para mozzila, após fazer o download do arquivo move-lo para a pasta raiz onde o python.exe está instalado.
#Segue em aenxo no diretorio foto com caminho padrão do python, eu usei o firefox

from selenium import webdriver
import time

navegador = webdriver.Firefox()
#navegador = webdriver.Chrome()
navegador.get("https://login.live.com")
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys('seuemail@seuemail.com.br')
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys('suasenha')
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()