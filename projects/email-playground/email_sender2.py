import smtplib
import os
from string import Template
from pathlib import Path
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'mjsdmj@hotmail.com'
email['to'] = 'mauricio.sdjr@gmail.com'
email['subject'] = 'Deu certo!!! Uhuuul'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

with smtplib.SMTP(host='smtp.outlook.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('mjsdmj@hotmail.com', EMAIL_PASSWORD)
  smtp.send_message(email)
  print('All good boss!')