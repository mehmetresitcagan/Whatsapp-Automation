import time
import pyautogui as auto
import webbrowser as web
from exceptions import InvalidTimeException

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


def send_messages(df, message, time_hour, time_min):
    left_time = set_time(time_hour, time_min)
    print(left_time)
    time.sleep(left_time)
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


def set_time(time_hour, time_min):
    if time_hour not in range(25) or time_min not in range(60):
        raise InvalidTimeException

    if time_hour == 0:
        time_hour = 24

    call_sec = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_sec - current_to_second

    if left_time < 0:
        left_time += 86400

    return left_time
