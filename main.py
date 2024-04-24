import smtplib as smtp
from create_account import CreateAccount
import json
from datetime import datetime
import pandas
from random import choice
from tkinter import messagebox

ACCOUNT_PATH = "data/user_account.json"
BIRTHDAYS_PATH = "data/birthdays.csv"
TEMPLATES_PATH = "data/letter_templates/letter_#.txt"
NUMBER_OF_TEMPLATES = 3


def get_email_and_password() -> (str, str, str):
    """
    retrieves data from ACCOUNT_PATH and returns it
    :return: name, email and password stored in ACCOUNT_PATH
    """

    with open(ACCOUNT_PATH, "r") as file:
        data = json.load(file)
        name = data["name"]
        email = data["email"]
        password = data["password"]
    return name, email, password


def get_random_letter() -> str:
    """
    gets a random letter template from TEMPLATES_PATH, replaces the required data and returns it
    :return: updated letter
    """

    letter_number = choice(range(1, NUMBER_OF_TEMPLATES + 1))
    letter_path = TEMPLATES_PATH.replace("#", str(letter_number))
    with open(letter_path, 'r') as file:
        letter = file.read()

    letter = letter.replace("[NAME]", to_name).replace("[MY_NAME]", from_name)
    return letter


def send_email() -> None:
    """
    sends birthday email from one account to another, then informs user
    :return: None
    """
    with smtp.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_pass)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"subject:Happy Birthday!\n\n{email_body}")

    messagebox.showinfo(title="Confirmation", message="Email(s) Sent!")


if __name__ == "__main__":
    try:
        from_name, from_email, from_pass = get_email_and_password()
    except FileNotFoundError:
        CreateAccount()
        from_name, from_email, from_pass = get_email_and_password()

    now = datetime.now()
    birthdays = pandas.read_csv(BIRTHDAYS_PATH).to_dict(orient="records")

    for birthday in birthdays:
        if now.year == birthday['year'] and now.month == birthday['month'] and now.day == birthday['day']:
            to_email = birthday["email"]
            to_name = birthday['name']

            email_body = get_random_letter()
            send_email()
