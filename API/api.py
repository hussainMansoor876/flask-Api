import requests

link = 'http://127.0.0.1:5000/form'
data = requests.get(link).json()

print(data)