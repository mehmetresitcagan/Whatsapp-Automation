import pandas as pd
import time
import pyautogui as auto
import webbrowser as web


def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    return data


def find_send_button():
    buttonLocation = None

    while buttonLocation is None:
        buttonLocation = auto.locateOnScreen("send_button.JPG", confidence=.8)

    return buttonLocation


def send_messages(data, message):
    for name, contact in zip(data["name"], data["contact"]):
        web.open('https://web.whatsapp.com/send?phone=+90' + str(contact) + '&text=' + message)
        time.sleep(10)

        button = find_send_button()

        auto.moveTo(button[0] + 5, button[1] + 5)
        time.sleep(1)
        auto.click()


if __name__ == '__main__':
    data = read_contact_file()
    send_messages(data, "selam")
