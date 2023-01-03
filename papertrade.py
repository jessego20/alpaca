from config import API_KEY, SECRET_KEY
import requests
import pandas as pd
import numpy as np
import datetime
import json

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = f'{BASE_URL}/v2/account'
ORDERS_URL = f'{BASE_URL}/v2/orders'
STOCKS_URL = f'{BASE_URL}/v2/stocks'
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(ORDERS_URL, headers=HEADERS, json=data)
    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)

# print(get_account())
# print(create_order('AAPL', 100, 'buy', 'market', 'day'))
# print(create_order('MSFT', 100, 'buy', 'market', 'day'))
# print(create_order('TSLA', 100, 'buy', 'market', 'day'))
# print(get_orders())