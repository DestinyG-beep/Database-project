import sqlite3
from db import create_connection

class Project:
    def __init__(self, id=None, name=None, description=None, client_id=None, status='ongoing'):
        self.id = id
        self.name = name
        self.description = description
        self.client_id = client_id
        self.status = status

    # Create the 'projects' table
    @classmethod
    def create_table(cls):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                client_id INTEGER,
                status TEXT
            )
        ''')
        conn.commit()
        conn.close()

    # Save a project to the database
    def save_to_db(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO projects (name, description, client_id, status)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.description, self.client_id, self.status))
        conn.commit()
        conn.close()

    # Fetch all projects
    @classmethod
    def get_all_projects(cls):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM projects')
        rows = cursor.fetchall()
        conn.close()
        return [
            cls(id=row[0], name=row[1], description=row[2], client_id=row[3], status=row[4])
            for row in rows
        ]

    # Fetch a project by its ID
    @classmethod
    def get_project_by_id(cls, project_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row[0], name=row[1], description=row[2], client_id=row[3], status=row[4])
        return None

    # Delete a project by its ID
    @classmethod
    def delete_project(cls, project_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
        conn.commit()
        conn.close()

    # Update the status of a project
    @classmethod
    def update_status(cls, project_id, new_status):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            UPDATE projects
            SET status = ?
            WHERE id = ?
        ''', (new_status, project_id))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name}, client_id={self.client_id}, status={self.status})>"
