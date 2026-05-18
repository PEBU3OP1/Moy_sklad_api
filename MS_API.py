import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN_MS')
print(token)
exit()
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
