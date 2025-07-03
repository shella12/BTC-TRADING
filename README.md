# BTCUSDT High/Low Price Classifier

**Predict Bitcoin Price Direction – Real-Time Binary Classification with Confidence Scores**

---

## Project Overview

This project is a real-time AI classifier/predictor that predicts whether BTCUSDT will go "high" or "low" in the next 10 minutes, based on 1-minute candlestick data. It uses features such as EMA30, EMA50, MACD, RSI, Bollinger Bands, and volume. The model outputs both the predicted class and its confidence (probability), helping traders make quick, data-driven decisions.

---

## Features

- **Real-Time Inference:** Evaluates BTCUSDT price action every minute and makes a prediction for the next 10 minutes.
- **Clear Prediction:** Outputs “HIGH” or “LOW” plus the confidence percentage for each call.
- **Feature Engineering:** Uses technical indicators (EMA30, EMA50, MACD, Bollinger Bands, volume) as model inputs.
- **Practical Performance:** Shows accuracy and confidence stats for recent predictions.
- **Multiple Models Tested:** Explored RandomForestClassifier and XGBoost during training, but currently focuses on tensorflow for time series problem(best performing model).
- **Easy to Run:** Start real-time predictions with a single command.

---

## Tech Stack

- **Python 3**
- **Binance API** (real-time candlestick data)
- **Pandas, NumPy** (data processing)
- **Scikit-learn, XGBoost, TensorFlow** (tensorflow model – best performer used)
- **TA-Lib** (technical indicators)


---

## How It Works

1. **Data Collection:** Fetches 1-minute OHLCV data for BTCUSDT from Binance.
2. **Feature Engineering:** Calculates RSI, EMA30, EMA50, MACD, Bollinger Bands, and volume for each candle.
3. **Prediction:** For every new candle, predicts if price will go “HIGH” or “LOW” over the next 10 minutes, with accuracy/confidence score.
4. **Evaluation:** Prints accuracy and recent prediction confidence during live operation.

---

## Sample Output
```
✅ Starting live prediction loop...
2025-07-03 08:07:04.810999: I tensorflow/core/grappler/optimizers/custom_graph_optimizer_registry.cc:117] Plugin optimizer for device_type GPU is enabled.
1/1 ━━━━━━━━━━━━━━━━━━━━ 1s 937ms/step
📈 Live Prediction: {'prediction': 0.3488968014717102, 'direction': 'Low', 'current_price': 108720.9, 'prediction_time': '2025-07-03 03:07:00'}
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step
📈 Live Prediction: {'prediction': 0.34470993280410767, 'direction': 'Low', 'current_price': 108716.22, 'prediction_time': '2025-07-03 03:08:00'}
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 28ms/step
📈 Live Prediction: {'prediction': 0.336466908454895, 'direction': 'Low', 'current_price': 108716.22, 'prediction_time': '2025-07-03 03:09:00'}
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step
📈 Live Prediction: {'prediction': 0.3231099843978882, 'direction': 'Low', 'current_price': 108719.99, 'prediction_time': '2025-07-03 03:10:00'}
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step
```

---

## Getting Started

### Prerequisites

- Python 3.x
- Binance account with API key
- Install dependencies: `pip install -r requirements.txt`

### Installation

```bash
git clone https://github.com/shella12/BTC-TRADING.git
cd BTC-TRADING
pip install -r requirements.txt
```

### Configuration
 - Add your Binance API credentials to `.env` file and set as environment variables. `.env` should have the following:

 ```
BINANCE_API_KEY= your_binance_api_key
BINANCE_API_SECRET= your_binance_api_secret
 ```

### Running the Model
```
cd backend
python realtime_predictor.py
```

### Customization
 - You can tweak feature engineering in the script to add/remove indicators.

 - To experiment with different classifiers, see the included `model_training.py` script. You can tweak the features and retrain the model using the script

### Future Improvements
 - Web dashboard for live monitoring

 - Integration with trading bots for automated signals

 - More feature and model experimentation

### Why I Built This

To gain hands-on experience in real-time AI for trading, while solving a personal challenge of predicting BTC price moves quickly and reliably using only widely-known technical indicators.

### License
MIT (Feel free to use and extend!)

### Contact
  - [linkedIn](https://www.linkedin.com/in/-ayesha-arshad/)
  - [github](https://github.com/shella12/)
  - [portfolio](https://ayesha-arshad-portfolio-2f0349.netlify.app/)
  - [email](ayeshaarshad4567@gmail.com)
