from flask import Flask, render_template
from api import Crypto

app = Flask(__name__)

'''import config file from root directory'''
app.config.from_object('config')

'''pass secret key as token value taken in Crypto class'''
crypto = Crypto(app.config['SECRET_KEY'])


@app.route("/top5")
def cmc_currency():
    '''access method and pass converter parameter as string ('USD', 'PLN', 'EUR' etc.) to obtain desired currency exchange'''
    convert = 'PLN'
    data = crypto.get_top_5_coins(convert)
    cryptoPrice = []
    for i in range(5):
        dict = {'name': data[i]['name'], 'slug': data[i]['slug'],
                 'price': data[i]['quote'][convert]['price'],
                 'percent_change_1h': round(data[i]['quote'][convert]['percent_change_1h'],2),
                 'percent_change_24h': round(data[i]['quote'][convert]['percent_change_24h'],2),
                 'percent_change_7d': round(data[i]['quote'][convert]['percent_change_7d'],2),
                 'percent_change_30d': round(data[i]['quote'][convert]['percent_change_30d'],2),
                 'percent_change_60d': round(data[i]['quote'][convert]['percent_change_60d'],2),
                 'percent_change_90d': round(data[i]['quote'][convert]['percent_change_90d'],2)}
        dict_copy = dict.copy()
        cryptoPrice.append(dict_copy)

    return render_template("index.html", price=cryptoPrice)

if __name__ == '__main__':
    app.run(debug=True)


