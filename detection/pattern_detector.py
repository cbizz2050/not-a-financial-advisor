class PatternDetection:
    def __init__(self, config):
        self.config = config
        self.database = Database(config['database'])
        self.ticker = config['ticker']
        self.interval = config['interval']
        self.detection_methods = self.create_detection_methods(config['detection_methods'])

    def create_detection_methods(self, detection_methods_config):
        # Create detection methods based on the provided configuration
        detection_methods = []
        for method_config in detection_methods_config:
            method_class = globals()[method_config['class']]
            method_params = method_config.get('params', {})
            detection_methods.append(method_class(method_params))
        return detection_methods

    def detect_patterns(self, market_data):
        # Detect patterns in the market data using the specified detection methods
        detection_events = []
        for data_point in market_data:
            detection_event = {'ticker': self.ticker, 'interval': self.interval, 'time': data_point['time']}
            for detection_method in self.detection_methods:
                confidence_rating = detection_method.detect_pattern(data_point)
                detection_event[detection_method.__class__.__name__] = confidence_rating
            detection_events.append(detection_event)

        return detection_events

    def write_detection_to_database(self, table, detection_event, confidence_rating):
        # Write the detection to the options table with the calculated confidence rating

        # Prepare the values to be inserted into the database
        values = (
            detection_event['timestamp'],
            detection_event['interval'],
            detection_event['open'],
            detection_event['high'],
            detection_event['low'],
            detection_event['close'],
            detection_event['volume'],
            confidence_rating
        )

        # Insert the values into the database
        # The query string uses f-strings to dynamically create the table name, 
        # column names, and parameter placeholders. 
        # The get_detection_method_names() method is used to get the names of the detection methods, 
        # which are then used to construct the column names in the INSERT INTO query.

        '''
        The parameter list for the query is constructed using a combination of a list containing the ticker, interval, and time values
        for the detection event, and a list of confidence ratings for each detection method. 
        The list of confidence ratings is constructed using a list comprehension to extract the confidence rating for each 
        detection method in the order they appear in the self.detection_methods list.
        '''
        query = f"INSERT INTO {table} (timestamp, interval, open, high, low, close, volume, confidence_rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.database.execute(query, values)
