import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = ""
password = ""

def send_email(to,msg):
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email,to, msg)

message = """\
Subject: Hi there

This message is sent from Python."""

send_email("", message)
    