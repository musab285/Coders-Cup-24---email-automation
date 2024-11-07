import datetime
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage

# TODO Implement correct way of fetching the sender's password
# Temporary method of getting the sender's password
# passFile = open("pass.txt", "r")
# password = passFile.readlines(  )[0].lstrip().rstrip()

password=""

def sendAttachmentMail(emailAddress, htmlContent):
    sender = "acm.khi@nu.edu.pk"  # Your sender email
    senderPassword = password
    recieverMail = emailAddress
    msg = EmailMessage()
    msg["Subject"] = "Important Coder's Cup Details & Vjudge Username Update"
    msg["From"] = sender
    msg["To"] = recieverMail

    

    # Attach the email design
    if isinstance(htmlContent, str):  # Ensure it's a string
        msg.set_content(htmlContent, subtype='html')
    else:
        print("HTML content is not a string.")

    # Sending Messages...
    print(f"[+] Sending attachment mail to {recieverMail}")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        try:
            smtp.starttls()
            smtp.login(sender, senderPassword)
            smtp.send_message(msg)
            print(f"[+] Successfully sent mail to {recieverMail}")
            return True                
        except smtplib.SMTPRecipientsRefused as e:
            print(f"\n[-] Failed to send mail to {recieverMail}: Refused email.")
            # Log refused emails
            unsuccessfulMailLog = open("notSentToEmails.log", "a")
            unsuccessfulMailLog.write(
                f"{recieverMail} | Error: {e} | {datetime.datetime.now()}\n"
            )
            unsuccessfulMailLog.close()
        except smtplib.SMTPAuthenticationError:
            print("\n[-] Authentication error: Failed to authenticate with the SMTP server. Please check your email and password.")
        except smtplib.SMTPResponseException as e:
            print(f"\n[-] Could not send mail to {recieverMail}: Error: {e.smtp_error}")
            unsuccessfulMailLog = open("notSentToEmails.log", "a")
            unsuccessfulMailLog.write(
                f"{recieverMail} | Error: {e.smtp_error} | {datetime.datetime.now()}\n"
            )
            unsuccessfulMailLog.close()
        return False
