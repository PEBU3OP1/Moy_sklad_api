import json
import os
import requests
from dotenv import load_dotenv
import pandas as pd


class Base:
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
        self.techcards_url = 'https://api.moysklad.ru/api/remap/1.2/entity/processingplan'

        ##############PATHS######################
        self.csv_file_test = 'test.csv'

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

if __name__ == '__main__':
    Base()