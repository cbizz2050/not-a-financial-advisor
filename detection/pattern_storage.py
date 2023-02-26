# Table: intraday_patterns
#
#| symbol | pattern_name   | start_time          | end_time            | confidence_score |
#|--------|----------------|---------------------|---------------------|------------------|
#| AAPL   | fail_swing     | 2023-03-01 12:30:00 | 2023-03-01 12:45:00 | 0.95             |

# Table: historical_patterns

# | symbol | pattern_name   | start_time  | end_time    | confidence_score |
# |--------|----------------|-------------|-------------|------------------|
# | AAPL   | fail_swing     | 2022-02-01  | 2022-03-01  | 0.90             |

import sqlite3

class PatternStorage:
    def __init__(self, intraday_db_name='intraday_patterns.db', historical_db_name='historical_patterns.db'):
        self.intraday_db_name = intraday_db_name
        self.historical_db_name = historical_db_name

        self.intraday_conn = sqlite3.connect(self.intraday_db_name)
        self.intraday_cursor = self.intraday_conn.cursor()

        self.historical_conn = sqlite3.connect(self.historical_db_name)
        self.historical_cursor = self.historical_conn.cursor()

    def store_intraday_pattern(self, pattern):
        # insert the pattern into the intraday database
        self.intraday_cursor.execute("INSERT INTO patterns (name, start_date, end_date, pattern_type, confidence) VALUES (?, ?, ?, ?, ?)",
            (pattern.name, pattern.start_date, pattern.end_date, pattern.pattern_type, pattern.confidence))
        self.intraday_conn.commit()

    def store_historical_pattern(self, pattern):
        # insert the pattern into the historical database
        self.historical_cursor.execute("INSERT INTO patterns (name, start_date, end_date, pattern_type, confidence) VALUES (?, ?, ?, ?, ?)",
            (pattern.name, pattern.start_date, pattern.end_date, pattern.pattern_type, pattern.confidence))
        self.historical_conn.commit()
