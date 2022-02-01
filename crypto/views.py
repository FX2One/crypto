from . import app
from flask import Flask, render_template
from api import Crypto

app.config.from_object('config')

'''passes secret key as token value taken in Crypto class'''
crypto = Crypto(app.config['SECRET_KEY'])

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



@app.route("/top-5")
def cmc_currency5():
    cryptoPrice = cmc_currency(5, 'PLN')

    return render_template("top_five.html", price=cryptoPrice)


@app.route("/top-10")
def cmc_currency10():
    cryptoPrice = cmc_currency(10, 'PLN')

    return render_template("top_ten.html", price=cryptoPrice)

@app.route("/top-15")
def cmc_currency15():
    cryptoPrice = cmc_currency(15, 'PLN')

    return render_template("top_15.html", price=cryptoPrice)