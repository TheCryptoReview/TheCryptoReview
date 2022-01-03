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
        coinName = request.form['coinName']
        return redirect("/dashboard.html?token="+coinName, code=302)

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

            confidence = 0
            preLast = y_predicted[len(y_predicted) - 1]
            realLast = y_real[len(y_real) - 1]
            if preLast <= realLast:
                confidence = (1 - ((realLast - preLast) / realLast)) * 50
            else:
                confidence = (1 - ((realLast - preLast) / preLast)) * 50
            confidence = round(confidence, 1)
            fearRating, emotion = priceGreed()

            return render_template("dashboardBigGraph.html", data=data, name=name,fg=fearRating,cr=confidence)
        except:
            print("Error")
    except:
        print("No token")

    coinName = 'BTC'
    return redirect("/dashboard.html?token=" + coinName, code=302)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/education.html")
def education():
    return render_template("education.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
  # app.run()
