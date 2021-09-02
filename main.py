import pandas as pd
import pywhatkit as kit
import time
import pyautogui as auto
import webbrowser as web
from urllib.parse import quote

"""

    I chose pywhatkit as framework used because of it's ease of usage. But I had a problem on sending messages.
    So I used pyautogui to just press 'send' button.
    
"""

"""
def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    return data


def send_message(data):
    for name, contact in zip(data["name"], data["contact"]):
        kit.sendwhatmsg_instantly(phone_no="+90" + str(contact), message="selam " + name, wait_time=10)
        # auto.hotkey('enter')
        time.sleep(1)


if __name__ == '__main__':
    data = read_contact_file()
    send_message(data)
"""


def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    return data


def send_message(data):
    message = "selam"
    parsed_message = quote(message)
    for name, contact in zip(data["name"], data["contact"]):
        web.open('https://web.whatsapp.com/send?phone=+90' + str(contact) + '&text=' + parsed_message)
        time.sleep(10)

        find_send_button = None

        while find_send_button is None:
            find_send_button = auto.locateOnScreen("send_button.JPG", confidence=.8)

        auto.moveTo(find_send_button[0] + 5, find_send_button[1] + 5)
        time.sleep(1)
        auto.click()


if __name__ == '__main__':
    data = read_contact_file()
    send_message(data)
