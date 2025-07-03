import time
import numpy as np
import pandas as pd
import joblib
import ta
from binance.client import Client
import tensorflow as tf 
from datetime import datetime
from dotenv import load_dotenv
import os
load_model = tf.keras.models.load_model
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

# Load model and scaler
model = load_model("btc_lstm_binary_model.h5")
scaler = joblib.load("scaler.pkl")

sequence_length = 30

def fetch_live_data():
    klines = client.get_klines(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1MINUTE, limit=100)
    df = pd.DataFrame(klines, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"
    ])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
    df.set_index("timestamp", inplace=True)
    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

    # Add technical indicators
    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    df["ema_10"] = ta.trend.EMAIndicator(df["close"], window=10).ema_indicator()
    df["ema_50"] = ta.trend.EMAIndicator(df["close"], window=50).ema_indicator()
    macd = ta.trend.MACD(df["close"])
    df["macd"] = macd.macd_diff()
    bollinger = ta.volatility.BollingerBands(df["close"])
    df["bollinger_mavg"] = bollinger.bollinger_mavg()
    df["bollinger_hband"] = bollinger.bollinger_hband()
    df["bollinger_lband"] = bollinger.bollinger_lband()

    df.dropna(inplace=True)
    return df

def predict_live():
    df = fetch_live_data()
    features = df[["open", "high", "low", "volume", "rsi", "ema_10", "ema_50", "macd", "bollinger_mavg", "bollinger_hband", "bollinger_lband"]]
    features_scaled = scaler.transform(features)

    X_input = features_scaled[-sequence_length:]
    X_input = np.expand_dims(X_input, axis=0)  # shape: (1, 30, n_features)

    pred_prob = model.predict(X_input)[0][0]
    prediction = "High" if pred_prob > 0.5 else "Low"

    result = {
        "prediction": float(pred_prob),
        "direction": prediction,
        "current_price": float(df["close"].iloc[-1]),
        "prediction_time": df.index[-1].strftime("%Y-%m-%d %H:%M:%S")
    }

    return result

if __name__ == "__main__":
    print("✅ Starting live prediction loop...")
    while True:
        try:
            result = predict_live()
            print("📈 Live Prediction:", result)
            time.sleep(60)  # wait 1 minute
        except Exception as e:
            print("❌ Error during prediction:", e)
            time.sleep(10)
