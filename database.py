import sqlite3

def init_db():
    """Initializes the database and creates the table if it doesn't exist."""
    conn = sqlite3.connect('travel_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS travel_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_query TEXT NOT NULL,
            ai_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_interaction(query, response):
    """Logs the agent's interaction into the SQLite database."""
    conn = sqlite3.connect('travel_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO travel_history (user_query, ai_response) VALUES (?, ?)', (query, response))
    conn.commit()
    conn.close()