import argparse
import logging
import sys

from market_data_ingestor import MarketDataIngestor
from pattern_detector import PatternDetector
from pattern_storage import PatternStorage


def main(interval, log_file):
    # Set up logging
    logging.basicConfig(filename=log_file, level=logging.INFO)

    # Instantiate objects
    ingestor = MarketDataIngestor()
    detector = PatternDetector()
    storage = PatternStorage()

    while True:
        try:
            # Ingest market data
            ingestor.ingest()

            # Detect patterns
            detected_patterns = detector.detect_patterns()

            # Store patterns
            storage.store_pattern(detected_patterns)
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            sys.exit(1)

        # Wait for next interval
        time.sleep(interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stock pattern detection')
    parser.add_argument('--interval', type=int, default=60,
                        help='Interval in seconds for ingesting and detecting market data')
    parser.add_argument('--log', type=str, default='pattern_detection.log',
                        help='File path for logging output')
    args = parser.parse_args()

    main(args.interval, args.log)
