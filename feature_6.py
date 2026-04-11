
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(password)

def feature_6():
    n = int(input("Введите длину пароля: "))
    generate_password(n)
