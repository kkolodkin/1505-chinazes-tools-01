import random

def feature_7():
    while True:
        try:
            count = int(input("Введите количество чисел от 1 до 1000: "))
            if 1 <= count <= 1000:
                break
            else:
                print("Ошибка: количество должно быть в диапазоне от 1 до 1000. Попробуйте снова.")
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

    print(f"Диапазон чисел: от {-10**10} до {10**10}")
    while True:
        try:
            min_val = int(input(f"Введите минимальное число (не меньше {-10**10}): "))
            max_val = int(input(f"Введите максимальное число (не больше {10**10}): "))
            
            if min_val < -10**10:
                print(f"Ошибка: минимальное число не может быть меньше {-10**10}. Попробуйте снова.")
                continue
            if max_val > 10**10:
                print(f"Ошибка: максимальное число не может быть больше {10**10}. Попробуйте снова.")
                continue

            if min_val > max_val:
                print("Ошибка: минимальное число не может быть больше максимального. Попробуйте снова.")
                continue

            break
        except ValueError:
            print("Ошибка: пожалуйста, введите целые числа.")
    random_numbers = [random.randint(min_val, max_val) for _ in range(count)]
    print(f"\nСгенерированные числа ({count} шт. в диапазоне от {min_val} до {max_val}):")
    print(random_numbers)



