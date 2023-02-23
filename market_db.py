import mysql.connector

class Database:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        # Connect to the database using the configuration parameters
        self.connection = mysql.connector.connect(**self.config)

    def execute(self, query, values=None, commit=True):
        # Execute a SQL query on the database

        # Connect to the database if not already connected
        if self.connection is None:
            self.connect()

        # Create a cursor object for executing the query
        cursor = self.connection.cursor()

        # Execute the query with the provided values
        if values is None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)

        # Commit the transaction if specified
        if commit:
            self.connection.commit()

        # Return the results of the query
        results = cursor.fetchall()

        # Close the cursor
        cursor.close()

        return results
