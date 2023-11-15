import smtplib


def request(text, login, password, send_name, to_name, subject, server_address):
    letter = f"""\
From: {send_name}
To: {to_name}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

{text}"""

    letter = letter.encode("UTF-8")

    server = smtplib.SMTP_SSL(server_address)
    server.login(login, password)
    server.sendmail(send_name, to_name, letter)
    server.quit()