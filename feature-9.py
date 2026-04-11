import requests
import json

def get_weather_moscow():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': 55.7558,
        'longitude': 37.6176,
        'current_weather': True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  
        data = response.json()

        current_weather = data['current_weather']

        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']
        weathercode = current_weather['weathercode']

        weather_conditions = {
            0: "Ясно",
            1: "В основном ясно",
            2: "Переменная облачность",
            3: "Облачно",
            45: "Туман",
            48: "Туман с изморозью",
            51: "Лёгкий дождь",
            53: "Умеренный дождь",
            55: "Сильный дождь",
            61: "Лёгкий моросящий дождь",
            63: "Умеренный моросящий дождь",
            65: "Сильный моросящий дождь",
            71: "Лёгкий снег",
            73: "Умеренный снег",
            75: "Сильный снег",
            80: "Лёгкие ливни",
            81: "Умеренные ливни",
            82: "Сильные ливни",
            95: "Гроза",
            96: "Гроза с градом",
            99: "Сильная гроза с градом"
        }

        condition = weather_conditions.get(weathercode, "Неизвестно")

        print("🌤️ Погода в Москве:")
        print(f"Температура: {temperature} °C")
        print(f"Скорость ветра: {windspeed} м/с")
        print(f"Состояние: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
    except KeyError as e:
        print(f"Ошибка обработки данных: отсутствует ключ {e} в ответе API")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    get_weather_moscow()
