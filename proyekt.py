data = {"card_pin": 7410, "card_number": 8600476523478901, "card_balance": 3000000, "card_tel_number": None, "status": False}
data_money = {"money_1000": 1000, "money_2000": 2000, "money_5000": 5000, "money_10000": 10000, "money_20000": 20000, "money_50000": 50000, "money_100000": 100000, "money_200000": 200000}
data_money_count = {"money_1000": 100, "money_2000": 150, "money_5000": 220, "money_10000": 300, "money_20000": 100 , "money_50000": 100 , "money_10000": 300 , "money_20000": 300000000}

global total_money

total_money = 0

keys = data_money_count.keys()

for i in keys:
    total_money += data_money_count[i] * data_money[i]
    print(total_money)
"""Uzbek meniyu uchun"""
soqqa = 0

dos = 0

def malumot():
    print(f"""
    1. Kartangizni raqami - {data["card_number"]}
    2. Kartangizni paroli - {data["card_pin"]}
    3. Kartangizni hisobi - {data["card_balance"]}
    4. Kartangizga ulangan telefon raqam - {data["card_tel_number"]}
    5. Kartangizni SMS xabarini tekshirish - {data["status"]}
""")

    return service_uz()


def get_money():
    global total_money
    money = input("Summani kiriting - ")
    fd = money * 1.01
    if data ["card_balance"] >= fd and total_money >= money:
        tad = input(f"""
         Summa : {money}
         Kartadan yechiladi : {fd}
         
         1. Davom ettirish
         2. Orqaga qaytish
              >>>""")

        if tad == '1':
            data["card_balance"] -= fd
            total_money -= money
            print(f"""Pul yechildi 
Xizmat yakunlandi""")
            return service_uz()
        else:
            print("Xizmat yakunlandi")
            return service_uz()

    else:
        if total_money < money:
            print("Bankomatda yetarlicha so'mma mavjud emas")
        elif data["card_balance"] < fd:
            print("Kartada mablag' yetarli emas")
        else:
            print("XATO")
            return service_uz()


def sms_uz_on():
    if data["status"] == True:
        print("Bu kartaga allaqachon telefon raqam ulangan")
        return sms_uz()
    else:
        tel_number = input("""
            Telefon raqam kiriting:
                >>> +998 """)

        if len(tel_number) == 9:
            data["status"] = (True)
            data["card_tel_number"] = tel_number
            return service_uz()
        else:
            print("""
            Error!
            Telefon raqam kiritishda xatolik bo'ldi!
                """)
            return sms_uz()


def sms_uz():
    print("SMS Service")
    tok = input("""
        Xizmatni tanglang:
            1. SMS xabarni yoqish
            2. SMS xabarni o'chirish
            0. Orqaga qaytish
                >>> """)

    if tok == "1":
        return sms_uz_on()

    elif tok == "2":
        if data["status"] == True:
            data["status"] = False
            data["card_tel_number"] = None
            print("SMS xabarnoma xizmati o'chirildi")
            return sms_uz()
        else:
            sms_info = input("""
            SMS xabarnoma xizmati mavjud emas!

            1. Yoqish
            0. Orqaga
                >>> """)
            if sms_info == "1":
                return sms_uz_on()
            elif sms_info == "0":
                return service_uz()
            else:
                print("Error!")
                return sms_uz()

    elif tok == "0":
        return service_uz()

    else:
        print("Error!")
        return sms_uz()


def password():
    n = 2
    pin_1 = input("Yangi parol kiriting")
    pin_2 = input("Yangi parolni tasdiqlang")
    if password == pin_2:
        print("Parolingiz o'zgartirildi")
        return service_uz()

def add_money():
    money =  int(input("Summani kiriting:"))
    money_1 = money * 0.99
    dos = input(f"""
        Kiritilgan summa - {money}
        Kartaga tushadigan summa - {money_1}
        
        1. Ha 
        2. Yo'q
        >>> """)

    if dos == '1':
        data ["card_balance"] += money_1
        print("Xizmat muvaffaqiyatli yakunlandi")
        return service_uz()
    else:
        print("Xizmat tugatildi")
        return service_uz()



def rep():
    reply = input("""
            1.Orqaga qaytish
            0. Xizmatni tugatish
                 >>> """)
    if reply == "1":
        return service_uz()
    elif reply == "0":
        return main ()

    else :
        print("Xato!")
        return rep()


def card_balance_uz():
    print(f"Kartada {data['card_balance']}")
    return rep()


def pin_code():
    print("kartani kodini o'zgartirish")
    pin_1 = int(input("Yangi kod kiriting: "))
    pin_2 = int(input("Yangi kodni qayta kiriting: "))
    if pin_1 == pin_2 and 999 < pin_1 < 10000:
        print("Tabriklaymiz parolingiz muvaffaqiyatli o'zgartirildi")
        data["card_pin"] = pin_1
        return service_uz()


def service_uz():
    print("Services")
    services = input("""
        Xizmat turini tanlang :
            1. Karta balansi
            2. Kartani to'ldirish
            3. Naxt pul yechish
            4. SMS
            5. Parolni o'zgartirish
            6. Xizmatni tugatish
            7. Kartani malumotlari 
                >>>>""")

    if services == "1":
        return card_balance_uz()

    elif services == "2":
     return add_money()

    elif services == "3":
        return get_money()

    elif services == "4":
        return sms_uz()

    elif services == "5":
        return pin_code()

    elif services == "6":
        return main()

    elif services == "7":
        return malumot()

    else:
        return service_uz()




def parol_uz():
    n = 2
    password = int(input("KARTANI PAROLINI KIRITING:"))
    while n >= 1 and data["card_pin"] != password:
        print("Siz notogri parol kiritdingiz")
        password = input("KARTANI PAROLINI KIRITING:")
        if data["card_pin"] == password:
            return service_uz()

        n -= 1

    if data["card_pin"] == password:
        return service_uz()
    else:
        print("KARTANGIZ BLOKLANDI")
        return main()


def malumot_eng():
    print(f"""
    1. Card number - {data["card_number"]}
    2. Card pin code - {data["card_pin"]}
    3. Card balance - {data["card_balance"]}
    4. Card phone number - {data["card_tel_number"]}
    5. Chek your card SMS message - {data["status"]}
""")

    return service_eng()


def get_money_eng():
    global total_money
    money = int(input("Enter the amount - "))
    fd = money * 1.01
    if data["card_balance"] >= fd and total_money >= money:
        tad = input(f"""
         Amount : {money}
         is deducted from the card : {fd}

         1. we will continue
         2. ga back
              >>>""")
        if tad == '1':
            data["card_balance"] -= fd
            total_money -= money
            print(f""" The money was withdrawn 
service completed""")
            return service_eng()
        else:
            print("service completed")
            return service_eng()

    else:
        if total_money < money:
            print("There is not enough money in the ATM")
            return service_eng()
        elif data["card_balance"] < fd:
            print("There is not enough money on the card")
            return service_eng()
        else:
            print("Error")
            return service_eng()


def sms_eng_on():
    if data["status"] == True:
        print("A phone number is already connected to this card")
        return sms_eng()
    else:
        tel_number = input("""
            Enter the phone number:
                >>> +998 """)

        if len(tel_number) == 9:
            data["status"] = True
            data["card_tel_number"] = tel_number
            return service_eng()
        else:
            print("""
            Error!
            There was an error entering the phone number
                """)
            return sms_eng()


def sms_eng():
    print("SMS Service")
    tok = input("""
        Select a service:
            1. Enable SMS message
            2. Delete SMS message
            0. go back
                >>> """)

    if tok == "1":
        return sms_eng_on()

    elif tok == "2":
        if data["status"] == True:
            data["status"] = False
            data["card_tel_number"] = None
            print("SMS notification service has been disabled")
            return sms_eng()
        else:
            sms_info = input("""
            SMS notification service is not availabe

            1. On
            0. Go back
                >>> """)
            if sms_info == "1":
                return sms_eng_on()
            elif sms_info == "0":
                return service_eng()
            else:
                print("Error!")
                return sms_eng()

    elif tok == "0":
        return service_eng()

    else:
        print("Error!")
        return sms_eng()


def password_eng():
    n = 2
    pin_1 = input("Enter a new password")
    pin_2 = input("Conifirm the new password ")
    if password == pin_2:
        print("Your password has been changed")
        return service_eng()


def add_money_eng():
    money = int(input("Enter the amount:"))
    money_1 = money * 0.99
    dos = input(f"""
        Amount entered - {money}
        Amount on the card - {money_1}

        1. Yes
        2. No
        >>> """)

    if dos == '1':
        data["card_balance"] += money_1
        print("Service completad successfully")
        return service_eng()
    else:
        print("Service terminated")
        return service_eng()


def rep_eng():
    reply = input("""
            1. Go back
            0. Termination of service
                 >>> """)
    if reply == "1":
        return service_eng()
    elif reply == "0":
        return main()

    else:
        print("Error!")
        return rep_eng()


def card_balance_eng():
    print(f"on the card {data['card_balance']}")
    return rep_eng()


def pin_code_eng():
    print("Change card code")
    pin_1 = int(input("Enter the new code: "))
    pin_2 = int(input("Enter the new code again: "))
    if pin_1 == pin_2 and 999 < pin_1 < 10000:
        print("Congratulations, your password has been successfully changed")
        data["card_pin"] = pin_1
        return service_eng()


def service_eng():
    print("Services")
    services = input("""
        Select the type of service :
            1. Card balance
            2. Filling out the card
            3. Cash withdrawal
            4. SMS
            5. Change password
            6. Termination of Service
            7. Card details 
                >>>>""")

    if services == "1":
        return card_balance_eng()

    elif services == "2":
        return add_money_eng()

    elif services == "3":
        return get_money_eng()

    elif services == "4":
        return sms_eng()

    elif services == "5":
        return pin_code_eng()

    elif services == "6":
        return main()

    elif services == "7":
        return malumot_eng()

    else:
        return service_eng()


def parol_eng():
    n = 2
    password = int(input("Enter the card password:"))
    while n >= 1 and data["card_pin"] != password:
        print("You entered an incorrect password")
        password = int(input("Enter the card password:"))
        if data["card_pin"] == password:
            return service_eng()

        n -= 1

    if data["card_pin"] == password:
        return service_eng()
    else:
        print("Your card has been blocked")
        return main()


def malumot_ru():
    print(f"""
    1. Hомер вашей карты - {data["card_number"]}
    2. Пароль вашей карты - {data["card_pin"]}
    3. Ваш карточный счет - {data["card_balance"]}
    4. Номер телефона, привязанный к вашей карте - {data["card_tel_number"]}
    5. Проверьте СМС-сообщение вашей карты - {data["status"]}
""")

    return service_ru()


def get_money_ru():
    global total_money
    money = int(input("Введите сумму - "))
    fd = money * 1.01
    if data["card_balance"] >= fd and total_money >= money:
        tad = input(f"""
         Cумму: {money}
         Cписывается с карты : {fd}

         1. Продолжать
         2. Возвращаться
              >>>""")
        if tad == '1':
            data["card_balance"] -= fd
            total_money -= money
            print(f"""Деньги были сняты 
Обслуживание завершено""")
            return service_ru()
        else:
            print("Обслуживание завершено")
            return service_ru()

    else:
        if total_money < money:
            print("В банкомате недостаточно денег")
        elif data["card_balance"] < fd:
            print("На карте недостаточно денег")
        else:
            print("Ошибка")
            return service_ru()


def sms_ru_on():
    if data["status"] == True:
        print("К этой карте уже привязан номер телефона")
        return sms_ru()
    else:
        tel_number = input("""
            Введите номер телефона:
                >>> +998 """)

        if len(tel_number) == 9:
            data["status"] = True
            data["card_tel_number"] = tel_number
            return service_ru()
        else:
            print("""
            Ошибка!
            Произошла ошибка при вводе номера телефона
                """)
            return sms_ru()


def sms_ru():
    print("SMS Service")
    tok = input("""
        Выберите услугу:
            1. Включи смс
            2. Удалить смс сообщение
            0. Возвращаться
                >>> """)

    if tok == "1":
        return sms_ru_on()

    elif tok == "2":
        if data["status"] == True:
            data["status"] = False
            data["card_tel_number"] = None
            print("SMS-сервис отключен")
            return sms_ru()
        else:
            sms_info = input("""
            Служба SMS-уведомлений недоступна!

            1. Включать
            0. Возвращаться
                >>> """)
        if sms_info == "1":
            return sms_ru_on()
        else:
            return service_ru()


def password_ru():
    n = 2
    pin_1 = input("Введите новый пароль")
    pin_2 = input("Подтвердите новый пароль")
    if password == pin_2:
        print("пароль изменен")
        return service_ru()


def add_money_ru():
    money = int(input("Введите сумму:"))
    money_1 = money * 0.99
    dos = input(f"""
        Введенная сумма - {money}
        Сумма на карте - {money_1}

        1. Да
        2. Нет
        >>> """)

    if dos == '1':
        data["card_balance"] += money_1
        print("Обслуживание завершено")
        return service_ru()
    else:
        print("Обслуживание прекращено")
        return service_ru()


def rep_ru():
    reply = input("""
            1. Возвращаться
            0. Прекращение обслуживания
                 >>> """)
    if reply == "1":
        return service_ru()
    elif reply == "0":
        return main()

    else:
        print("Ошибка!")
        return rep_ru()


def card_balance_ru():
    print(f"На карте {data['card_balance']}")
    return rep_ru()


def pin_code_ru():
    print("Изменить код карты")
    pin_1 = int(input("введите новый код: "))
    pin_2 = int(input("Подтвердите новый код: "))
    if pin_1 == pin_2 and 999 < pin_1 < 10000:
        print("Поздравляем, ваш пароль успешно изменен")
        data["card_pin"] = pin_1
        return service_ru()


def service_ru():
    print("Services")
    services = input("""
        Выберите тип услуги :
            1. Карточный счет
            2. Заполнение карты
            3. Выдача наличных
            4. CMC
            5. Изменить пароль
            6. Прекращение обслуживания
            7. Информация о карте
                >>>>""")

    if services == "1":
        return card_balance_ru()

    elif services == "2":
        return add_money_ru()

    elif services == "3":
        return get_money_ru()

    elif services == "4":
        return sms_ru()

    elif services == "5":
        return pin_code_ru()

    elif services == "6":
        return main()

    elif services == "7":
        return malumot_ru()

    else:
        return service_ru()


def parol_ru():
    n = 2
    password = int(input("Введите пароль карты:"))
    while n >= 1 and data["card_pin"] != password:
        print("Вы ввели неправильный пароль")
        password = int(input("Введите пароль карты:"))
        if data["card_pin"] == password:
            return service_ru()

        n -= 1

    if data["card_pin"] == password:
        return service_ru()
    else:
        print("Ваша карта заблокирована")
        return main()


def main():
    lenguage = input("""
    Tilni tanlang :
    1. Uzb
    2. Eng
    3. Rus
        >>>""")


    if lenguage == "1":
        return parol_uz()

    elif lenguage == "2":
        return parol_eng()

    elif lenguage == "3":
        return parol_ru()
    else:
        print(f"""Bunday til mavjud emas
No such language exists
Такого языка не существует""")
        return main()

if __name__ == "__main__":
        main()
