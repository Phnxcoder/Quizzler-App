import requests

api = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')

data = api.json()

question_data = data['results']
print(question_data)