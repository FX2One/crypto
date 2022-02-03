from requests import Request, Session
import json

class Crypto:
    '''token is *args taken from .env file'''
    def __init__(self, token):
        self.base_url = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': token,
                        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_top_coins(self,limit,convert):
        url = self.base_url + '/v1/cryptocurrency/listings/latest'
        parameters = {'start':'1',
                      'limit': limit,
                      'convert': convert}
        response = self.session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['data']





