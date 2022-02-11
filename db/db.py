import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


# Creating connection to Database


def create_connection():
    connection = psycopg2.connect(
        dbname=os.getenv('PG_DBNAME'),
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASS'),
        host=os.getenv('PG_HOST'),
        port=os.getenv('PG_PORT'))
    return connection


# Creating new table if not exists

def create_table():
    try:
        # Connect to Database
        conn = create_connection()
        cursor = conn.cursor()

        # SQL Command for creating table
        sql = """CREATE TABLE IF NOT EXISTS data( 
                name VARCHAR(255),
                value VARCHAR
                )
                """

        # Inserting and Executing Query
        cursor.execute(sql)
        conn.commit()
        print("Connection to Database successfully!")

        conn.close()

    except:
        print("Error while connecting to Database")


# Connection to DDBB to insert data

def insert_data(name, value):
    try:
        # Connect to Database
        conn = create_connection()
        cursor = conn.cursor()

        # Inserting and Executing Query
        db_name = os.getenv('PG_DBNAME')
        cursor.execute("INSERT INTO {} VALUES (%s, %s)".format(db_name), (name, value,))
        conn.commit()

        conn.close()

    except:
        print("Couldn't insert values to Database")
