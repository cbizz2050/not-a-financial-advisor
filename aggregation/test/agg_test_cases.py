import unittest
from market_data_ingestor import MarketDataIngestor

class TestMarketDataIngestor(unittest.TestCase):
    def test_ingest(self):
        # Create an instance of the MarketDataIngestor class
        ingestor = MarketDataIngestor()
        # Call the ingest method
        result = ingestor.ingest()
        # Check that the method returns a boolean value
        self.assertIsInstance(result, bool)
