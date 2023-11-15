import os
from dotenv import load_dotenv
from send_mail import request
import json
import argparse


def main():
    load_dotenv()
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    send_name = os.getenv("send_name")

    parser = argparse.ArgumentParser(
        description='identify'
    )

    parser.add_argument('-m', help='Режим работы программы - введите 1 файл с почтами', default='')
    parser.add_argument('-t', help='Режим работы программы - введите файл с текстом', default='')
    parser.add_argument('-s', help='Режим работы программы - введите вашу тему', default='')
    emails_file_name = parser.parse_args().m
    text_file_name = parser.parse_args().t
    subject = parser.parse_args().s
    try:
        with open(emails_file_name, "r") as file:
            emails_contents = file.read()
        with open(text_file_name, "r") as my_file:
            text_contents = my_file.read()
        mails = json.loads(emails_contents)
    except FileNotFoundError:
        print("не корректный ввод местоположения файлов")
        exit()
    except json.decoder.JSONDecodeError:
        print("не корректно составлен файл с почтами")

    server_address = "smtp.yandex.ru:465"

    for mail in mails:
        request(text_contents, login, password, send_name, mail, subject, server_address)


if __name__ == "__main__":
    main()