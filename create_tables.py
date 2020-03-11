import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, position text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS pets (name text PRIMARY KEY, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()
