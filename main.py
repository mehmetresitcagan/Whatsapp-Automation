import pandas as pd


def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")
    for i in data["contact"]:
        print(i)


if __name__ == '__main__':
    read_contact_file()
