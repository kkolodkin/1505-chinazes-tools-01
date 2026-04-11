import requests

def done_():
    response = requests.get('http://api.quotable.io/random')
    data = response.json()
    print(f"Цитата: {data['content']}")
    print(f"Автор: {data['author']}")
done_()

