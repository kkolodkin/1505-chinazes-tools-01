import requests

r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en").json()
print(r)
