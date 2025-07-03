# from binance.client import Client
# import pandas as pd
# import time
# import os
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("BINANCE_API_KEY")
# api_secret = os.getenv("BINANCE_API_SECRET")

# client = Client(api_key, api_secret)

# # Fetch last 1,000 minutes of 1-minute interval data
# klines = client.get_klines(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1MINUTE, limit=200000)

# # Parse to DataFrame
# df = pd.DataFrame(klines, columns=[
#     "timestamp", "open", "high", "low", "close", "volume",
#     "close_time", "quote_asset_volume", "number_of_trades",
#     "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
# ])

# df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
# df.set_index("timestamp", inplace=True)

# df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

# # Save it
# df.to_csv("BTCUSDT_1m.csv")
# print("✅ Data saved as BTCUSDT_1m.csv")
from binance.client import Client
import pandas as pd
import time
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

symbol = "BTCUSDT"
interval = Client.KLINE_INTERVAL_1MINUTE
limit = 1000  # max allowed
total_minutes = 200_000  # target
batch_count = total_minutes // limit

print(f"📦 Downloading ~{total_minutes} minutes of 1m data (~{batch_count} requests)...")

all_klines = []
start_time = int((datetime.now() - timedelta(minutes=total_minutes)).timestamp() * 1000)

for _ in range(batch_count):
    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit,
        startTime=start_time
    )
    if not klines:
        break
    all_klines.extend(klines)
    start_time = klines[-1][0] + 60_000  # next minute

    time.sleep(0.2)  # avoid rate limit

# To DataFrame
df = pd.DataFrame(all_klines, columns=[
    "timestamp", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "number_of_trades",
    "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
])

df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
df.set_index("timestamp", inplace=True)
df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

df.to_csv("BTCUSDT_1m.csv")
print(f"✅ Saved {len(df)} rows to BTCUSDT_1m.csv")
