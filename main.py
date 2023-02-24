from datetime import datetime, timedelta
from typing import List

import matplotlib.pyplot as plt

from market_data_ingestor import MarketDataIngestor
from pattern_detector import Method1Detector
from database import Database
from detection_plotter import DetectionEventPlotter


def main(interval_minutes: int, symbols: List[str], plot_window_minutes: int) -> None:
    # Instantiate a database object
    database = Database()

    # Instantiate a market data ingestor object for each symbol
    ingestors = [MarketDataIngestor(database, symbol, interval_minutes) for symbol in symbols]

    # Instantiate one or more pattern detectors
    detectors = [Method1Detector(database) for _ in range(3)]

    # Instantiate a detection event plotter
    plotter = DetectionEventPlotter(database, symbols, plot_window_minutes)

    # Run the main loop
    while True:
        # Fetch the latest market data for each symbol
        market_data = [ingestor.fetch_latest_market_data() for ingestor in ingestors]

        # Pass the market data to each pattern detector
        for detector in detectors:
            for data in market_data:
                detector.detect(data)

        # Plot any new detection events
        plotter.plot_new_events()

        # Sleep for some period of time
        time.sleep(interval_minutes * 60)
