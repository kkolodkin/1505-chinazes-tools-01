import requests
import time
def feature_10():
    response = requests.get('http://api.quotable.io/random')
    data = response.json()
    print(f"Цитата: {data['content']}")
    print(f"Автор: {data['author']}")
    time.sleep(1)

