from task_1 import *
from task_2 import *
def user_menu():
    menu = '*** Задача №1 ***\n' \
           ' *** Задача №2 ***\n' \
           ' Чтобы закончить введите "end"\n' \
           '------------------------------'
    user = input((f'Привет! Что будем проверять на этот раз?\n {menu} \n'))
    while user.lower() != 'end':
        if user.lower() == 'задача №1' or user.lower() == 'задача 1' or user.lower() == '1':
            with open('file_1.txt', 'r') as f1, open('file_2.txt', 'r') as f2:
                a = list(f1.readline().replace('*', '').split('+'))
                b = list(f2.readline().replace('*', '').split('+'))
                sl1 = dictionary(a)
                sl1 = dictionary_2(b, sl1)
                s = sum(sl1)
                print(s.replace('+', '', 1))
            user = input((f'\nЧто будем проверять дальше?\n {menu} \n'))
        elif user.lower() == 'задача №2' or user.lower() == 'задача 2' or user.lower() == '2':
            number_task_2 = list(map(int, input('Задайте последовательность числе через пробел:').split()))
            print(posled(number_task_2))
            user = input((f'\nЧто будем проверять дальше?\n {menu} \n'))
        else:
            print('Я тебя не понимаю. Давай ещё раз')
            user = input((f'Что будем проверять?\n {menu} \n'))