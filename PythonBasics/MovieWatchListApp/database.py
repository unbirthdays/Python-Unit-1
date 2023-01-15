import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY (user_username) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);
"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"
INSERT_USER = "INSERT INTO users (username) VALUES (?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = """SELECT movies.* FROM movies
JOIN watched ON movies.id = watched.movie_id
JOIN users ON users.username = watched.user_username
WHERE users.username = ?;"""
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?,?)"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE ?;"
CREATE_RELEASE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp);"

connection = sqlite3.connect("data.db")

def create_tables():
    connection.execute(CREATE_MOVIES_TABLE)
    connection.execute(CREATE_WATCHED_TABLE)
    connection.execute(CREATE_USERS_TABLE)
    connection.execute(CREATE_RELEASE_INDEX)
    connection.commit()

def add_user(username):
    connection.execute(INSERT_USER, (username,))
    connection.commit()

def add_movie(title, release_timestamp):
    connection.execute(INSERT_MOVIES, (title, release_timestamp)) # reminder that cursor.execute expects a tuple
    connection.commit()

def get_movies(upcoming=False):
    cursor = connection.cursor()
    if upcoming:
        today_timestamp = datetime.datetime.today().timestamp() # these are all methods within datetime that we imported
        cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        connection.commit()
    else:
        cursor.execute(SELECT_ALL_MOVIES)
        connection.commit()
    return cursor.fetchall()

def search_movies(search_term):
    cursor = connection.cursor()
    cursor.execute(SEARCH_MOVIES, (f"%{search_term}%",))
    connection.commit()
    return cursor.fetchall()

def watch_movie(username, movie_id):
    connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))
    connection.commit()

def get_watched_movies(username):
    cursor = connection.cursor()
    cursor.execute(SELECT_WATCHED_MOVIES, (username,))
    connection.commit()
    return cursor.fetchall()
