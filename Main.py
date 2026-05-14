import json

import requests

token = '9ac31b28b78eb109d8714c6fac7d5c551aeeed74'

url = 'https://api.moysklad.ru/api/remap/1.2/entity/assortment'
goods_url = 'url = "https://api.moysklad.ru/api/remap/1.2/entity/product'

header = {
    'Authorization': f'Bearer {token}',
    "Content-Type": "application/json"
}
params = {
    'filter': 'name = Диск тормозной 330 мм'
}

response = requests.get(url = url, headers= header, params=params)

if response.status_code == 200:
    goods = response.json()
    print(json.dumps(goods, indent=4, ensure_ascii=False))
