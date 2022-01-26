from flask import Flask, render_template
from api import Crypto

app = Flask(__name__)

'''import config file from root directory'''
app.config.from_object('config')

'''pass secret key as token value taken in Crypto class'''
crypto = Crypto(app.config['SECRET_KEY'])


@app.route("/top5")
def cmc_currency():
    '''access method and pass converter paramter to obtain desired currency exchange'''
    data = crypto.get_top_5_coins('PLN')
    bitcoinPrice = data[0]
    return render_template("index.html", price=bitcoinPrice)

if __name__ == '__main__':
    app.run(debug=True)

