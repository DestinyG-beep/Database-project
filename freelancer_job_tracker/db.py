import sqlite3
from pathlib import Path

DB_FILE = "freelancer_tracker.db"


def create_connection(db_file=DB_FILE):
    """
    Creates a database connection to the SQLite database.
    
    Args:
        db_file (str): Path to the database file.

    Returns:
        sqlite3.Connection: SQLite connection object.
    """
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database at {db_file}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def create_tables(conn):
    """
    Creates necessary tables for the application.

    Args:
        conn (sqlite3.Connection): SQLite connection object.
    """
    try:
        cursor = conn.cursor()

        
        tables = {
            "freelancer": """
                CREATE TABLE IF NOT EXISTS freelancers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """,
            "clients": """
               CREATE TABLE IF NOT EXISTS clients (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL UNIQUE,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                );
            """,
            "projects": """
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'ongoing',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    deadline DATE,
                    FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE
                );
            """,
            "invoices": """
                CREATE TABLE IF NOT EXISTS invoices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    status TEXT DEFAULT 'unpaid',
                    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    paid_at TIMESTAMP,
                    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
                );
            """
        }

        for table_name, create_sql in tables.items():
            print(f"Creating table {table_name}...")
            cursor.execute(create_sql)

        conn.commit()
        print("All tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")


if __name__ == "__main__":
    
    db_file_path = Path(DB_FILE)
    if not db_file_path.exists():
        print(f"Database file {DB_FILE} does not exist. Creating a new one...")

    
    connection = create_connection()
    if connection:
        create_tables(connection)
        connection.close()
        print("Database setup complete!")
