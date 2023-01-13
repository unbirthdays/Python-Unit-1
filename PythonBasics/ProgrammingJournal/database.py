import sqlite3
connection = sqlite3.connect("data.db")
# connection.row_factory = sqlite3.Row   # USE TO ACCESS AS STRING PROPERTIES

def create_table():
    connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")
    connection.commit()

def add_entry(entry_content, entry_date):
    connection.execute("INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date))
    connection.commit()

def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
