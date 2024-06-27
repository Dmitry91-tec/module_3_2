def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    list_ = (".com", ".ru", ".net")
    while True:
        if not "@" in message and not "@" in recipient or not sender.endswith(list_):
            print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient)
            break
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            break
        if sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient)
            break
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient)
            break

#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')