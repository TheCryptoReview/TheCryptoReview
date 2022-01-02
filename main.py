from flask import Flask, render_template
from CryptoModelV2 import formatTimeDataWithTime, predictCrypto
from PriceRetriever import headingGetter as getCryptoData

app = Flask(__name__)


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
    symbol, price, pchange_1h, pchange_24h, pchange_7d, pchange_30d, pchange_60d, pchange_90d, market_cap = getCryptoData("ETH")
    x_real, y_real, x_predicted, y_predicted = predictCrypto(symbol, daysToPredict=180)

    data = {
        'coinName': symbol,
        'dates': x_predicted,
        'historical_data': y_real,
        'predicted_data': y_predicted
    }

    return render_template("dashboardBigGraph.html", data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/education")
def education():
    return render_template("education.html")


app.run(host='0.0.0.0', port=8080, debug=True)