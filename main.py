import pandas as pd
import pywhatkit as kit


def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    return data


def send_message(data):
    for name, contact in zip(data["name"], data["contact"]):
        kit.sendwhatmsg_instantly(phone_no="+90" + str(contact), message="selam " + name, wait_time=20)


if __name__ == '__main__':
    data = read_contact_file()
    send_message(data)
