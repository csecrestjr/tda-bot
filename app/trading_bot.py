import time
import requests
import json

def get_stock_price(stock_symbol):
    url = f"https://api.tdameritrade.com/v1/marketdata/{stock_symbol}/price"
    response = requests.get(url)
    return json.loads(response.text)["lastPrice"]

def buy_stock(stock_symbol, quantity):
    url = f"https://api.tdameritrade.com/v1/accounts/{account_id}/orders"
    payload = {
        "orderType": "MARKET",
        "session": "NORMAL",
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegCollection": [
            {
                "instruction": "BUY",
                "quantity": quantity,
                "instrument": {
                    "symbol": stock_symbol,
                    "assetType": "EQUITY"
                }
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return json.loads(response.text)

def sell_stock(stock_symbol, quantity):
    url = f"https://api.tdameritrade.com/v1/accounts/{account_id}/orders"
    payload = {
        "orderType": "MARKET",
        "session": "NORMAL",
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegCollection": [
            {
                "instruction": "SELL",
                "quantity": quantity,
                "instrument": {
                    "symbol": stock_symbol,
                    "assetType": "EQUITY"
                }
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return json.loads(response.text)

def moderate_risk_trading_bot():
    stock_symbol = "AAPL"
    target_profit_percentage = 0.03
    max_loss_percentage = 0.01
    while True:
        current_price = get_stock_price(stock_symbol)
        position = get_position(stock_symbol)
        if position is None:
            buy_stock(stock_symbol, 1)
            position = {"cost": current_price, "quantity": 1}
        elif (current_price - position["cost"]) / position["cost"] >= target_profit_percentage:
            sell_stock(stock_sy
