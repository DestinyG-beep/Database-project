import click
from models.Client import Client
from models.Project import Project
from db import create_connection
from tabulate import tabulate  # Helps display data in a tabular format.


@click.group()
def cli():
    """Freelancer Job Tracker - Manage clients and projects."""
    pass


# ----------------- CLIENT COMMANDS ----------------- #
@cli.group()
def client():
    """Manage clients."""
    pass


@client.command("create")
@click.option('--name', prompt="Client name", help="The name of the client.")
@click.option('--email', prompt="Client email", help="The email of the client.")
def create_client(name, email):
    """Create a new client."""
    conn = create_connection()
    client = Client.create_client(name, email)
    print(f"Client created successfully: {client}")


@client.command("view")
def view_clients():
    """View all clients."""
    conn = create_connection()
    clients = Client.get_all_clients()
    if clients:
        print("\nClients:")
        print(tabulate([c.make_dict() for c in clients], headers="keys", tablefmt="fancy_grid"))
    else:
        print("No clients found.")


@client.command("delete")
@click.argument('client_id', type=int)
def delete_client(client_id):
    """Delete a client by ID."""
    conn = create_connection()
    Client.delete_client(client_id)
    print(f"Client with ID {client_id} deleted successfully.")


# ----------------- PROJECT COMMANDS ----------------- #
@cli.group()
def project():
    """Manage projects."""
    pass


@project.command("create")
@click.option('--name', prompt="Project name", help="The name of the project.")
@click.option('--description', prompt="Project description", help="The description of the project.")
@click.option('--client_id', prompt="Client ID", type=int, help="The ID of the client associated with this project.")
def create_project(name, description, client_id):
    """Create a new project."""
    conn = create_connection()
    project = Project(name, description, client_id)
    project.save_to_db(conn)
    print(f"Project '{name}' created successfully!")


@project.command("view")
def view_projects():
    """View all projects."""
    conn = create_connection()
    projects = Project.get_all_projects(conn)
    if projects:
        print("\nProjects:")
        print(tabulate(projects, headers=["ID", "Name", "Description", "Client ID", "Status"], tablefmt="fancy_grid"))
    else:
        print("No projects found.")


@project.command("delete")
@click.argument('project_id', type=int)
def delete_project(project_id):
    """Delete a project by ID."""
    conn = create_connection()
    Project.delete_project(project_id, conn)
    print(f"Project with ID {project_id} deleted successfully.")


# ----------------- MAIN ENTRY POINT ----------------- #
if __name__ == "__main__":
    cli()
