from email import message
import imaplib
import email

def get_mail():
        
    user_name = ""
    password =""

    gmail_host = "imap.gmail.com"

    mail = imaplib.IMAP4_SSL(gmail_host)

    mail.login(user_name,password)

    mail.select('inbox')

    #_,selected_mail = mail.search(None,'(FROM "xxx@gmail.com")') # get from same id
    _,selected_mail = mail.search(None,'ALL')

    print(selected_mail)

    print(f"Total Message : {len(selected_mail[0].split())}")

    for num in selected_mail[0].split():
        _,data = mail.fetch(num, '(RFC822)')
        _,bytes_data = data[0]
        
        email_message = email.message_from_bytes(bytes_data)
        
        print("*"*50)
        
        print("Subject: ", email_message["subject"])
        print("To: ", email_message["to"])
        print("From: ", email_message["from"])
        print("Date: ", email_message["date"])
        
        for part in email_message.walk():
            if part.get_content_type()=="text/plain" or part.get_content_type() == "text/html":
                msg = part.get_payload(decode=True)
                print("Message: \n", msg.decode())
                print("*"*50)
                break
            

get_mail()