import pandas_datareader as web
from datetime import datetime, timedelta

def getVolatility(ticker, pastDays):
    if (pastDays <= 1 or not isinstance(pastDays, int)):
        print("Invalid")
        return 0
    else:
        end = datetime.now()
        start = end - timedelta(days=pastDays)

        # Retrieve Data
        crypto_currency = ticker.upper()
        against_currency = 'USD'

        df = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)

        n = len(df)
        openingPrice = float(df[['Open']].iloc[0])
        sum = 0

        for i in range(n):
            sum += (openingPrice - float(df[['Open']].iloc[i]))**2

        stdDev = (sum/n)**0.5

        volatilityInDollars = float((n**0.5) * stdDev)
        print(volatilityInDollars)

        return volatilityInDollars


getVolatility("BTC", 31)
