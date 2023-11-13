import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

send_name = "bezdqrtest@yandex.ru"
to_name = "test13221412@gmail.com"

letter = """\
From: bezdqrtest@yandex.ru
To: test13221412@gmail.com
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";

Привет!"""

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(send_name, to_name, letter)
server.quit()

#bezdqrtest
#BezdqrTest123
#xgmvmkgiohmveryd