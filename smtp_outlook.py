import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Hello, PFA file'''

#The mail addresses and password
sender_address = ''
sender_pass = ''
receiver_address = ''

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Mithra system Generated Mail'

attach_file_name = []
print(len(attach_file_name))
print(attach_file_name[0])

for i in attach_file_name:
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file = open(i, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment

    #add payload header with filename
    payload.add_header('Content-Disposition', 'attachment', filename=i)
    message.attach(payload)


#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.office365.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
print(text)
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')