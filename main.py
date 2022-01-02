from flask import Flask, render_template
from CryptoModelV2 import formatTimeDataWithTime, predictCrypto
from PriceRetriever import headingGetter as getCryptoData
from PriceRetriever import roundCrypto, formatLargeNumber

app = Flask(__name__)
global name, symbol, price, pchange_1h, pchange_24h, pchange_7d, pchange_30d, pchange_60d, pchange_90d, market_cap
global x_real, y_real, x_predicted, y_predicted

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # x_real, y_real, x_predicted, y_predicted, ticker
    # symbol, specificData['price'], specificData['percent_change_1h'], +specificData['percent_change_24h'], \
    #           specificData['percent_change_7d'], specificData['percent_change_30d'], specificData['percent_change_60d'], \
    #           specificData['percent_change_90d'], specificData['market_cap']
    name, symbol, price, pchange_1h, pchange_24h, pchange_7d, pchange_30d, pchange_60d, pchange_90d, market_cap = getCryptoData("BTC")
    x_real, y_real, x_predicted, y_predicted = predictCrypto(symbol, daysToPredict=180)

    price = roundCrypto(price)
    pchange_1h = roundCrypto(pchange_1h)
    pchange_24h = roundCrypto(pchange_24h)
    pchange_7d = roundCrypto(pchange_7d)
    pchange_30d = roundCrypto(pchange_30d)
    pchange_60d = roundCrypto(pchange_60d)
    pchange_90d = roundCrypto(pchange_90d)
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

    return render_template("dashboardBigGraph.html", data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/education")
def education():
    return render_template("education.html")


app.run(host='0.0.0.0', port=8080, debug=True)