import requests
import random

def get_random_question():
    try:
        response = requests.get("https://the-trivia-api.com/v2/questions")
        response.raise_for_status()  
        data = response.json()

        if not data:
            print("Не удалось получить вопрос. Попробуйте позже.")
            return None

        question_data = data[0]

        return {
            'question': question_data['question'],
            'correct_answer': question_data['correctAnswer'],
            'incorrect_answers': question_data.get('incorrectAnswers', []),
        }
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Ошибка обработки данных: {e}")
        return None

def display_question(question_data):
    print(f"\nВопрос: {question_data['question']}")

    all_answers = [question_data['correct_answer']] + question_data['incorrect_answers']
    random.shuffle(all_answers)

    for i, answer in enumerate(all_answers, start=1):
        print(f"{i}. {answer}")

    return all_answers

def get_user_answer(num_options):
    while True:
        try:
            choice = int(input(f"\nВаш ответ (1-{num_options}): "))
            if 1 <= choice <= num_options:
                return choice
            else:
                print(f"Пожалуйста, введите число от 1 до {num_options}.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def check_answer(user_choice, all_answers, correct_answer):
    selected_answer = all_answers[user_choice - 1]
    return selected_answer == correct_answer

def feature_5():
    score = 0
    total_questions = 0

    print("Добро пожаловать в викторину!")
    print("Отвечайте на вопросы, чтобы набрать очки. Для выхода введите 'q'.")

    while True:
    
        question_data = get_random_question()
        if not question_data:
            break

        total_questions += 1

        all_answers = display_question(question_data)

        user_choice = get_user_answer(len(all_answers))

        if check_answer(user_choice, all_answers, question_data['correct_answer']):
            print("Правильно! +1 очко.")
            score += 1
        else:
            correct_index = all_answers.index(question_data['correct_answer']) + 1
            print(f"Неправильно. Правильный ответ: {correct_index}. {question_data['correct_answer']}")

        continue_game = input("\nХотите продолжить? (y/n): ").strip().lower()
        if continue_game in ['n', 'нет', 'no']:
            break

    print(f"\nИгра окончена!")
    print(f"Всего вопросов: {total_questions}")
    print(f"Правильных ответов: {score}")
    if total_questions > 0:
        percentage = (score / total_questions) * 100
        print(f"Результат: {percentage:.1f}% правильных ответов")