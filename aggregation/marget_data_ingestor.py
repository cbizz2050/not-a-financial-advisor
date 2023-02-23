class MarketDataIngestor:
    def __init__(self, config):
        self.config = config
        self.database = Database(config['database'])
        self.ticker = config['ticker']
        self.interval = config['interval']
        self.endpoint = config['endpoint']

    def ingest_market_data(self):
        # Ingest market data for the specified ticker, interval, and endpoint
        market_data = self.read_market_data()

        # Clean the market data for use in the detection methods
        cleaned_data = self.clean_market_data(market_data)

        return cleaned_data

    def read_market_data(self):
        # Read market data for the specified ticker, interval, and endpoint from the API
        api_params = {'ticker': self.ticker, 'interval': self.interval, 'endpoint': self.endpoint}
        api_data = API.get_market_data(api_params)
        market_data = api_data['data']

        return market_data

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