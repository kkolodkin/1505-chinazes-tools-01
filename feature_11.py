import requests
import time
def feature_11():
    try:
        r = requests.get("https://api.adviceslip.com/advice").json()
        print(r["slip"]["advice"])
    except:
        print("Ошибка 67")
    time.sleep(1)
