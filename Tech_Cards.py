import numpy as np
from Goods import Goods
from Base import Base
import pandas as pd


class Tech_Cards(Base):
    def __init__(self):
        super().__init__()

    def get_cards_names(self):
        response = self.get_request_to_ms(self.techcards_url)
        for card in response['rows']:
            print(card['name'])

    def get_card(self):
        pass

    def add_cards(self, materials_list: list, products_list: list):
        card_params = {
            'name': 'Make_Banana_great_again',
            'materials': materials_list,
            'products': products_list
        }

        response = self.post_request_to_ms(url=self.techcards_url, body_json=card_params)
        print(response)

    def add_card(self):
        materials_list = list()
        products_list = list()

        cards_csv = pd.read_csv(self.csv_file_test, sep=';', encoding='utf-8-sig', low_memory=False)
        for i, row in cards_csv.iterrows():
            for key, val in row.items():
                if 'material_article' in key:
                    if str(val) != 'nan':
                        one_material_dict = {
                            'quantity': row[str(key).replace('article', 'quantity')],
                            'assortment': {
                                'meta': {
                                    'href': self.product_url + f'/{Goods().get_product_id(val)}',
                                    'type': 'product',
                                    'mediaType': 'application/json'
                                }
                            }
                        }
                        materials_list.append(one_material_dict)
                elif 'product_article' in key:
                    one_product_dict = {
                        'quantity': row[str(key).replace('article', 'quantity')],
                        'assortment': {
                            'meta': {
                                'href': self.product_url + f'/{Goods().get_product_id(val)}',
                                'type': 'product',
                                'mediaType': 'application/json'
                            }
                        }
                    }
                    products_list.append(one_product_dict)
        card_params = {
            'name': 'Make_Banana_great_again',
            'materials': materials_list,
            'products': products_list
        }

        response = self.post_request_to_ms(url=self.techcards_url, body_json=card_params)
        print(response)


# Tech_Cards().add_cards()
# Tech_Cards().add_card()
