import time
import pyautogui as auto
import webbrowser as web

"""

Delivers given messages to receivers in the given time.

"""


def find_new_chat_button():
    buttonLocation = None

    while buttonLocation is None:
        buttonLocation = auto.locateOnScreen("new_chat_button.JPG", confidence=.8)

    auto.moveTo(buttonLocation[0] + 10, buttonLocation[1] + 10)
    time.sleep(1)
    auto.click()


def send_messages(df, message):
    web.open("https://web.whatsapp.com/")
    for contact in df["contact"]:
        find_new_chat_button()
        auto.typewrite(str(contact), interval=.02)
        time.sleep(0.5)
        auto.hotkey("enter")
        time.sleep(0.5)
        auto.typewrite(message, interval=.02)
        time.sleep(0.5)
        auto.hotkey("enter")
        time.sleep(0.5)
