def caesar_cipher(text, shift):
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted)
        elif 'а' <= char <= 'я':
            shifted = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            result.append(shifted)
        elif 'А' <= char <= 'Я':
            shifted = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            result.append(shifted)
        elif char.isdigit():
            shifted = str((int(char) + shift) % 10)
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)



def feature_8():
    message = input("Введите сообщение для шифрования: ")
    try:
        shift = int(input("Введите сдвиг (целое число): "))
    except ValueError:
        print("Ошибка: сдвиг должен быть целым числом!")
        return
    encrypted = caesar_cipher(message, shift)
    print(f"Зашифрованное сообщение: {encrypted}")

    decrypted = caesar_cipher(encrypted, -shift)
    print(f"Расшифрованное сообщение: {decrypted}")

