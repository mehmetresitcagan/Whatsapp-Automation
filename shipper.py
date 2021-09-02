import time
import pyautogui as auto
import webbrowser as web


def find_new_chat_button():
    buttonLocation = None

    while buttonLocation is None:
        buttonLocation = auto.locateOnScreen("new_chat_button.JPG", confidence=.8)

    auto.moveTo(buttonLocation[0] + 10, buttonLocation[1] + 10)
    time.sleep(1)
    auto.click()


def send_messages(data, message):
    web.open("https://web.whatsapp.com/")
    for contact in data["contact"]:
        find_new_chat_button()
        auto.typewrite(str(contact), interval=.02)
        time.sleep(0.5)
        auto.hotkey("enter")
        time.sleep(0.5)
        auto.typewrite(message, interval=.02)
        time.sleep(0.5)
        auto.hotkey("enter")
        time.sleep(0.5)
