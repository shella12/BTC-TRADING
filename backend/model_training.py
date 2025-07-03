import pandas as pd
import ta
import tensorflow as tf

Sequential = tf.keras.models.Sequential
LSTM = tf.keras.layers.LSTM
Dense = tf.keras.layers.Dense
Dropout = tf.keras.layers.Dropout
EarlyStopping = tf.keras.callbacks.EarlyStopping
Input = tf.keras.layers.Input

# Load dataset
df = pd.read_csv("BTCUSDT_1m.csv", index_col="timestamp", parse_dates=True)
print(df)
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

# Binary target: 1 = Up, 0 = Not Up (Down or Neutral)
threshold = 0.001
df["target"] = (df["close"].shift(-10) - df["close"]) / df["close"]
df["target"] = df["target"].apply(lambda x: 1 if x > threshold else 0)

# Drop rows with NaNs (after ta indicators and shift)
df.dropna(inplace=True)

# Select features (exclude 'close' to avoid target leakage)
features = df[["open", "high", "low", "volume", "rsi", "ema_10", "ema_50", "macd", "bollinger_mavg", "bollinger_hband", "bollinger_lband"]]
labels = df["target"]
