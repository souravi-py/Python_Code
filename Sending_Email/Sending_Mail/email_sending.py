import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('mail.html').read_text())
email = EmailMessage()
email['from'] = 'Souravi Sinha'
email['to'] = 'souravi.sinha@hotmail.com'
email['subject'] = 'You are just awesome!!'

email.set_content(html.substitute({'name' : 'Souravi','company': 'Morgan Stanley'}),'html')

with smtplib.SMTP(host = 'smtp.live.com', port = 465) as smpt:
    smtp.elho()
    smtp.starttls()
    smpt.login('souravi.sinha@hotmail.com','Python@35')
    smtp.send_message(email)
