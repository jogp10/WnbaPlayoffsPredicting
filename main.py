# For MySQL Connector/Python
import mysql.connector

import json

with open("config.json") as config_file:
    config = json.load(config_file)

host = config["db_host"]
user = config["db_user"]
password = config["db_password"]
database = config["db_database"]


connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()


cursor.execute("SELECT * FROM awards_players")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()