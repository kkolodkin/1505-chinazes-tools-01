from deep_translator import GoogleTranslator

def feature_14():
    try:
        translator = GoogleTranslator(source='ru', target='en')

        print("--- Русско-английский переводчик ---")
        print("Введите 'exit' для выхода из программы.")

        while True:
            text = input("\nВведите текст на русском: ")

            if text.lower() == 'exit':
                print("Программа завершена.")
                break
            if not text.strip():
                continue
            try:
                translation = translator.translate(text)
                print(f"Перевод на английский: {translation}")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
    except:
        print("Ошибка 67")

