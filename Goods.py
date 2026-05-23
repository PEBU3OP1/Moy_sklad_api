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
            'Accept-Encoding': 'gzip',
            "Content-Type": "application/json"
        }

        ##############URLS######################
        self.assortment_url = 'https://api.moysklad.ru/api/remap/1.2/entity/assortment'
        self.product_url = 'https://api.moysklad.ru/api/remap/1.2/entity/product'
        self.warehouse_url = 'https://api.moysklad.ru/api/remap/1.2/entity/store'
        self.product_folder_url = 'https://api.moysklad.ru/api/remap/1.2/entity/productfolder'
        self.uom_url = 'https://api.moysklad.ru/api/remap/1.2/entity/uom'

    def get_request_to_ms(self, url, params=None):
        response = requests.get(url=url, headers=self.header, params=params)
        if response.status_code == 200:
            return response.json()

    def post_request_to_ms(self, url, body_json=None):
        response = requests.post(url=url, headers=self.header, json=body_json)
        print(response.text)
        if response.status_code == 200:
            return response.json()

    def get_product_folders(self):
        product_folders = self.get_request_to_ms(url=self.product_folder_url)
        # print(json.dumps(product_folders, indent=4, ensure_ascii=False))
        for folder in product_folders['rows']:
            if folder['name'] == 'Номенклатура':
                print(json.dumps(folder, indent=4, ensure_ascii=False))

    def get_uom(self):
        response = self.get_request_to_ms(url=self.uom_url)
        print(json.dumps(response, indent=4, ensure_ascii=False))

    def get_warehouses(self) -> list:
        warehouse_list = list()
        warehouse_json = self.get_request_to_ms(self.warehouse_url)
        for wrhs_dict in warehouse_json['rows']:
            warehouse_list.append(wrhs_dict['name'])
        return warehouse_list

    def add_new_product(self):
        product_params = {
            'name': 'Banana',
            'code': 'test_banana',
            'description': 'AFrica Banana',
            'productFolder': {
                'meta': {
                    'href': 'https://api.moysklad.ru/api/remap/1.2/entity/productfolder/64e51b1d-4ec6-11f1-0a80-045400101aa5',
                    'type': 'productfolder',
                    'mediaType': 'application/json'
                }

            },
            'uom': {
                "meta": {
                    "href": "https://api.moysklad.ru/api/remap/1.2/entity/uom/19f1edc0-fc42-4001-94cb-c9ec9c62ec10",
                    "type": "uom",
                    "mediaType": "application/json"
                }
            },
            'article': 'banan_ueban'
        }
        g = self.post_request_to_ms(url=self.product_url, body_json=product_params)
        print(g)


Goods().add_new_product()
# Goods().get_product_folders()
# Goods().get_uom()
