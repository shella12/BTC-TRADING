from binance.client import Client

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")
client = Client(api_key, api_secret)

def place_order(signal):
    if signal == 1:
        order = client.futures_create_order(
            symbol="BTCUSDT", side="BUY", type="MARKET", quantity=0.001)
    else:
        order = client.futures_create_order(
            symbol="BTCUSDT", side="SELL", type="MARKET", quantity=0.001)
    print(order)
