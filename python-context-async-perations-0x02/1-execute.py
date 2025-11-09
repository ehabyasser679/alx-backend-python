"""Simple interest module placeholder repurposed as a demo for
DatabaseConnection context manager.

This file implements a class-based context manager `DatabaseConnection`
using __enter__ and __exit__, then demonstrates using it to run
`SELECT * FROM users` and print the results.
"""
import sqlite3
from typing import Optional
import os


class DatabaseConnection:
	"""Class-based context manager for sqlite3 connections.

	Example:
		with DatabaseConnection('demo_users.db') as conn:
			cur = conn.cursor()
			cur.execute('SELECT * FROM users')
			print(cur.fetchall())
	"""

	def __init__(self, db_path: str = ':memory:') -> None:
		self.db_path = db_path
		self.conn: Optional[sqlite3.Connection] = None

	def __enter__(self) -> sqlite3.Connection:
		self.conn = sqlite3.connect(self.db_path)
		return self.conn

	def __exit__(self, exc_type, exc_value, traceback) -> bool:
		if self.conn:
			try:
				if exc_type is None:
					self.conn.commit()
				else:
					self.conn.rollback()
			finally:
				self.conn.close()
				self.conn = None
		return False


def setup_demo_db(path: str) -> None:
	"""Create `users` table and insert sample rows if empty."""
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
		cur.execute('SELECT COUNT(*) FROM users')
		count = cur.fetchone()[0]
		if count == 0:
			cur.executemany(
				'INSERT INTO users (username, email) VALUES (?, ?)',
				[
					('alice', 'alice@example.com'),
					('bob', 'bob@example.com'),
					('carol', 'carol@example.com'),
				],
			)


def print_users(path: str) -> None:
	"""Use DatabaseConnection to execute SELECT * FROM users and print rows."""
	with DatabaseConnection(path) as conn:
		cur = conn.cursor()
		cur.execute('SELECT * FROM users')
		rows = cur.fetchall()

	print(f"Found {len(rows)} users:")
	for row in rows:
		print(row)


if __name__ == '__main__':
	DB_FILE = os.path.join(os.path.dirname(__file__), 'demo_users.db')
	setup_demo_db(DB_FILE)
	print_users(DB_FILE)
