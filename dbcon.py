import sys
import os
import psycopg2
import logging
from dotenv import load_dotenv

#=================================================================================
# (1.1) CONNECT TO DATABASE AND CHECK FOR ERRORS
def get_db_connection():
    """
    Docstring for get_db_connection
    
    - establish connection with the database
    - end the program and log into log file if the connection fails
    - if connection established returns the connection object for futher use

    """
    load_dotenv()
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB_NAME"),
            user=os.getenv("POSTGRES_USERNAME"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
        )
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        logging.error(f"Connection Error: {error}")
        print("\n CRITICAL ERROR: Could not connect to database.")
        print("Please check if your DB credentials are correct and PostgreSQL is running.")
        sys.exit(1)