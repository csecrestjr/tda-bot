import pandas as pd
import requests

# Define the endpoint URL
url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(symbol)

# Define the query parameters
params = {'apikey': 'YOUR_API_KEY',
          'periodType': 'day',
          'frequencyType': 'minute',
          'frequency': '1',
          'startDate': '2021-01-01',
          'endDate': '2021-01-31'}

# Send the GET request to the endpoint
response = requests.get(url, params=params)

# Print the response
print(response.json())

# Load sample data into a pandas DataFrame
data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
        'Open': [100.00, 100.25, 101.50, 101.75, 101.25],
        'High': [101.00, 102.00, 102.50, 102.00, 102.50],
        'Low': [99.50, 100.00, 100.75, 100.50, 100.75],
        'Close': [100.25, 101.50, 101.75, 101.25, 102.00],
        'Volume': [1000, 2000, 1500, 1700, 2100]}
df = pd.DataFrame(data)

# Add columns for moving averages
df['SMA_10'] = df['Close'].rolling(window=10).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()

# Initialize a variable to track the current position (1 = long, -1 = short)
position = 0

# Iterate through the DataFrame and check for moving average crossovers
for i in range(len(df)):
    if i < 50:
        continue
    if df.at[i, 'SMA_10'] > df.at[i, 'SMA_50'] and position <= 0:
        # Buy signal - go long
        position = 1
        print('Buy at', df.at[i, 'Close'])
    elif df.at[i, 'SMA_10'] < df.at[i, 'SMA_50'] and position >= 0:
        # Sell signal - go short
        position = -1
        print('Sell at', df.at[i, 'Close'])

