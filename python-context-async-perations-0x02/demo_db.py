"""Demo script for DatabaseConnection context manager.

This script will:
 - create a SQLite database file `demo_users.db` (in the current directory)
 - create a `users` table if it doesn't exist
 - insert a few sample users
 - use the DatabaseConnection context manager to SELECT * FROM users and print rows
"""
from databaseconnection import DatabaseConnection
import os


DB_FILE = os.path.join(os.path.dirname(__file__), 'demo_users.db')


def setup_db(path: str) -> None:
    # Use the context manager to create table and insert sample data
    with DatabaseConnection(path) as conn:
        cur = conn.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
            '''
        )

        # Insert sample data only if table is empty
        cur.execute('SELECT COUNT(*) FROM users')
        count = cur.fetchone()[0]
        if count == 0:
            users = [
                ('alice', 'alice@example.com'),
                ('bob', 'bob@example.com'),
                ('carol', 'carol@example.com'),
            ]
            cur.executemany('INSERT INTO users (username, email) VALUES (?, ?)', users)


def print_users(path: str) -> None:
    # Demonstrate using DatabaseConnection to SELECT * FROM users
    with DatabaseConnection(path) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()

        print(f"Found {len(rows)} users:")
        for row in rows:
            print(row)


if __name__ == '__main__':
    setup_db(DB_FILE)
    print_users(DB_FILE)
"""Demo script for DatabaseConnection context manager.

This script will:
 - create a SQLite database file `demo_users.db` (in the current directory)
 - create a `users` table if it doesn't exist
 - insert a few sample users
 - use the DatabaseConnection context manager to SELECT * FROM users and print rows
"""
from databaseconnection import DatabaseConnection
import os


DB_FILE = os.path.join(os.path.dirname(__file__), 'demo_users.db')


def setup_db(path: str) -> None:
    # Use the context manager to create table and insert sample data
    with DatabaseConnection(path) as conn:
        cur = conn.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
            '''
        )

        # Insert sample data only if table is empty
        cur.execute('SELECT COUNT(*) FROM users')
        count = cur.fetchone()[0]
        if count == 0:
            users = [
                ('alice', 'alice@example.com'),
                ('bob', 'bob@example.com'),
                ('carol', 'carol@example.com'),
            ]
            cur.executemany('INSERT INTO users (username, email) VALUES (?, ?)', users)


def print_users(path: str) -> None:
    # Demonstrate using DatabaseConnection to SELECT * FROM users
    with DatabaseConnection(path) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()

        print(f"Found {len(rows)} users:")
        for row in rows:
            print(row)


if __name__ == '__main__':
    setup_db(DB_FILE)
    """Demo script for DatabaseConnection context manager.

    This script will:
     - create a SQLite database file `demo_users.db` (in the current directory)
     - create a `users` table if it doesn't exist
     - insert a few sample users
     - use the DatabaseConnection context manager to SELECT * FROM users and print rows
    """
    from databaseconnection import DatabaseConnection
    import os


    DB_FILE = os.path.join(os.path.dirname(__file__), 'demo_users.db')


    def setup_db(path: str) -> None:
        # Use the context manager to create table and insert sample data
        with DatabaseConnection(path) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL
                )
                '''
            )

            # Insert sample data only if table is empty
            cur.execute('SELECT COUNT(*) FROM users')
            count = cur.fetchone()[0]
            if count == 0:
                users = [
                    ('alice', 'alice@example.com'),
                    ('bob', 'bob@example.com'),
                    ('carol', 'carol@example.com'),
                ]
                cur.executemany('INSERT INTO users (username, email) VALUES (?, ?)', users)


    def print_users(path: str) -> None:
        # Demonstrate using DatabaseConnection to SELECT * FROM users
        with DatabaseConnection(path) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM users')
            rows = cur.fetchall()

            print(f"Found {len(rows)} users:")
            for row in rows:
                print(row)


    if __name__ == '__main__':
        setup_db(DB_FILE)
        print_users(DB_FILE)
