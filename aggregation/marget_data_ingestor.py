import sqlite3
import requests
import json

class MarketDataIngestor:
import sqlite3
import pandas as pd

class MarketDataIngestor:
    def __init__(self, db_name, ticker, interval, start_date=None):
        self.db_name = db_name
        self.ticker = ticker
        self.interval = interval

        # Connect to the SQLite database
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

        # Create the table for this ticker and interval if it doesn't already exist
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {self.ticker}_{self.interval} (time INTEGER PRIMARY KEY, high REAL, low REAL, open REAL, close REAL, volume REAL)")

        # Set the start date for data ingestion
        if start_date is not None:
            self.start_date = pd.to_datetime(start_date)
        else:
            self.start_date = pd.to_datetime("2000-01-01")

    def download_data(self):
        # Download market data from Alpha Vantage API (Recommended by gpt)
        api_key = 'YOUR_API_KEY_HERE'
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{self.interval.upper()}&symbol={self.ticker}&apikey={api_key}'
        response = requests.get(url)

        # Parse the JSON response
        data = json.loads(response.text)[f'Time Series ({self.interval})']

        # Insert each data point into the database
        for time, values in data.items():
            self.c.execute(f"INSERT OR REPLACE INTO {self.ticker}_{self.interval} (time, high, low, open, close, volume) VALUES (?, ?, ?, ?, ?, ?)", (time, values['2. high'], values['3. low'], values['1. open'], values['4. close'], values['5. volume']))

        # Commit changes to the database
        self.conn.commit()

    def clean_market_data(self, market_data):
        # Clean the market data by setting unassigned fields to standard values
        cleaned_data = []
        for data_point in market_data:
            # Clean the data point by setting unassigned fields to standard values
            cleaned_data_point = {
                'time': data_point.get('time', 0),
                'open': data_point.get('open', 0),
                'high': data_point.get('high', 0),
                'low': data_point.get('low', 0),
                'close': data_point.get('close', 0),
                'volume': data_point.get('volume', 0)
            }
            cleaned_data.append(cleaned_data_point)

        return cleaned_data