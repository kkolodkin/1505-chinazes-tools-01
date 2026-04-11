import random
print("Угадай число, которое я загадал")
def f(p):
    while True:
        try:
            num = int(input(p))
            return num
        except ValueError:
            print("Ошибка. Введи число")
while True:
    minn = int(input("Минимальное число диапазона: "))
    maxn = int(input("Максимальное число диапазона: "))
    if minn >= maxn:
        print("Ошибка. максимальное число диапазона должно быть больше минимаьного")
    else:
        break
    ans = random.randint(minn, maxn)
    c = 0
while True:
    try:
        v = int(input("Как ты думаешь какое число я загадал? "))
        c += 1
        if v < ans:
            print("Моё число больше")
        elif v >ans:
            print("Моё число меньше")
        else:
            print(f"Угадал! Моё число: {ans}. Попыток : {c}")
            break
    except ValueError:
        print("Введи число")
        continue
