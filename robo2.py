from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

response = requests.get("https://api.github.com/users/gabriel")
data = response.json()


# Atribuição de Variaveis
email = "roboparapython@gmail.com"
senha = "cursopython123"

destinatario = "roboparapython@gmail.com"
assunto = "E-mail enviado pelo robo"
mensagem = "API GitHub\n Seguidores: %s\n Seguindo: %s\n" % (data["followers"],data["following"])

driver = webdriver.Chrome("/home/gabriel/Desktop/Robos/chromedriver")

print("Iniciando nosso robô...\n")
print("Acessando o Gmail...")
driver.get("https://gmail.com.br/")

#LOGIN
print("Realizando login...")
login = driver.find_element_by_id("identifierId")
login.clear()
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(2)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(6)
print("Login realizado...")

print("Abrindo caixa de e-mail")
driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
time.sleep(10)

print("Escrevendo o e-mail...")
para = driver.find_element_by_name("to")
para.send_keys(destinatario)
para.send_keys(Keys.RETURN)

titulo = driver.find_element_by_name("subjectbox")
titulo.send_keys(assunto)
titulo.send_keys(Keys.RETURN)

corpo_de_texto = driver.find_element_by_xpath("//div[@role='textbox']")
corpo_de_texto.send_keys(mensagem)

enviar = driver.find_element_by_xpath("//div[@aria-label='Enviar ‪(Ctrl-Enter)‬']")
enviar.click()
print("Enviado e-mail...")
time.sleep(5)
print("E-mail enviado com sucesso!")

driver.close()

