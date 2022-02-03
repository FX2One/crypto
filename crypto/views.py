from . import app
from flask import render_template
from api import Crypto

app.config.from_object('config')

'''passes secret key as token value taken in Crypto class'''
crypto = Crypto(app.config['SECRET_KEY'])

'''appends values as list of dictionaries by calling API'''
def cmc_currency(limit,convert):
    data = crypto.get_top_coins(limit,convert)
    cryptoPrice = []
    for i in range(limit):
        dict = {'name': data[i]['name'],
                'symbol': data[i]['symbol'],
                'price': round(data[i]['quote'][convert]['price'],2),
                'percent_change_1h': round(data[i]['quote'][convert]['percent_change_1h'],2),
                'percent_change_24h': round(data[i]['quote'][convert]['percent_change_24h'],2),
                'percent_change_7d': round(data[i]['quote'][convert]['percent_change_7d'],2),
                'percent_change_30d': round(data[i]['quote'][convert]['percent_change_30d'],2),
                'percent_change_60d': round(data[i]['quote'][convert]['percent_change_60d'],2),
                'percent_change_90d': round(data[i]['quote'][convert]['percent_change_90d'],2)}
        dict_copy = dict.copy()
        cryptoPrice.append(dict_copy)
    return cryptoPrice

@app.route("/")
def index():
    return render_template("index.html")

'''provide number in URL to display amount of cryptocurrencies to display manually'''
'''change convert symbol to desired one to have currency you want'''
@app.route("/top/<int:number>")
def cmc_currency_top(number):
    convert = 'PLN'
    cryptoPrice = cmc_currency(number, convert)
    return render_template("top_coin.html", price=cryptoPrice)
