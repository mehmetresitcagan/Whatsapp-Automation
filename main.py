import pandas as pd
import pywhatkit as kit
import time

def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    dataDict = {}

    for name, contact in zip(data["name"], data["contact"]):
        dataDict[name] = contact
        kit.sendwhatmsg_instantly(phone_no="+90"+str(contact),message="selam "+name,wait_time=20)




if __name__ == '__main__':
    read_contact_file()
