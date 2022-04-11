from selenium import webdriver
import time
from selenium.webdriver.commom.keys import keys

#abrindo o google chrome

driver = webdriver.Chrome()

#maximizando a janela
driver.maximize_window()

#deletando os cookies
driver.delete_all_cookies()

#navegando ate a url
driver.get("https://www.gmail.com")

#identificando o nome de usuario na caixa de texto e dando ENTER

driver.find_element_by_id("identifierId").send_keys("youremailhere")

time.sleep(2)

#clicando no proximo botão

driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

time.sleep(3)

#identificando a senha na caixa de testo e dando ENTER
driver.find_element_by_name("password").send_keys("########")
time.sleep(3)

#clicando no botão próximo
driver.find_elements_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

time.sleep(3)

#Fechando o browser
driver.close()
print('Login no Gmail efetuado com sucesso')
