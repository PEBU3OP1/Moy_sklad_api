import json
import os
import requests
from dotenv import load_dotenv

class MS_Ap:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('TOKEN_MS')
        self.header = {
            'Authorization': f'Bearer {self.token}',
            "Content-Type": "application/json"
        }

        #########   URLS  ###########
        self.assortment_url = 'https://api.moysklad.ru/api/remap/1.2/entity/assortment'
        self.goods_url = 'url = "https://api.moysklad.ru/api/remap/1.2/entity/product'
        self.warehouse_url = 'https://api.moysklad.ru/api/remap/1.2/entity/store'

    def get_info_by_api(self, url, params=None):
        response = requests.get(url=url, headers = self.header, params=params)
        if response.status_code == 200:
            result = response.json()
            print(json.dumps(result, indent=4, ensure_ascii=False))
            return result
        else:
            print(response.status_code)
    def get_goods(self):

        params = {
            'filter': 'name = Диск тормозной 330 мм'
        }

        response = requests.get(url = self.assortment_url, headers= self.header, params=params)

        if response.status_code == 200:
            goods = response.json()
            print(json.dumps(goods, indent=4, ensure_ascii=False))


    def get_warehouses(self):
        for wrhs_name in self.get_info_by_api(self.warehouse_url)['rows']:



MS_Ap().get_warehouses()