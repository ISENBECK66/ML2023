import requests

url = 'https://7xgghpctxk.execute-api.eu-west-3.amazonaws.com/test/predict'

data = {'url':'https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg'}

#data = {'url':'https://imgs.search.brave.com/gI0-mO_syvJa21FFgB4XzD8fCUJuOZb6iTLMhZcgp7U/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9hbmlt/YWxpLndpa2kvd3At/Y29udGVudC91cGxv/YWRzLzIwMTgvMDcv/YWJlamExLmpwZw'}



result = requests.post(url, json=data).json()
print(result)
