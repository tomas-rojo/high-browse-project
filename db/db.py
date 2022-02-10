import psycopg2

# Connection to DDBB for creating new table if not exists


def create_table():
    try:
        # Connect to Database
        conn = psycopg2.connect(
            dbname="data",
            user="postgres",
            password="1234567890",
            host="localhost",
            port="5432")
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
        print("Table loaded successfully!")

        # Closing connection
        conn.close()
    except:
        raise Exception("Error while connecting to Database")

# Connection to DDBB to register new user


def insert_data(name, value):

    # Connect to Database
    conn = psycopg2.connect(
            dbname="data",
            user="postgres",
            password="1234567890",
            host="localhost",
            port="5432")
    cursor = conn.cursor()

    # Inserting and Executing Query
    try:
        cursor.execute("INSERT INTO {} VALUES (%s, %s)".format('data'), (name, value,))
        conn.commit()
    except:
        print("Couldn't insert values")

    # Closing Connection
    conn.close()
