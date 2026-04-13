import test
import importlib
from feature_1 import feature_1
from feature_2 import feature_2
from feature_3 import feature_3
from feature_4 import feature_4
from feature_5 import feature_5
from feature_6 import feature_6
from feature_7 import feature_7
from feature_8 import feature_8
from feature_9 import feature_9
from feature_10 import feature_10
from feature_11 import feature_11
from feature_12 import feature_12
from feature_13 import feature_13
from feature_14 import feature_14


def print_menu():
    print(
'''
============================
Menu options

1. Run Test Module
2. Exit
3. Игра угадай число
4. Быки и коровы
5. Игра крестики-нолики
6. Игра камень, ножницы, бумага
7. Игра викторина
8. Генератор паролей
9. Генератор случайных чисел
10. Шифрование/дешифрование
11. Погода в Москве
12. Случайная цитата
13. Случайный совет
14. Случайная шутка о программистах
15. Случайный факт
16. Русско-английской переводчик
============================
''')

prog = [
    "feature-1.py",
    "feature-2.py",
    "feature-3.py",
    "feature-4.py",
    "feature-5.py",
    "feature-6.py",
    "feature-7.py",
    "feature-8.py",
    "feature-9.py",
    "feature-10.py",
    "feature-11.py",
    "feature-12.py",
    "feature-13.py",
    "feature-14.py"
]

print("Hello! Welcome to Chinazes Tools!")

while 1:
    print_menu()
    user_choice = input("Select a menu option number: ")
    print()
    
    if user_choice == '1':
        test.run()
    if user_choice == '2':
        print("Bye!")
        break
    elif 2 < int(user_choice) < 17:
        # print(prog[int(user_choice) - 3])
        module_name = f"feature_{int(user_choice)-2}"
        function_name = f"feature_{int(user_choice)-2}"
        module = importlib.import_module(module_name)
        func = getattr(module, function_name)
        func()
    else:
        print("Invalid choice. Try again.")
