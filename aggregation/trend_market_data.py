import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

class TrendMarketData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.interval = None
        self.symbol = None
        self.raw_data = None
        self.df = None
        self.timestamps = None
        self.processed_data = None

    def retrieve_data(self, symbol, interval='1min'):
        self.interval = interval
        self.symbol = symbol
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={self.api_key}'
        response = requests.get(url)
        self.raw_data = response.json()['Time Series ({})'.format(interval)]
        self.df = pd.DataFrame(self.raw_data).transpose()
        self.df = self.df.astype(float)
        self.df.index = pd.to_datetime(self.df.index)
        return self.df

    def preprocess_data(self):
        # Search for a column name containing "close" using a regular expression
        close_col = self.df.columns[self.df.columns.str.contains(r'(?i)close')].tolist()
        if not close_col:
            raise ValueError("The 'close' column is not present in the dataframe.")

        # Rename the "close" column
        self.df = self.df.rename(columns={close_col[0]: 'close'})

        # Fill missing values with the previous value
        self.df = self.df.fillna(method='ffill')

        # Drop any rows with NaN values
        self.df = self.df.dropna()

        # Add a rolling moving average
        rolling_window = 10
        self.df['rolling_ma'] = self.df['close'].rolling(window=rolling_window).mean()

        # Add the relative strength index
        period = 14
        delta = self.df['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        self.df['rsi'] = rsi

        # Add the bollinger bands
        std_multiplier = 2
        rolling_mean = self.df['close'].rolling(window=rolling_window).mean()
        rolling_std = self.df['close'].rolling(window=rolling_window).std()
        self.df['upper_band'] = rolling_mean + (rolling_std * std_multiplier)
        self.df['lower_band'] = rolling_mean - (rolling_std * std_multiplier)

        # Save the processed data as a numpy array
        self.processed_data = self.df[['rolling_ma', 'rsi', 'upper_band', 'lower_band']].values
        self.timestamps = self.df.index.values

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


