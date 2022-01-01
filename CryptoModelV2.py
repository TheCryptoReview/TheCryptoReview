# import pandas as pd
# import pandas_datareader as web
# import datetime as dt
# from prophet import Prophet
# import matplotlib.pyplot as plt

# def predictCrypto(ticker):
#     # Retrieve Data
#     crypto_currency = ticker.upper()
#     against_currency = 'USD'

#     start = dt.datetime(2016, 1, 1)
#     end = dt.datetime.now()

#     periods = 180

#     df = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)
#     df['ds'] = df.index
#     df['y'] = df['Close']

#     # print(df.head(2))

#     m = Prophet()
#     m.fit(df)

#     future = m.make_future_dataframe(periods=180)
#     future.tail(2)

#     forecast = m.predict(future)
#     forecast.tail(2)

#     plt.figure(figsize=(15,5))
#     plt.title(crypto_currency + against_currency + ' price prediction')
#     plt.plot(df['ds'], df['Close'])
#     plt.plot(forecast['ds'], forecast['yhat'], color='green')
#     plt.plot(forecast['ds'], forecast['yhat_lower'], alpha=0.1, color='blue')
#     plt.plot(forecast['ds'], forecast['yhat_upper'], alpha=0.1, color='blue')
#     plt.legend('upper right')

#     plt.fill_between(forecast['ds'], forecast['yhat_upper'], forecast['yhat_lower'], alpha=0.1)
#     plt.plot(forecast['ds'], forecast['trend'])

#     plt.show()

#     predicted_data = forecast[len(df['Close']):len(forecast['yhat'])]
#     predicted_data.set_index(predicted_data['ds'], drop=True, append=False, inplace=True)
#     predicted_data = predicted_data[['trend', 'yhat_lower', 'yhat_upper', 'yhat']]

#     # predicted_data.drop(columns=['ds'])
#     print(predicted_data.index)
#     print(predicted_data.columns)

#     forecast.set_index(forecast['ds'], drop=True, append=False, inplace=True)
#     forecast = forecast[['trend', 'yhat_lower', 'yhat_upper', 'yhat']]
#     forecast.to_csv('FullEthereumData.csv')


# predictCrypto('DOGE')