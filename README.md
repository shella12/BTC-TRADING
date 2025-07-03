# BTCUSDT High/Low Price Prediction Model

**AI-Powered Classification of Bitcoin Price Movements**

---

## Project Overview

This project predicts whether the price of BTCUSDT (Bitcoin/USDT pair) will go “high” or “low” in the near future using machine learning. Historical price data is collected from the Binance API and multiple classification algorithms—including TensorFlow and XGBoost—are applied. The goal: help traders anticipate price swings and inform better trading decisions.

---

## Features

- **Automated Data Collection:** Fetches historical BTCUSDT price data from Binance using their official API.
- **Feature Engineering:** Generates features from price history and technical indicators (e.g., moving averages, RSI, Bollinger Bands).
- **Multiple Classifier Models:** Trains and compares TensorFlow neural networks and XGBoost classifiers.
- **Performance Evaluation:** Measures accuracy, precision, recall, and F1-score to benchmark models.
- **Easy Experimentation:** Jupyter notebook included for quick tweaking and reproducibility.

---

## Tech Stack

- **Python 3**
- **Binance API** (data collection)
- **Pandas, NumPy** (data processing)
- **TensorFlow, XGBoost** (classification models)
- **Scikit-learn** (metrics and preprocessing)
- **Matplotlib** (visualizations)

---

## How It Works

1. **Data Acquisition:** Pulls historical OHLCV (open, high, low, close, volume) data from Binance.
2. **Data Preprocessing:** Cleans data and creates input features, including technical indicators.
3. **Label Generation:** Classifies each row as “high” (price is likely to go up) or “low” (likely to go down) based on future movement.
4. **Model Training:** Fits and tunes TensorFlow and XGBoost classifier models.
5. **Evaluation:** Assesses model performance with cross-validation and multiple metrics.
6. **Prediction:** Outputs probabilities for high/low movement for the next time interval.

---

## Sample Results

*Include a sample confusion matrix or accuracy score screenshot here if you have one.*

---

## Getting Started

### Prerequisites

- Python 3.x installed
- Binance account with API key
- Jupyter Notebook (recommended for running and editing code)

### Installation

```bash
git clone https://github.com/shella12/BTC-TRADING.git
cd BTC-TRADING
pip install -r requirements.txt
