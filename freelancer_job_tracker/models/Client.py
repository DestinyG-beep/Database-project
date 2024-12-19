from db import create_connection

def new_client(name, email, freelancer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO freelancers (freelancer_id, name, email) VALUES (?, ?, ?)",
        (freelancer_id, name, email),
    )
    conn.commit()
    conn.close()
