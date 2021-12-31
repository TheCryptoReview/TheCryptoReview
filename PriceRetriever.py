from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
currency = 'USD'
parameters = {
  'start':'1',
  'limit':'1',
  'convert': currency
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'de88b749-ce4c-420f-bda7-494b636327b7',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  specificData = data['data'][0]['quote'][currency]
  print(specificData['price'], specificData['percent_change_1h'], +specificData['percent_change_24h'], \
        specificData['percent_change_7d'], specificData['percent_change_30d'], specificData['percent_change_60d'], \
        specificData['percent_change_90d'], specificData['market_cap'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

