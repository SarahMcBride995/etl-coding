#Sample Requests Project
#Sarah McBride
#July 30, 2022




#####GET CURRENCY INFORMATION ######
#to get currency information
import requests
import pandas as pd

#get full name form currency code
def get_currency_name(code):
    api_key = 'YOUR API KEY'
    url = 'https://developers.coinbase.com/api/v2#data-endpoints'
    name = requests.get(url).json()
    curr_name = name['name']
    return str(curr_name)
    



# request specific currency dat aoutput at csv
from datetime import datetime
def get_currency_info(code):
    api_key = 'YOUR API KEY'
    url = 'https://developers.coinbase.com/api/v2#data-endpoints'
    curr_data = requests.get(url).json()
    curr_info = pd.DataFrame(curr_data)
    return curr_info

curr_info.tocsv('\code' + '-exchange_output' + '\timestamp.csv')

#print data


### GET BTC INFO ###
#to get latest crypto currency price
#BTC e.g.
import requests
import pandas as pd

def get_crypto_price(symbol):
    api_key = 'YOUR API KEY'
    api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={api_key}'
    raw = requests.get(api_url).json()
    price = raw['price']
    return float(price)

btc = get_crypto_price('btcusd')
print('Price of 1 Bitcoin: {} USD'.format(btc))


def get_btc(value):
    api_key = 'YOUR API KEY'
    api_url = f'https://cloud.iexapis.com/stable/crypto/btc/price?token={api_key}'
    btc_data = requests.get(url).json()
    price = btc_data['price'] #current btc price
    float(value)
    btc_value = value/price
    return btc_value
