import pandas as pd
import time
import urllib3

contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)

from selenium import webdriver
from selenium.webdriver.common.keys import keys

navegador = webdriver.chrome()
navegador.get("https://web.whatsapp.com/")

#espera aparecer o elemento que tem id de "side"
while len (navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

#Já estamos com o login feito no whatsapp web

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoas = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib3.parse.quote(f"Oi {Pessoa}! {Mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&{text}={texto}"
    navegador.get(link)
    while len (navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(keys.ENTER)
    time.sleep(10)
    
    