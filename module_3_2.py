# Шапка работы
import sys
print ('Created by',sys.version)
print ('Домашняя работа по уроку "Способы вызова функции"')
print ('Студент Анисимов Алексей Юрьевич')
print ('-'*20)
# Блок описания функции
def send_email(message, recipient,*, sender='university.help@gmail.com'):
    # Блок начального задания переменных
    end_domen = ['.com','.ru','.net']
    err_dog = True
    err_domen = True
    # Проверка на наличие @ в адресе получателя (1) и принадлежности домена получателя списку end_domen, (2)
    # установка флагов проверки
    if recipient.find ('@') != -1 and sender.find ('@') != -1 : # (1)
        err_dog = False
    for i in end_domen: # (2)
        if recipient[::-1].find(i[::-1]) == 0 and sender[::-1].find(i[::-1]) == 0:
            err_domen = False
    # Проверка состояния флагов наличия @ в адресе получателя и принадлежности домена получателя списку end_domen
    if not(err_dog) and not(err_domen):
        # Ветка отсутствия ошибок в адресах
        # Проверка совпадения адресов отправителя и получателя
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        else:
            # Проверка отправителя на значение university.help@gmail.com
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        # Ветка ошибок в адресах
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
send_email('Привет', 'test@gmail.com', sender='post@gmail.com')
