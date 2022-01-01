import pandas_datareader as web
import datetime as dt
from prophet import Prophet
import matplotlib.pyplot as plt

# Retrieve Data
crypto_currency = 'BTC'
against_currency = 'USD'

start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()

df = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)
df['ds'] = df.index
df['y'] = df['Close']

print(df.head(2))

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=180)
future.tail(2)

forecast= m.predict(future)
forecast.tail(2)

plt.figure(figsize=(15,5))
plt.title(crypto_currency + against_currency + ' price prediction')
plt.plot(df['ds'], df['Close'])
plt.plot(forecast['ds'], forecast['yhat'])
plt.plot(forecast['ds'], forecast['yhat_lower'], alpha=0.1, color='blue')
plt.plot(forecast['ds'], forecast['yhat_upper'], alpha=0.1, color='blue')
plt.legend('upper right')

plt.fill_between(forecast['ds'], forecast['yhat_upper'], forecast['yhat_lower'], alpha=0.1)
#plt.plot(forecast['ds'], forecast['trend'])

plt.show()
