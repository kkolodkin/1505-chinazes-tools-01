import requests

def done_():
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json()
    print(f"{data['slip']['advice']}")

done_()