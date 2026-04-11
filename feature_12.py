import requests
import time

def feature_12():
    r = requests.get("https://v2.jokeapi.dev/joke/Programming").json()
    if r["type"] == "single":
        print(r["joke"])
    else:
        print(f"{r['setup']}\n{r['delivery']}")
    time.sleep(1)