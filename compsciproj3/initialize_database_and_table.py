from database import DatabaseManager
db = DatabaseManager(name = "database.db")
db.execute(query = '''
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        username TEXT not null,
        name TEXT not null,
        email_address TEXT,
        password_hash TEXT,
        address_list TEXT, 
        is_employee INTEGER,
        confirmation_hash TEXT)
''')
db.execute(query = '''
    CREATE TABLE order_list (
        order_id INTEGER PRIMARY KEY,
        last_modified_user_id TEXT,
        user_id TEXT,
        status TEXT,
        order_date DATE,
        food_id TEXT,
        receipt_id TEXT,
        confirmation_hash TEXT)
''')
db.execute(query = '''
    CREATE TABLE food_listing (
        food_id INTEGER PRIMARY KEY,
        cost REAL,
        description TEXT,
        confirmation_hash TEXT)
''')
db.execute(query = '''
    CREATE TABLE food_listing (
        name TEXT PRIMARY KEY,
        location TEXT)
''')


