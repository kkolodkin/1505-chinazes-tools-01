
import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль заданной длины"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Пример использования
password = generate_password(16)
print(f"Сгенерированный пароль: {password}")
