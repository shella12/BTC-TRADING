import pandas as pd
import numpy as np
import joblib
import ta
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
from sklearn.metrics import classification_report

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

# # Scale features
# scaler = StandardScaler()
# features_scaled = scaler.fit_transform(features)
# joblib.dump(scaler, "scaler.pkl")

# # Create sequences (30 timesteps)
# sequence_length = 30
# X, y = [], []
# for i in range(len(features_scaled) - sequence_length):
#     X.append(features_scaled[i:i + sequence_length])
#     y.append(labels.iloc[i + sequence_length])

# X = np.array(X)
# y = np.array(y)

# # Train/test split (preserve time order)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# # Compute class weights for imbalance
# class_weights = class_weight.compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
# class_weights_dict = dict(enumerate(class_weights))
# print("Class weights:", class_weights_dict)

# # Build Binary LSTM model
# model = Sequential([
#     Input(shape=(sequence_length, X.shape[2])),
#     LSTM(64, return_sequences=True),
#     Dropout(0.3),
#     LSTM(64),
#     Dropout(0.3),
#     Dense(32, activation="relu"),
#     Dense(1, activation="sigmoid")
# ])
# model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# # Train model with early stopping
# early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
# model.fit(
#     X_train, y_train,
#     epochs=20,
#     batch_size=64,
#     validation_split=0.1,
#     class_weight=class_weights_dict,
#     callbacks=[early_stop],
#     verbose=1
# )

# # Evaluate model
# loss, accuracy = model.evaluate(X_test, y_test)
# print(f"\u2705 Test Accuracy: {accuracy:.4f}")

# # Save model
# model.save("btc_lstm_binary_model.h5")
# print("\u2705 Binary LSTM model saved as btc_lstm_binary_model.h5")

# # Predictions & Classification Report
# y_pred_probs = model.predict(X_test)
# y_pred = (y_pred_probs > 0.5).astype(int).flatten()
# print("\n\ud83d\udcca Classification Report:")
# print(classification_report(y_test, y_pred, target_names=["Not Up", "Up"]))
