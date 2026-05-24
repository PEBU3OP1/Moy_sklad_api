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
    def add_card(self):
        card_params = {
            'name': 'Make_Banana_great_again',
            'materials': [{
                'quantity': 1,
                'assortment': {
                    'meta': {
                        'href': self.product_url + '/40b66247-5524-11f1-0a80-107100491e8b',
                        'type': 'product',
                        'mediaType': 'application/json'
                    }
                }
            }
            ],
            'products': [{
                'quantity': 1,
                'assortment': {
                    'meta':{
                        'href': self.product_url + '/9970d740-4ec6-11f1-0a80-1d29001072a9',
                        'type': 'product',
                        'mediaType': 'application/json'
                    }
                }
            }]
        }

        response = self.post_request_to_ms(url=self.techcards_url, body_json=card_params)
        print(response)

    def add_cards(self):
        cards_csv = pd.read_csv(self.csv_file_test, sep=';', encoding='utf-8-sig', low_memory=False)
        print(cards_csv)


Tech_Cards().add_cards()
