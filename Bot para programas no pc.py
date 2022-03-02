#Bot para programas no pc
import pyautogui
pyautogui.PAUSE(5) #tempo de execução entre cada comando
import time

# abrir a ferramenta/ o sistema / o programa
pyautogui.press('win') #colocar a tecla necessária para acessar o programa 
pyautogui.write('login.xlsx')
pyautogui.press('backspace')
pyautogui.press('enter')

time.sleep(5)
pyautogui.position()

#preencher o login
pyautogui.click(x=500, y=186) #verificar posição do icone a ser preenchido no seu computador 
pyautogui.write("Seu usuário") #adicionar seu nome de usuário antes de rodar o código

#preencher a senha
pyautogui.click(x=511, y=225) #verificar posição do icone a ser preenchido no seu computador
pyautogui.write("Sua senha") #adicionar sua senha antes de rodoar o código

#clicar em fazer login
pyautogui.click(x=491, y=347) #  aqui ele acessa o programa 