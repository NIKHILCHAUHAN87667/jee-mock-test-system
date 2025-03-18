import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        # Establish the connection
        conn = mysql.connector.connect(
            host="localhost",       # MySQL server address
            user="root",            # Your MySQL username
            password="0212",# Your MySQL password
            database="mock_test" # Your database name
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
