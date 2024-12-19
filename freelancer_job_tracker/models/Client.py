from db import create_connection

class Client:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def make_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
    
    @staticmethod
    def create_client(name, email):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        return Client( name, email)
                
    @staticmethod
    def get_all_clients():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM clients")
        rows = cursor.fetchall()
        conn.close()
        return [Client(*row) for row in rows]
            
    @staticmethod
    def delete_client(client_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
        conn.commit()
        conn.close()

