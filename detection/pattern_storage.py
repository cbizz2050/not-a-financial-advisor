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
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS patterns 
                          (pattern_type text, start_date text, end_date text, symbol text, magnitude real)''')
        self.conn.commit()

    def store_pattern(self, pattern):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO patterns VALUES (?, ?, ?, ?, ?)",
                       (pattern.pattern_type, pattern.start_date, pattern.end_date, pattern.symbol, pattern.magnitude))
        self.conn.commit()
