import random
print("Угадай число, которое я загадал")
minn = int(input("Минимальное число диапазона: "))
maxn = int(input("Максимальное число диапазона: "))
ans = random.randint(minn, maxn)
c = 0
while True:
    v = int(input("Как ты думаешь какое число я загадал? "))
    c += 1

    if v < ans:
        print("Моё число больше")
    elif v >ans:
        print("Моё число меньше")
    else:
        print(f"Угадал! Моё число: {ans}. Попыток : {c}")
        break
