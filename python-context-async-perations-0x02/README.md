# DatabaseConnection demo

This small project demonstrates a class-based context manager `DatabaseConnection` that manages sqlite3 database connections using `__enter__` and `__exit__`.

Files
- `database_connection.py` — contains `DatabaseConnection` class
- `demo_db.py` — demo script that creates a `users` table, inserts sample rows, and prints the results of `SELECT * FROM users`

Run the demo (Windows PowerShell):

```powershell
python .\demo_db.py
```

This will create `demo_users.db` next to the scripts and print the inserted users.
