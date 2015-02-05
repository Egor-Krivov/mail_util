import json
import smtplib
from email.mime.text import MIMEText

def send_data(message):
    """Send message to some e-mail.
    Settings should be located in current folder in file settings.json.
    See settings.json.template for example."""
    smtp_server = data['smtp_server']
    smtp_port = data['smtp_port']
    
    sender = data['sender']
    smtp_password = data['smtp_password']
    
    to = data['to']
    subject = data['subject']
    
    mail_lib = smtplib.SMTP_SSL(smtp_server, smtp_port)
    mail_lib.login(sender, smtp_password)
    
    msg = MIMEText(message.encode('utf-8'), _charset="UTF-8")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    
    mail_lib.sendmail(sender, to, msg.as_string())
    mail_lib.quit
    
