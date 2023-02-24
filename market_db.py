class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        column_definitions = ', '.join([f"{column} TEXT" for column in columns])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})")

    def insert_row(self, table_name, row):
        placeholders = ', '.join(['?' for _ in row])
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)
        self.conn.commit()

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def mark_detection_event_processed(self, detection_event_id):
        self.cursor.execute(f"UPDATE detection_events SET processed = 1 WHERE id = ?", (detection_event_id,))
        self.conn.commit()