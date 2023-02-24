import yfinance as yf
import pandas as pd
import sqlite3
from typing import List

class MarketDataIngestor:
    def __init__(self, symbols: List[str], start_date: str, end_date: str):
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date
        self.cache = {}
        self.connection = sqlite3.connect('market_data.db')
        self.cursor = self.connection.cursor()

    def download_data(self, symbol):
        df = yf.download(symbol, start=self.start_date, end=self.end_date)
        df.reset_index(inplace=True)
        df.rename(columns={'Adj Close': 'AdjClose'}, inplace=True)
        return df

    def ingest(self, symbol):
        if symbol in self.cache:
            return self.cache[symbol]
        
        # Check if data already exists in the database
        self.cursor.execute('SELECT * FROM market_data WHERE Symbol=?', (symbol,))
        if self.cursor.fetchone():
            print(f"Data for {symbol} already exists in the database")
            return None

        # Download and clean market data
        data = self.download_data(symbol)
        if data is None:
            return None
        
        # Insert data into the database
        data.to_sql('market_data', self.connection, if_exists='append')
        self.cache[symbol] = data
        return data

    def ingest_all(self):
        for symbol in self.symbols:
            self.ingest(symbol)
