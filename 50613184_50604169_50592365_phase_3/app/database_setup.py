import sqlite3

connection = sqlite3.connect('recommendations.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skin_type TEXT,
        budget REAL,
        primary_category TEXT,
        sub_category TEXT,
        label TEXT,
        product_name TEXT,
        rank REAL,
        price REAL
    )
''')
connection.commit()
connection.close()

print("Database and table created successfully.")
