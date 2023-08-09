# https://docs.python.org/3.9/library/email.examples.html#email-examples
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
textfile = "textfile.txt"
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())


receivers = ['xxxx@gmail.com,aaaa@qq.com']
cc = ['xxxx.liu@xxxx.com,aass.jiao@xxx.com']
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = 'landy.liu@xxxa.com'
msg['To'] = ','.join(receivers)
msg['Cc'] = ','.join(cc)

# Send the message via our own SMTP server.
s = smtplib.SMTP('xxx.ssss.com')

s.send_message(msg)
s.quit()
