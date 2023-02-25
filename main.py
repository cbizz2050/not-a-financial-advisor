import logging
import sys
import time

from market_data import IntradayData, HistoricalData
from pattern_detector import PatternDetector
from pattern_storage import PatternStorage


def main(interval, log_file):
    # Set up logging
    logging.basicConfig(filename=log_file, level=logging.INFO)

    api_key = 'your_api_key_here'
    symbols = ['AAPL', 'GOOG', 'TSLA']
    start_date = '2021-01-01'
    end_date = '2022-02-28'

    for symbol in symbols:
        # Retrieve and preprocess intraday data
        intraday_data = IntradayData(api_key)
        intraday_df = intraday_data.retrieve_data(symbol=symbol)
        intraday_data.preprocess_data()

        # Retrieve and preprocess historical data
        historical_data = HistoricalData(api_key)
        historical_df = historical_data.retrieve_data(symbol=symbol, start_date=start_date, end_date=end_date)
        historical_data.preprocess_data()

        # Run pattern detection on intraday data
        pattern_detector = PatternDetector(intraday_data=intraday_data, historical_data=historical_data)
        detected_patterns = pattern_detector.detect_patterns()

        # Use the dataframes for pattern detection
        intraday_detector = PatternDetector(intraday_data=intraday_df, historical_data=historical_df)
        intraday_patterns = intraday_detector.detect_patterns()
        detected_patterns.extend(intraday_patterns)

        # Store patterns in the database
        storage = PatternStorage()
        for pattern in detected_patterns:
            confidence_rating = pattern.calculate_confidence_rating()
            storage.store_pattern(symbol, pattern.pattern_name, confidence_rating)

        # Wait for next interval
        time.sleep(interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stock pattern detection')
    parser.add_argument('--interval', type=int, default=60,
                        help='Interval in seconds for ingesting and detecting market data')
    parser.add_argument('--log', type=str, default='pattern_detection.log',
                        help='File path for logging output')
    args = parser.parse_args()

    while True:
        try:
            main(args.interval, args.log)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            sys.exit(1)
