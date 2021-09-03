import pandas as pd
from table import *
from delivery import *


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
    try:
        if str(option) == "1":
            message = input("Göndermek istediğiniz mesajı yazın:")
            timeHour = int(input("Mesajı göndermek istediğiniz saat:"))
            timeMin = int(input("Mesajı göndermek istediğiniz dakika:"))
            send_messages(df=df, message=message, time_hour=timeHour, time_min=timeMin)
        elif option == "2":
            print(make_table(df))
            print(
                "Rehberinizdeki tüm kişiler gösterilmiştir. Sadece adını doğru yazdığınız kişilere mesaj gönderilecektir.")
            nameInputs = input("Mesaj göndermek istediğiniz kişilerin isimlerini boşluk bırakarak yazın:").split()
            messageReceiversList = [[name, contactNo] for name, contactNo in zip(df["name"], df["contact"]) if
                                    name_is_in_the_list(nameInputs, name)]
            messageReceiversDf = pd.DataFrame(data=messageReceiversList, columns=["name", "contact"])

            message = input("Göndermek istediğiniz mesajı yazın:")
            timeHour = int(input("Mesajı göndermek istediğiniz saat:"))
            timeMin = int(input("Mesajı göndermek istediğiniz dakika:"))
            send_messages(df=messageReceiversDf, message=message, time_hour=timeHour, time_min=timeMin)
        else:
            return 0
    except InvalidTimeException:
        print("Zamanı yanlış girdiniz. Tek haneli sayıları başına sıfır koymadan yazın.")


if __name__ == '__main__':
    main()
