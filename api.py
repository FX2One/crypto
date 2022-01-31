from requests import Request, Session
import json


class Crypto:
    def __init__(self, token):
        self.base_url = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': token,
                        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_top_5_coins(self,convert):
        url = self.base_url + '/v1/cryptocurrency/listings/latest'
        parameters = {'start':'1',
                      'limit': '5',
                      'convert': convert}
        response = self.session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']

    def get_top_10_coins(self,convert):
        url = self.base_url + '/v1/cryptocurrency/listings/latest'
        parameters = {'start':'1',
                      'limit': '10',
                      'convert': convert}
        response = self.session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']


