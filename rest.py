from config import API_KEY, SECRET_KEY
import requests
import pandas as pd
import numpy as np
import datetime
import json

BASE_URL = 'https://data.alpaca.markets/v2'
STOCKS_URL = f'{BASE_URL}/stocks'
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

def get_bars(symbol, timeframe, start, end):
    bars_url = f'{STOCKS_URL}/{symbol}/bars?timeframe={timeframe}&start={start}&end={end}'
    r = requests.get(bars_url, headers=HEADERS)
    return json.loads(r.content)

bars = get_bars('AAPL', '1Day', '2022-12-26', '2022-12-31')
print(json.dumps(bars, indent=4))