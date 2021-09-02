import pandas as pd
from table import *
from shipper import *


def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    return data


if __name__ == '__main__':
    data = read_contact_file()
    print("Rehberinizde bulunan tüm kişiler:")
    print(make_table(data))
    send_messages(data, "selam")
