import pandas_datareader as web
import datetime as dt
# from prophet import Prophet
from fbprophet import Prophet
import numpy as np
import matplotlib.pyplot as plt

def formatTimeDataWithTime(x):
    x = np.array(x.to_pydatetime(), dtype=np.datetime64)
    x_list = []
    for i in x:
        x_list.append(str(i)[:-16])
    return x_list

def predictCrypto(ticker, daysToPredict=180):
    try:
        # Retrieve Data
        crypto_currency = ticker.upper()
        against_currency = 'USD'

        start = dt.datetime(2016, 1, 1)
        end = dt.datetime.now()

        periods = daysToPredict

        df = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)
        df['ds'] = df.index
        df['y'] = df['Close']

        m = Prophet()
        m.fit(df)

        future = m.make_future_dataframe(periods=180)
        future.tail(2)

        forecast = m.predict(future)
        forecast.tail(2)

        # plt.figure(figsize=(15,5))
        # plt.title(crypto_currency + against_currency + ' price prediction')
        # plt.plot(df['ds'], df['Close'])
        # plt.plot(forecast['ds'], forecast['yhat'], color='green')
        # # plt.plot(forecast['ds'], forecast['yhat_lower'], alpha=0.1, color='blue')
        # # plt.plot(forecast['ds'], forecast['yhat_upper'], alpha=0.1, color='blue')
        # plt.legend('upper right')
        #
        # # plt.fill_between(forecast['ds'], forecast['yhat_upper'], forecast['yhat_lower'], alpha=0.1)
        # # plt.plot(forecast['ds'], forecast['trend'])
        #
        # plt.show()

        predicted_data = forecast[len(df['Close']):len(forecast['yhat'])]
        predicted_data.set_index(predicted_data['ds'], drop=True, append=False, inplace=True)
        predicted_data = predicted_data[['trend', 'yhat_lower', 'yhat_upper', 'yhat']]

        forecast.set_index(forecast['ds'], drop=True, append=False, inplace=True)
        forecast = forecast[['trend', 'yhat_lower', 'yhat_upper', 'yhat']]

        return formatTimeDataWithTime(df.index), df['Close'].to_numpy().tolist(), formatTimeDataWithTime(forecast.index), forecast['yhat'].to_numpy().tolist()
    except:
        print("Error")
        return None, None, None, None


x_real, y_real, x_predicted, y_predicted = predictCrypto("IOTX", 180)
print(x_real)
print(y_real)
print(x_predicted)
print(y_predicted)
