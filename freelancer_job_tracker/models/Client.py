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
        """
        Creates a new client in the database and returns a Client object.
        """
        conn = create_connection()
        cursor = conn.cursor()
        # Insert the client into the database
        cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", (name, email))
        conn.commit()

        # Fetch the auto-generated ID of the newly created client
        client_id = cursor.lastrowid

        conn.close()
        # Return the Client object with the generated ID
        return Client(client_id, name, email)
                
    @staticmethod
    def get_all_clients():
        """
        Fetches all clients from the database and returns a list of Client objects.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM clients")
        rows = cursor.fetchall()
        conn.close()
        # Create Client objects for each row
        return [Client(*row) for row in rows]
            
    @staticmethod
    def delete_client(client_id):
        """
        Deletes a client by ID.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name}, email={self.email})>"
