import asyncio
import aiohttp
import cachetools
import mysql.connector
from datetime import datetime, timedelta
from asyncio.locks import Lock

class MarketDataIngestor:
    def __init__(self, ticker, api_key, cache_size=1000, cache_ttl=3600):
        self.ticker = ticker
        self.api_key = api_key
        self.market_data = None
        self.cache = cachetools.TTLCache(maxsize=cache_size, ttl=cache_ttl)
        self.lock = Lock()

    async def ingest_market_data(self):
        cache_key = "{}_{}".format(self.ticker, datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S"))
        cached_data = self.cache.get(cache_key)
        if cached_data is not None:
            self.market_data = cached_data
            return

        async with aiohttp.ClientSession() as session:
            url = "https://marketdata.websol.barchart.com/getHistory.json?apikey={}&symbol={}&type=hour&startDate=20220101000000".format(self.api_key, self.ticker)
            for attempt in range(3):
                try:
                    async with session.get(url) as response:
                        json_data = await response.json()
                        self.market_data = json_data['results']
                        self.cache[cache_key] = self.market_data
                        return
                except aiohttp.ClientError:
                    await asyncio.sleep(1)
                    continue
            raise Exception("Failed to ingest market data after 3 attempts")

    async def clean_market_data(self):
        market_data = self.market_data
        for i in range(len(market_data)):
            if market_data[i]['high'] is None:
                market_data[i]['high'] = market_data[i-1]['close']
            if market_data[i]['low'] is None:
                market_data[i]['low'] = market_data[i-1]['close']
            if market_data[i]['close'] is None:
                market_data[i]['close'] = market_data[i]['open']
            if market_data[i]['volume'] is None:
                market_data[i]['volume'] = 0
        self.market_data = market_data

    async def append_market_data(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="market_data_db"
        )
        async with mydb:
            cursor = mydb.cursor()
            table_name = "{}_table".format(self.ticker.lower())
            query = "CREATE TABLE IF NOT EXISTS {} (time DATETIME PRIMARY KEY, high FLOAT, low FLOAT, close FLOAT, volume FLOAT)".format(table_name)
            await cursor.execute(query)
            for i in range(len(self.market_data)):
                time = datetime.fromtimestamp(self.market_data[i]['timestamp'])
                high = self.market_data[i]['high']
                low = self.market_data[i]['low']
                close = self.market_data[i]['close']
                volume = self.market_data[i]['volume']
                query = "INSERT INTO {} (time, high, low, close, volume) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE high=VALUES(high), low=VALUES(low), close=VALUES(close), volume=VALUES(volume)".format(table_name)
                values = (time, high, low, close, volume)
                await cursor.execute(query, values)
            await mydb.commit()

    async def run_all(self):
        tasks = [asyncio.create_task(self.ingest_market_data()),
                 asyncio.create_task(self.clean_market_data()),
                 asyncio.create_task(self.append_market_data())]
        await asyncio.gather(*tasks)
