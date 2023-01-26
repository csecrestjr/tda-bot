# Basic trading bot used with TD Ameritrade API and will continue to update. 

## Here are the general steps you can take to use the trading bot code I generated with TD Ameritrade's developer app:

1. Create an account on TD Ameritrade's website.
2. Create a developer app on TD Ameritrade's developer portal. You will need to provide a name and description for your app, as well as specify the permissions it will require.
3. Obtain an access token for your app by following the instructions on the developer portal.
4. Replace the placeholder values in the trading bot code with your own account ID and access token.
5. Install the required libraries like requests, pandas, numpy, selenium and webdriver-manager.
6. Run the code and make sure it is working correctly, you can try to run it locally on your computer first and then check if the trades are being executed correctly on TD Ameritrade's website.
7. Once you have confirmed that the bot is working correctly, you can schedule it to run automatically at specific intervals.

<b><i><u>NOTE:</b></i></u> Please note that the use of selenium and webdriver-manager to automate trading is against the terms and conditions of most of the trading platform and it is illegal, it is recommended not to use it. Additionally, it is important to note that the performance of a trading bot is highly dependent on market conditions, and the use of any trading strategy or bot carries a risk of financial loss. Therefore, It is recommended to conduct your own research and testing before deploying any bot into live trading. It is important to consult with a financial advisor before making any investment decisions. </br></br>

TD Ameritrade API setup link to create API key + access token: https://developer.tdameritrade.com/content/getting-started

### Replace the following key/value pairs with your API key + access token values:

<b><i>"apiKey": "enter your tdameritrade api key",</b></i></br>
<b><i>"accessToken": "enter your tdameritrade access token"</b></i>

If no API key or access token is provided, then the request will be unable to retrieve data from TD Ameritrade and return a 500 status code.  In this case, the program will use the default dummy/test data (TSLA-10day-5min.json) already included for mock test.</br></br>
Run the program by running the main.py file and user will be prompted to enter a stock ticker symbol, then the following menu will appear for trade strategy selection (below).  Upon user selection, then the calculated EMA/RSI indicator values will appear + simulated trade transaction, followed by the net gain/loss.</br>

<pre>
+-----------------------------------------------+
|               Trading Strategies              |
+-----------------------------------------------+
|   1. Baseline - trade on RSI=50 level         |
|   2. EMA only - trade w/ EMA indicator        |
|   3. RSI only - trade based on last RSI level |
|   4. EMA + RSI - trade w/ EMA + RSI level     |
+-----------------------------------------------+
|   select a trading strategy (1,2,3,4):        |
+-----------------------------------------------+
</pre>
