import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "criandorobosempython@gmail.com"
toaddr = "criandorobosempython@gmail.com, gabrielcasemiro68@gmail.com"

# Instância do MIMEMultipart
msg = MIMEMultipart()


msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "Venha conhecer nosso restaurante!!!"

body = """Inauguração do nosso restaurante essa noite, venha conhecer."""

msg.attach(MIMEText(body, 'plain'))

#Anexo
filename="panfleto.pdf"
anexo = open("panfleto.pdf","rb")

p = MIMEBase('application', 'octet-stream')

p.set_payload((anexo).read())

# encode em base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)

#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

# Segurança
s.starttls()

s.login(fromaddr, 'robos123')

# Converte para String
text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()