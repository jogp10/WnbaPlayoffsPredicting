import json
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("config.json") as config_file:
    config = json.load(config_file)

host = config["db_host"]
user = config["db_user"]
password = config["db_password"]
database = config["db_database"]
schema = config["db_schema"]

# SELECT
SELECT = "SELECT * FROM " + schema + "." # + table_name

# INSERT
INSERT = "INSERT INTO " + schema + "."  # + table_name + " VALUES " + values

# UPDATE
UPDATE = "UPDATE " + schema + "." # + table_name + " SET " + column_name + " = " + value

# DELETE
DELETE = "DELETE FROM " + schema + "." # + table_name + " WHERE " + column_name + " = " + value


# Functions so I can reutilize the code
def connect():
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    return connection, cursor

def close(connection, cursor):
    cursor.close()
    connection.close()

def execute(connection, cursor, query):
    cursor.execute(query)
    connection.commit()
    return cursor.fetchall()

def fetch(connection, cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

def fetchone(connection, cursor, query):
    cursor.execute(query)
    return cursor.fetchone()

def fetchmany(connection, cursor, query, size):
    cursor.execute(query)
    return cursor.fetchmany(size)

def insert(connection, cursor, query, values):
    cursor.execute(query, values)
    connection.commit()
    return cursor.lastrowid

def update(connection, cursor, query, values):
    cursor.execute(query, values)
    connection.commit()

def delete(connection, cursor, query, values):
    cursor.execute(query, values)
    connection.commit()
