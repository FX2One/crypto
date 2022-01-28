from flask import Flask, render_template
from api import Crypto

app = Flask(__name__)

'''import config file from root directory'''
app.config.from_object('config')

'''pass secret key as token value taken in Crypto class'''
crypto = Crypto(app.config['SECRET_KEY'])


@app.route("/top5")
def cmc_currency():
    '''access method and pass converter parameter to obtain desired currency exchange'''
    data = crypto.get_top_5_coins('PLN')
    cryptoPrice = []
    for i in range(5):
        dict = {'name': data[i]['name'], 'slug': data[i]['slug'],
                 'price': data[i]['quote']['PLN']['price'],
                 'percent_change_1h': data[i]['quote']['PLN']['percent_change_1h'],
                 'percent_change_24h': data[i]['quote']['PLN']['percent_change_24h'],
                 'percent_change_7d': data[i]['quote']['PLN']['percent_change_7d'],
                 'percent_change_30d': data[i]['quote']['PLN']['percent_change_30d'],
                 'percent_change_60d': data[i]['quote']['PLN']['percent_change_60d'],
                 'percent_change_90d': data[i]['quote']['PLN']['percent_change_90d']}
        dict_copy = dict.copy()
        cryptoPrice.append(dict_copy)
    return render_template("index.html", price=cryptoPrice)

if __name__ == '__main__':
    app.run(debug=True)


