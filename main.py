from database import Database
from market_data_ingestor import MarketDataIngestor
from pattern_detector import PatternDetector
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Define the tickers and intervals to monitor
tickers = ['AAPL', 'MSFT']
intervals = ['1h', '1d']

# Create the database
database = Database(host='localhost', user='root', password='password', db_name='market_data_db')

# Create MarketDataIngestor and PatternDetector objects for each ticker and interval
ingestors = [MarketDataIngestor(database, ticker, interval) for ticker in tickers for interval in intervals]
detectors = [PatternDetector(database, ingestor, detection_methods=[Method1Detector(), Method2Detector()]) for ingestor in ingestors]

# Define the function to be called on each animation frame
def update(frame):
    # Query the database for new detection events and plot them
    for detector in detectors:
        detection_events = detector.query_database_for_new_detections()
        if detection_events:
            for detection_event in detection_events:
                plt.plot(detection_event['time'], detection_event['confidence'], 'o', label=detection_event['ticker'])
            plt.legend()
    plt.show()

# Set up the animation
ani = FuncAnimation(plt.gcf(), update, interval=10000)

# Display the plot
plt.show()
