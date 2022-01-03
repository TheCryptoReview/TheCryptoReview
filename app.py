from flask import Flask, render_template, request, redirect, url_for, jsonify
from CryptoModelV2 import formatTimeDataWithTime, predictCrypto
from PriceRetriever import headingGetter as getCryptoData
from PriceRetriever import roundCrypto, formatLargeNumber, roundCryptoWithoutDollar, priceGreed

app = Flask(__name__)
global name, symbol, price, pchange_1h, pchange_24h, pchange_7d, pchange_30d, pchange_60d, pchange_90d, market_cap
global x_real, y_real, x_predicted, y_predicted

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/dashboard.html", methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        try:
            coinName = request.form['coinName']
            name, symbol, price, pchange_1h, pchange_24h, pchange_7d, pchange_30d, pchange_60d, pchange_90d, market_cap = getCryptoData(
                coinName)
            x_real, y_real, x_predicted, y_predicted = predictCrypto(symbol, daysToPredict=180)

            price = roundCrypto(price)
            pchange_1h = roundCrypto(pchange_1h)
            pchange_24h = roundCryptoWithoutDollar(pchange_24h)
            pchange_7d = roundCryptoWithoutDollar(pchange_7d)
            pchange_30d = roundCryptoWithoutDollar(pchange_30d)
            pchange_60d = roundCryptoWithoutDollar(pchange_60d)
            pchange_90d = roundCryptoWithoutDollar(pchange_90d)
            market_cap = roundCrypto(market_cap)

            data = {
                'coin_name': name,
                'coin_ticker': symbol,
                'dates': x_predicted,
                'historical_data': y_real,
                'predicted_data': y_predicted,
                'price': price,
                'pchange_24h': pchange_24h,
                'pchange_7d': pchange_7d,
                'pchange_30d': pchange_30d,
                'pchange_60d': pchange_60d,
                'pchange_90d': pchange_90d,
                'market_cap': market_cap
            }

            return render_template("dashboardBigGraph.html", data=data, name=name, cr=10.0, fg=10)
        except:
            print("Error")

    try:
        coinName = request.args.get("token")
        try:
            name, symbol, price, pchange_1h, pchange_24h, pchange_7d, pchange_30d, pchange_60d, pchange_90d, market_cap = getCryptoData(
                coinName)
            x_real, y_real, x_predicted, y_predicted = predictCrypto(symbol, daysToPredict=180)

            price = roundCrypto(price)
            pchange_1h = roundCrypto(pchange_1h)
            pchange_24h = roundCryptoWithoutDollar(pchange_24h)
            pchange_7d = roundCryptoWithoutDollar(pchange_7d)
            pchange_30d = roundCryptoWithoutDollar(pchange_30d)
            pchange_60d = roundCryptoWithoutDollar(pchange_60d)
            pchange_90d = roundCryptoWithoutDollar(pchange_90d)
            market_cap = roundCrypto(market_cap)

            data = {
                'coin_name': name,
                'coin_ticker': symbol,
                'dates': x_predicted,
                'historical_data': y_real,
                'predicted_data': y_predicted,
                'price': price,
                'pchange_24h': pchange_24h,
                'pchange_7d': pchange_7d,
                'pchange_30d': pchange_30d,
                'pchange_60d': pchange_60d,
                'pchange_90d': pchange_90d,
                'market_cap': market_cap
            }

            return render_template("dashboardBigGraph.html", data=data, name=name, cr=10.0, fg=10)
        except:
            print("Error")
    except:
        print("No token")

    coinName = 'BTC'
    name, symbol, price, pchange_1h, pchange_24h, pchange_7d, pchange_30d, pchange_60d, pchange_90d, market_cap = getCryptoData(
        coinName)
    x_real, y_real, x_predicted, y_predicted = predictCrypto(symbol, daysToPredict=180)

    price = roundCrypto(price)
    pchange_1h = roundCrypto(pchange_1h)
    pchange_24h = roundCryptoWithoutDollar(pchange_24h)
    pchange_7d = roundCryptoWithoutDollar(pchange_7d)
    pchange_30d = roundCryptoWithoutDollar(pchange_30d)
    pchange_60d = roundCryptoWithoutDollar(pchange_60d)
    pchange_90d = roundCryptoWithoutDollar(pchange_90d)
    market_cap = roundCrypto(market_cap)

    data = {
        'coin_name': name,
        'coin_ticker': symbol,
        'dates': x_predicted,
        'historical_data': y_real,
        'predicted_data': y_predicted,
        'price': price,
        'pchange_24h': pchange_24h,
        'pchange_7d': pchange_7d,
        'pchange_30d': pchange_30d,
        'pchange_60d': pchange_60d,
        'pchange_90d': pchange_90d,
        'market_cap': market_cap
    }

    return render_template("dashboardBigGraph.html", data=data, name=name, cr=10.0, fg=10)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/education.html")
def education():
    return render_template("education.html")


if __name__ == '__main__':
  app.run()
