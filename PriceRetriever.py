from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

global url
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
global parameters
parameters = {
  'start':'1',
  'limit':'5000',
  'convert': 'USD'
}
global headers
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'de88b749-ce4c-420f-bda7-494b636327b7',
}

def headingGetter(coinName):
  session = Session()
  session.headers.update(headers)

  response = session.get(url, params=parameters)
  data = json.loads(response.text)

  for i in range(5000):
    name = data['data'][i]['name']
    symbol = data['data'][i]['symbol']
    if coinName.title() in name or coinName in name or coinName.upper() in symbol:
      finalIndex = i
      break

  specificData = data['data'][finalIndex]['quote']['USD']

  return symbol, specificData['price'], specificData['percent_change_1h'], +specificData['percent_change_24h'], \
        specificData['percent_change_7d'], specificData['percent_change_30d'], specificData['percent_change_60d'], \
        specificData['percent_change_90d'], specificData['market_cap']



