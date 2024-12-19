import sqlite3
import datetime
from db import create_connection

class Project:
    def __init__(self, name, description, client_id, status='ongoing'):
        self.name = name
        self.description = description
        self.client_id = client_id
        self.status = status

    def save_to_db(self, conn):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO projects (name, description, client_id, status)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.description, self.client_id, self.status))
        conn.commit()

    @staticmethod
    def get_all_projects(conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM projects')
        rows = cursor.fetchall()
        return [
            Project(name=row[1], description=row[2], client_id=row[3], status=row[4])
            for row in rows
        ]
    
    def __repr__(self):
        return f"<Project(name={self.name}, client_id={self.client_id})>"

