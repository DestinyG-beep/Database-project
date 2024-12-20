import click
from models.Client import Client
from models.Project import Project
from db import create_connection
from tabulate import tabulate #this is a library that helps to display data in a tabular format, making the data visually appealing.


@click.group()
def cli():
    """Freelancer Job Tracker - A command-line tool to manage clients, projects, and invoices."""
    pass


#-- CLIENT COMMANDS --#
@cli.group()
def client():
    """Manage clients."""
    pass


@client.command("add")
@click.option('--name', prompt="Client name", help="The name of the client.")
@click.option('--email', prompt="Client email", help="The email of the client.")
def add_client(name, email):
    """Add a new client."""
    conn = create_connection()
    client = Client.create_client(name, email)
    print(f"Client added successfully: {client}")


@client.command("list")
def list_clients():
    """List all clients."""
    conn = create_connection()
    clients = Client.get_all_clients()
    if clients:
        print("\nClients:")
        print(tabulate([c.make_dict() for c in clients], headers="keys"))
    else:
        print("No clients found.")


@client.command("delete")
@click.argument('client_id', type=int)
def delete_client(client_id):
    """Delete a client by ID."""
    conn = create_connection()
    Client.delete_client(client_id)
    print(f"Client with ID {client_id} deleted successfully.")


# -- PROJECT COMMANDS -- #
@cli.group()
def project():
    """Manage projects."""
    pass


@project.command("add")
@click.option('--name', prompt="Project name", help="The name of the project.")
@click.option('--description', prompt="Project description", help="The description of the project.")
@click.option('--client_id', prompt="Client ID", type=int, help="The ID of the client.")
def add_project(name, description, client_id):
    """Add a new project."""
    conn = create_connection()
    project = Project(name, description, client_id)
    project.save_to_db(conn)
    print(f"Project '{name}' added successfully!")


@project.command("list")
def list_projects():
    """List all projects."""
    conn = create_connection()
    projects = Project.get_all_projects(conn)
    if projects:
        print("\nProjects:")
        print(tabulate(projects, headers=["ID", "Name", "Description", "Client ID", "Status"]))
    else:
        print("No projects found.")


@project.command("update-status")
@click.argument('project_id', type=int)
@click.option('--status', prompt="New status", type=click.Choice(['ongoing', 'completed'], case_sensitive=False))
def update_project_status(project_id, status):
    """Update a project's status."""
    conn = create_connection()
    Project.update_status(project_id, status, conn)
    print(f"Project {project_id} status updated to '{status}' successfully.")


# -- MAIN ENTRY POINT -- #
if __name__ == "__main__":
    cli()
