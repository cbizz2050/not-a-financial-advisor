import yfinance as yf
from .pattern import Pattern
from .database import Database


class PatternDetector:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = yf.download(symbol, start_date, end_date)
        self.patterns = []
        self.db = Database()

    def detect_patterns(self):
        self.patterns = []
        for name, pattern in Pattern.get_all_patterns().items():
            result = pattern.detect(self.data)
            if result is not None:
                self.patterns.append(result)
                self.db.write_detection_event_to_database(result, name)

    def get_patterns(self):
        return self.patterns
