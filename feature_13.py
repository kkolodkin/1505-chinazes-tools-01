import requests
import time

def feature_13():
    try:
        r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en").json()
        print(r['text'])
    except:
        print("Ошибка 67")
    time.sleep(1)
