import sqlite3

class PatternDetector:
    def __init__(self, db_name, market_data_ingestor, detection_methods):
        self.db_name = db_name
        self.market_data_ingestor = market_data_ingestor
        self.detection_methods = detection_methods

        # Connect to the SQLite database
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

        # Create the table for this ticker and interval if it doesn't already exist
        table_name = f"{self.market_data_ingestor.ticker}_{self.market_data_ingestor.interval}_detection_events"
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, ticker TEXT, interval TEXT, time INTEGER, confidence REAL)")

        # Get the last detection time from the database
        self.last_detection_time = self.get_last_detection_time()

    def query_database_for_new_detections(self, limit=None, rate_limit_seconds=5):
        table_name = f"{self.ticker}_{self.interval}_detection_events"
        columns = ['id', 'time', 'ticker', 'interval',
                   'detection_method', 'confidence', 'message', 'processed']
        
        query = f"SELECT {', '.join(columns)} FROM {table_name} WHERE processed = 0 ORDER BY time ASC"
        if limit:
            query += f" LIMIT {limit}"

        detections = self.database.query(query)

        if detections:
            for detection in detections:
                # Process the detection event
                self.process_detection_event(detection)

                # Rate limit to avoid overwhelming the database
                time.sleep(rate_limit_seconds)
        else:
            print(f"No new detection events found for {self.ticker} ({self.interval})")

    def write_detection_events_to_database(self, detection_events):
        # Write the detection events to the database
        table_name = f"{self.market_data_ingestor.ticker}_{self.market_data_ingestor.interval}_detection_events"
        for detection_event in detection_events:
            self.c.execute(f"INSERT INTO {table_name} (ticker, interval, time, confidence) VALUES (?, ?, ?, ?)", (detection_event[1], detection_event[2], detection_event[3], detection_event[4]))

        # Commit changes to the database
        self.conn.commit()

    def get_last_detection_time(self):
        # Get the last detection time from the database
        table_name = f"{self.market_data_ingestor.ticker}_{self.market_data_ingestor.interval}_detection_events"
        self.c.execute(f"SELECT MAX(time) FROM {table_name}")
        last_detection_time = self.c.fetchone()[0]

        if last_detection_time is not None:
            return last_detection_time
        else:
            return 0
