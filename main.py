import pandas as pd
from table import *
from shipper import *


def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    return data


if __name__ == '__main__':
    data = read_contact_file()
    print(make_table(data))
    option = input("Rehberinizdeki tüm kişilere mesaj göndermek için '1', belirli kişilere göndermek için '2', "
                   "çıkış yapmak için herhangi bir tuşa basın:")

    if str(option) == "1":
        send_messages(data, "123")

