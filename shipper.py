import time
import pyautogui as auto
import pywhatkit as kit
import webbrowser as web


def find_send_button_andClick():
    buttonLocation = None

    while buttonLocation is None:
        buttonLocation = auto.locateOnScreen("send_button.JPG", confidence=.8)

    auto.moveTo(buttonLocation[0] + 5, buttonLocation[1] + 5)
    time.sleep(1)
    auto.click()


def find_new_chat_button_andClick():
    buttonLocation = None

    while buttonLocation is None:
        buttonLocation = auto.locateOnScreen("new_chat_button.JPG", confidence=.8)

    auto.moveTo(buttonLocation[0] + 5, buttonLocation[1] + 5)
    time.sleep(1)
    auto.click()


def send_messages(contactList, message):
    # web.open("https://web.whatsapp.com/")
    for contact in contactList:
        """find_new_chat_button_andClick()
        auto.typewrite("+90" + str(contact["contact"]), interval=.02)
        time.sleep(0.5)
        auto.hotkey("enter")"""
