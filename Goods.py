import json
import os
import requests
from dotenv import load_dotenv
from Base import Base


class Goods(Base):
    def __init__(self):
        super().__init__()

    def add_product(self):
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

    def get_product_id(self, article: str):
        article_product_url = self.product_url + '?filter=article={}'.format(article)
        products_json = self.get_request_to_ms(url=article_product_url)
        # print(json.dumps(products_json, ensure_ascii=False, indent=4))
        if products_json:
            for product in products_json['rows']:
                return product['id']





# Goods().get_product_id('banan_ueban')
# Goods().add_new_product()
# Goods().get_product_folders()
# Goods().get_uom()
