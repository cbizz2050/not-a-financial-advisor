import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

# from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.historical import StockHistoricalDataClient

import ta_indicators


class MarketData:
    # Not sure about the bst way to include the secret key here
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key  # Not sure if this will be a problem for using an api with no secret key
        self.interval = None
        self.symbol = None
        self.df = None  # is the ohlcv per timestamp dataframe
        self.tech_indicators = None 
        self.candle_patterns = None
        # Can add mor ta_lib indicators
        self.timestamps = None
        self.start_time = None  # Think having a good way to mave around differnet time types here would be good
        self.end_time = None
        self.processed_data = None
        self.processed_data = None

    def retrieve_data_alpaca(self, symbol, interval):
        API_KEY = "AK1OJLCW8QD9NMWX0HRR"
        SECRET_KEY = "e5MKaGLVjQevaeTUtdYgWFwzf8ibIliaGfHfss87"

        self.symbol = symbol
        self.interval = interval
        self.symbol = symbol

        stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

        # The working test times 
        # start_time = datetime(2015, 2, 1, 15, 16, 17, 345, tzinfo=timezone.utc)
        # end_time = datetime(2023, 2, 2, 15, 16, 17, 345, tzinfo=timezone.utc)

        # LIst of timeframes that can be used in the request parameters
        # Day = <alpaca.data.timeframe.TimeFrame object>
        # Hour = <alpaca.data.timeframe.TimeFrame object>
        # Minute = <alpaca.data.timeframe.TimeFrame object>
        # Month = <alpaca.data.timeframe.TimeFrame object>
        # Week = <alpaca.data.timeframe.TimeFrame object>

        request_params = StockBarsRequest(
                                symbol_or_symbols=self.symbol, # Also can pass a list of tickers here
                                timeframe=TimeFrame.Minute,
                                start=self.start_time,  # Needs data time object (Not sure about Timezone stuff for data)
                                end=self.end_time
                                )

        # Retrieve daily bars for Bitcoin in a DataFrame and printing it
        stock_bars = stock_client.get_stock_bars(request_params)

        # Convert to dataframe
        self.df = stock_bars.df
        return self.df
 

    def trading_analysis(self):
        # Guessing that this will all be different dataframes to add together for one big one
        self.tech_indicators = ta_indicators.ta_indicators(self.df)
        self.candle_patterns = ta_indicators.candle_pattern_recognition(self.df)


        # might need this later to drop NA values after doing tech analysis
        # Drop any rows with NaN values
        self.df = self.df.dropna()


    # WOuld have to update this for all of the ta_indicators
    def plot_processed_data(self):
        fig, ax = plt.subplots(figsize=(15, 8))
        ax.plot(self.timestamps, self.processed_data[:, 0], label='Rolling Moving Average')
        ax.plot(self.timestamps, self.processed_data[:, 2], label='Upper Bollinger Band')
        ax.plot(self.timestamps, self.processed_data[:, 3], label='Lower Bollinger Band')
        ax.plot(self.timestamps, self.df['close'], label='Market Price')
        ax2 = ax.twinx()
        ax2.plot(self.timestamps, self.processed_data[:, 1], color='yellow', label='Relative Strength Index')
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Price')
        ax2.set_ylabel('RSI')
        ax.set_title(f'{self.symbol} {self.interval} Market Data')
        ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        plt.show()


