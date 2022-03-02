import win32com.client as win32

#criando a integração com o outlook
outlook = win32.Dispatch('outlook application')

#criando o email
email = outlook.CreateItem(0)

faturamento = 1500 #variavel que será usada no texto do email
qtde_produtos = 10 #segunda variavel que será usada no texto do email
ticket_medio = faturamento / qtde_produtos

#configurar as informações do seu e-mail
email.To = "destion"; "destino2"  #email do destinatario
email.Subject = "Assunto do email"
email.HTMLBody = f"""
#Aqui será criada o texto do email
<p> O faturamento da loja foi de R${faturamento}</p>
<p>Vendemos {qtde_produtos} produtos</p>
<p>o Ticket médio de vendas foi de R${ticket_medio}</p>
<p>Abs,</p>
<p>Código Python</p>
"""

#anexo = "C://Users/seu usuario/Pasta do arquivo/arquivo.extensão(pdf, xlsx, doc, docx, csv)"
#email.Attachments.Add(anexo)

email.Send()
print("Email Enviado")

"""_summary_
    Feito isso nós vamos configurar as informações do e-mail:

Email.to – É o destino do e-mail, ou seja, quem vai receber o e-mail, podendo colocar mais de um destinatário conforme código;
Email.subjetct – Assunto do e-mail;
Email.HTMLbody – É o corpo do e-mail no formato HTML que vai ser um formato personalizado.

Agora vamos as explicações dos símbolos que temos dentro do nosso corpo de e-mail no formato HTML.

“”” e “”” ou ‘’’ e ‘’’ – É para indicar que o nosso texto será escrito em mais de uma linha dentro do HTML, então podemos utilizar 3 aspas duplas no início e no fim ou 3 aspas simples no início e no fim do código.
<p> e </p> – São as marcações de início e término de um parágrafo, ou seja, tudo que está dentro desses símbolos é referente a um parágrafo. Então caso queira outro parágrafo basta colocar o próximo texto com essa
mesma marcação.
f + {} – É o que chamamos de fstring que é uma forma de fazer referência a uma variável dentro do texto para que o Python utilize o valor da variável ao invés de colocar somente o nome dela

Na penúltima parte do código temos o anexo que é opcional, caso queira enviar. Essa variável vai ter o caminho do arquivo que será inserido no e-mail.
Logo em seguida temos o comando que anexa esse arquivo ao e-mail.
Por fim temos o emai.send que é o comando para enviar o e-mail da maneira que foi configurada.

Essa é a mensagem que recebemos no e-mail. Como informado anteriormente é possível adicionar anexos caso seja necessário, basta remover o # da linha e ajustar o caminho do arquivo, pois o # significa que é um 
comentário.
E linhas com comentários são ignoradas dentro do código, elas servem apenas para descrever melhor o código.
IMPORTANTE: É importante verificar se está logado no Outlook e se o arquivo que de fato está rodando é o arquivo de envio de e-mail. Verificado isso o código deve funcionar normalmente. Caso deseje enviar 
por outro servidor de emai mudar o parametro do email para o servidor escolhido. Exemplo: gmail = win32.Dispatch('gmail application'), email = gmail.CreateItem(0)
"""