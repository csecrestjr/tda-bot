import time
import requests
import json

def get_bond_yield(bond_symbol):
    url = f"https://api.tdameritrade.com/v1/marketdata/{bond_symbol}/yield"
    response = requests.get(url)
    return json.loads(response.text)["yield"]

def buy_bond(bond_symbol, quantity):
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
                    "symbol": bond_symbol,
                    "assetType": "BOND"
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

def sell_bond(bond_symbol, quantity):
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
                    "symbol": bond_symbol,
                    "assetType": "BOND"
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

def yield_trading_bot():
    bond_symbol = "TBILL"
    target_yield = 0.02
    while True:
        current_yield = get_bond_yield(bond_symbol)
        position = get_position(bond_symbol)
        if position is None:
            if current_yield >= target_yield:
                buy_bond(bond_symbol, 1)
        elif current_yield < target_yield:
            sell_bond(bond_symbol, position["quantity"])
        time.sleep(3600)
