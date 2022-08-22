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

msg['Subject'] = "Video Aulas Grátis!!"


html = """
<html>
	<body>
		<p>Oi,<br>
		Como vai você?<br>
		<a href="https://www.udemy.com">Video Aulas Gratuitas</a>
		Muitas aulas para assistir.


		</p>
	</body>
<html>
"""

part1 = MIMEText(html, "html")

msg.attach(part1)

#Servidor SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)

# Segurança
s.starttls()

s.login(fromaddr, 'robos123')

# Converte para String
text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()