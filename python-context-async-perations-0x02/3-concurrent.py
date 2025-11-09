"""Async demo using aiosqlite to fetch users concurrently.

This script creates a small database `async_demo_users.db` with a `users` table
that includes an `age` column, inserts sample rows, and runs two async queries
concurrently using asyncio.gather:
- async_fetch_users(): fetches all users
- async_fetch_older_users(): fetches users older than 40

Run with: python async_demo.py
"""
import asyncio
import aiosqlite
import os


DB_FILE = os.path.join(os.path.dirname(__file__), 'async_demo_users.db')


async def setup_db(path: str) -> None:
    async with aiosqlite.connect(path) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        await db.commit()

        async with db.execute('SELECT COUNT(*) FROM users') as cur:
            row = await cur.fetchone()
            count = row[0]

        if count == 0:
            users = [
                ('alice', 'alice@example.com', 30),
                ('bob', 'bob@example.com', 45),
                ('carol', 'carol@example.com', 55),
                ('dave', 'dave@example.com', 22),
            ]
            await db.executemany('INSERT INTO users (username, email, age) VALUES (?, ?, ?)', users)
            await db.commit()


async def async_fetch_users(path: str):
    """Fetch all users asynchronously."""
    async with aiosqlite.connect(path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute('SELECT * FROM users') as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]


async def async_fetch_older_users(path: str, min_age: int = 40):
    """Fetch users older than min_age asynchronously."""
    async with aiosqlite.connect(path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute('SELECT * FROM users WHERE age > ?', (min_age,)) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]


async def fetch_concurrently(path: str):
    # Run both queries concurrently
    all_users_task = async_fetch_users(path)
    older_users_task = async_fetch_older_users(path, 40)

    all_users, older_users = await asyncio.gather(all_users_task, older_users_task)

    print(f"All users ({len(all_users)}):")
    for u in all_users:
        print(u)

    print(f"\nUsers older than 40 ({len(older_users)}):")
    for u in older_users:
        print(u)


if __name__ == '__main__':
    try:
        import aiosqlite  # ensure available
    except Exception as e:
        print('aiosqlite is required. Install with: pip install aiosqlite')
        raise

    asyncio.run(setup_db(DB_FILE))
    asyncio.run(fetch_concurrently(DB_FILE))
