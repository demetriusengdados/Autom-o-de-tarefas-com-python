from TelegramBot import TelegramBot

obj_telegram = TelegramBot()

print("Iniciando nosso robô...")
print("Escolha o grupo alvo")
grupo_alvo = obj_telegram.get_groups()
membros = obj_telegram.get_members_of_group(grupo_alvo)