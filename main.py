import pandas as pd
from table import *
from shipper import *


def read_contact_file():
    data = pd.read_excel(io="contact.xlsx")

    return data


def name_is_in_the_list(name_inputs, name):
    if name in name_inputs:
        return True

    return False


def main():
    df = read_contact_file()
    option = input("Rehberinizdeki tüm kişilere mesaj göndermek için '1', belirli kişilere göndermek için '2', "
                   "çıkış yapmak için herhangi bir tuşa basın:")

    if str(option) == "1":
        send_messages(df, "123")

    elif option == "2":
        print(make_table(df))
        print(
            "Rehberinizdeki tüm kişiler gösterilmiştir. Sadece adını doğru yazdığınız kişilerer mesaj gönderilecektir.")
        nameInputs = input("Mesaj göndermek istediğiniz kişilerin isimlerini bosluk bırakarak yazın:").split()
        messageReceiversList = [[name, contactNo] for name, contactNo in zip(df["name"], df["contact"]) if
                                name_is_in_the_list(nameInputs, name)]
        messageReceiversDf = pd.DataFrame(data=messageReceiversList, columns=["name", "contact"])

        send_messages(messageReceiversDf, "abc")

    else:
        return 0


if __name__ == '__main__':
    main()
