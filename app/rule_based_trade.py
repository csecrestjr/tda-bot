import pandas as pd
import numpy as np
import requests

def get_stock_data(stock_symbol):
    url = f"https://api.tdameritrade.com/v1/marketdata/{stock_symbol}/pricehistory"
    response = requests.get(url)
    return pd.DataFrame(json.loads(response.text)["candles"])

def moving_average_crossover_strategy(stock_data, short_window=50, long_window=200):
    stock_data["short_ma"] = stock_data["close"].rolling(window=short_window).mean()
    stock_data["long_ma"] = stock_data["close"].rolling(window=long_window).mean()
    stock_data["signal"] = np.where(stock_data["short_ma"] > stock_data["long_ma"], 1, 0)
    stock_data["position"] = stock_data["signal"].diff()
    return stock_data

def rule_based_trading_bot(stock_symbol):
    stock_data = get_stock_data(stock_symbol)
    stock_data = moving_average_crossover_strategy(stock_data)
    account_id = "YOUR_ACCOUNT_ID"
    access_token = "YOUR_ACCESS_TOKEN"
    for i in range(len(stock_data)):
        if stock_data.iloc[i]["position"] == 1:
            buy_stock(stock_symbol, 1)
        elif stock_data.iloc[i]["position"] == -1:
            sell_stock(stock_symbol, 1)
