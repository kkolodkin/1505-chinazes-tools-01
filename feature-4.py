import random

def get_winner(player, computer):
    """Определяет победителя"""
    if player == computer:
        return "Ничья!"
    
    winning_combinations = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень"
    }
    
    if winning_combinations[player] == computer:
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_game():
    choices = ["камень", "ножницы", "бумага"]
    
    print("\n=== Игра 'Камень, ножницы, бумага' ===")
    print("Доступные варианты: камень, ножницы, бумага")
    print("Для выхода введите 'выход'")
    
    while True:

        player_choice = input("Ваш выбор: ").lower().strip()

        if player_choice == "выход":
            print("Спасибо за игру! До свидания!")
            break

        if player_choice not in choices:
            print("ОШИБКА: Неверный параметр!")
            print(f"Пожалуйста, выберите из: {', '.join(choices)}")
            continue

        computer_choice = random.choice(choices)

        print(f"Ваш выбор: {player_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        print(f"{get_winner(player_choice, computer_choice)}")


play_game()
