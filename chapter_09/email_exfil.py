import smtplib
import time

import win32com.client

smtp_server = "smtp.example.com"
smtp_port = 587
smtp_account = "tim@example.com"
smtp_password = "seKret"
target_accounts = ["tim@elsewhere.com"]


def plain_email(subject, contents):
    message = f"Subject: {subject}\nFrom {smtp_account}\n"
    message += f"To: {target_accounts}\n\n{contents.decode()}"

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_account, smtp_password)

    # server.set_debuglevel(1)
    server.sendmail(smtp_account, target_accounts, message)
    time.sleep(1)
    server.quit()


def outlook(subject, contents):
    outlook = win32com.client.Dispatch("Outlook.Application")

    message = outlook.CreateItem(0)
    message.DeleteAfterSubmit = True
    message.Subject = subject
    message.Body = contents.decode()
    message.To = target_accounts[0]

    message.Send()


if __name__ == "__main__":
    plain_email("test2 message", "attack at dawn")
