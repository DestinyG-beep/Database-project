from db import create_connection

def new_client(client_id, title, description, status, deadline):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (client_id, title, description, status, deadline) VALUES (?, ?, ?)",
        (client_id, title, description, status, deadline),
    )
    conn.commit()
    conn.close()
    