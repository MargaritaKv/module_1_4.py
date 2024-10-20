def send_email (message, recepient, sender = "university.help@gmail.com"):
    if not (recepient.endswith (".com") or recepient.endswith (".ru") or recepient.endswith (".net")):
        print ("Невозможно отправить письма с адреса", sender ,"на адрес", recepient)
    if not (sender (".com") or sender (".ru") or sender (".net")):
        if sender == recepient:
            print ("Невозможно отправить письмо самому себе")
        elif sender == "university.help@gmail.com":
            print ("Письмо успешно отправлено с адреса", sender, "на адрес", recepient)
        else:
            print ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recepient)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


