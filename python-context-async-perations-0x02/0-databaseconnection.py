"""Database connection context manager.

Provides DatabaseConnection class that manages sqlite3 connections using
__enter__ and __exit__ so it can be used with the `with` statement.

Usage:
    from database_connection import DatabaseConnection

    with DatabaseConnection('example.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT 1')
"""
import sqlite3
from typing import Optional


class DatabaseConnection:
    """Class-based context manager for sqlite3 connections.

    Parameters
    - db_path: path to sqlite database file. Use ':memory:' for in-memory DB.

    Behavior
    - __enter__ opens and returns the sqlite3.Connection object
    - __exit__ commits (if no exception) and closes the connection
    """

    def __init__(self, db_path: str = ':memory:') -> None:
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

    def __enter__(self) -> sqlite3.Connection:
        # Open the connection and return it
        self.conn = sqlite3.connect(self.db_path)
        # Return the connection so the user can get cursor and execute queries
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        # If the connection was opened, commit on success, otherwise rollback
        if self.conn:
            try:
                if exc_type is None:
                    self.conn.commit()
                else:
                    # If an exception occurred, rollback to avoid partial commits
                    self.conn.rollback()
            finally:
                self.conn.close()
                self.conn = None

        # Returning False will propagate exception (if any) to caller.
        return False
