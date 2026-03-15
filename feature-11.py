import requests

r = requests.get("https://api.adviceslip.com/advice").json()
print(r["slip"]["advice"])
