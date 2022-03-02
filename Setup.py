from cx_Freeze import setup, Executable

setup(
    name = "Enviando Email",
    version = "1.0",
    description = "Script para enviar email automatico",
    executables = [Executable("enviando_email.py")],
)

#segundo passo 
#Após salvar o setup.py,copie o setup.py e seuprograma.py para a pasta do Python no disco ‘C:’
#Após copiar os arquivos para a pasta do Python no disco ‘C:’,abra o propomt de comando ou powershell e digite as seguintes linhas :
#>>> C:\users\user>cd\
#>>> C:\> cd python(a versão do seu python,sem pontuação. EX: python34)
#>>> C:Python34> c:\python34\python.exe setup.py build