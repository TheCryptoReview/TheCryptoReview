from requests import Request, Session
import json
import math

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
  'X-CMC_PRO_API_KEY': '15518944-2395-4c5c-8134-8aca38572fb1',
}

def headingGetter(coinName):
  try:
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

    return name, symbol, specificData['price'], specificData['percent_change_1h'], +specificData['percent_change_24h'], \
          specificData['percent_change_7d'], specificData['percent_change_30d'], specificData['percent_change_60d'], \
          specificData['percent_change_90d'], specificData['market_cap']
  except:
    print("Error")
    return None, None, None, None, None, None, None, None, None, None

def formatLargeNumber(num):
  return "{:,}".format(num)

def roundCrypto(dec):
  if dec < 0:
    if dec == 0:
      return 0
    elif dec >= -0.01:
      return '-$0.01'
    else:
      dec = float(formatLargeNumber(round(dec, 2)))
      return str(dec)[:1]+'$'+str(dec)[1:]
  else:
    if dec == 0:
      return 0
    elif dec <= 0.01:
      return '$0.01'
    else:
      return '$' + str(formatLargeNumber(round(dec, 2)))
  return 0

def roundCryptoWithoutDollar(dec):
  if dec < 0:
    if dec == 0:
      return '0%'
    elif dec >= -0.01:
      return '-0.01%'
    else:
      dec = float(formatLargeNumber(round(dec, 2)))
      return str(dec)[:1]+str(dec)[1:]+'%'
  else:
    if dec == 0:
      return '0%'
    elif dec <= 0.01:
      return '0.01%'
    else:
      return str(formatLargeNumber(round(dec, 2))) + '%'
  return 0

global url2
url2 = 'https://api.alternative.me/fng/'
def priceGreed():
  session2 = Session()
  response2 = session2.get(url2)
  data2 = json.loads(response2.text)
  return data2["data"][0]["value"],data2["data"][0]["value_classification"]


  
