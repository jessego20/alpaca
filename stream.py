from config import API_KEY, SECRET_KEY
import requests
import pandas as pd
import numpy as np
import datetime
import json
import websocket

def on_open(ws):
    print('opened')

    auth_message = {
        'action': 'auth',
        'key': API_KEY,
        'secret': SECRET_KEY
    }
    ws.send(json.dumps(auth_message))

    data_message = {
        'action': 'subscribe',
        'bars': ['AAPL']
    }
    ws.send(json.dumps(data_message))

def on_message(ws, message):
    print('received a message:')
    print(json.dumps(json.loads(message), indent=4))

def on_close(ws):
    print('closed connection')

socket = 'wss://stream.data.alpaca.markets/v2/iex'

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()