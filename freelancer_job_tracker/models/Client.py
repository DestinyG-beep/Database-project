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

    @classmethod
    def create_client(cls, name, email):
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
        return cls(client_id, name, email)  # Use 'cls' to create an instance of the class

    @classmethod
    def get_all_clients(cls):
        """
        Fetches all clients from the database and returns a list of Client objects.
        """
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM clients")
        rows = cursor.fetchall()
        conn.close()
        # Create Client objects for each row
        return [cls(*row) for row in rows]  # Use 'cls' to create instances of the class

    @classmethod
    def delete_client(cls, client_id):
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
