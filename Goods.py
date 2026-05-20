import json
import os
import requests
from dotenv import load_dotenv


class Goods():
    def __init__(self):
        load_dotenv()
        token = os.getenv('TOKEN_MS')
        self.header = header = {
            'Authorization': f'Bearer {token}',
            "Content-Type": "application/json"
        }

        ##############URLS######################
        self.assortment_url = 'https://api.moysklad.ru/api/remap/1.2/entity/assortment'
        self.goods_url = 'url = "https://api.moysklad.ru/api/remap/1.2/entity/product'
        self.warehouse_url = 'https://api.moysklad.ru/api/remap/1.2/entity/store'


    def get_request_to_ms(self, url, params=None):
        response = requests.get(url=url, headers= self.header, params=params)
        if response.status_code == 200:
            return response.json()

    def get_warehouses(self)->list:
        warehouse_list = list()
        warehouse_json = self.get_request_to_ms(self.warehouse_url)
        for wrhs_dict in warehouse_json['rows']:
            warehouse_list.append(wrhs_dict['name'])
        return warehouse_list


Goods().get_warehouses()