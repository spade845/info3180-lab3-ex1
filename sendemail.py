import smtplib 
from_addr = 'spadeandroid@gmail.com' 
to_addr  = 'anybody@gmail.com' 
message = """From: {} <{}> 
To: {} <{}> 
Subject: {} 
{} 
""" 
from_name='SPADE'
to_name='ANYBODY'
subject='HEY'
msg='WOW THIS WORKS'
message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject,msg) 
# Credentials (if needed) 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, 
password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit() 