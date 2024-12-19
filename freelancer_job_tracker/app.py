from models import Client, Freelancer, Invoice, Project
from db import create_connection

def main():
    # Example usage of the models
    conn = create_connection()

    # Add a new client
    new_client = Client.create_client("Jane Doe", "jane.doe@example.com")
    print(f"Added client: {new_client.make_dict()}")

    # Add a new project
    new_project = Project(None, new_client.id, "Mobile App Development", "Develop a new mobile app").save_to_db()
    print(f"Added project: {new_project}")

    # Add a new invoice
    new_invoice = Invoice.create_invoice(new_project.id, 2000.00)
    print(f"Added invoice: {new_invoice.make_invoice_dict()}")

    # List all clients
    clients = Client.get_all_clients(conn)
    for client in clients:
        print(client.make_dict())

    # List all projects
    projects = Project.get_all_projects(conn)
    for project in projects:
        print(project)

    # List all invoices
    invoices = Invoice.get_all_invoices(conn)
    for invoice in invoices:
        print(invoice.make_invoice_dict())

    conn.close()

if __name__ == "__main__":
    main()

