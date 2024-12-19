import click
from models.Client import Client
from models.Project import Project
from models.Invoice import Invoice
from db import create_connection


@click.group()
def cli():
    """Freelancer Job Tracker CLI"""
    pass

@cli.command()
@click.argument('name')
@click.argument('email')
def add_client(name, email):
    """Add a new client"""
    client = Client.create_client(name, email)
    click.echo(f"Added client: {client.make_dict()}")

@cli.command()
@click.argument('client_id', type=int)
@click.argument('title')
@click.argument('description')
def add_project(client_id, title, description):
    """Add a new project"""
    project = Project(None, client_id, title, description).save_to_db()
    click.echo(f"Added project: {project}")

@cli.command()
@click.argument('project_id', type=int)
@click.argument('amount', type=float)
def add_invoice(project_id, amount):
    """Add a new invoice"""
    invoice = Invoice.create_invoice(project_id, amount)
    click.echo(f"Added invoice: {invoice.make_invoice_dict()}")

@cli.command()
def list_clients():
    """List all clients"""
    conn = create_connection()
    clients = Client.get_all_clients(conn)
    for client in clients:
        click.echo(client.make_dict())
    conn.close()

@cli.command()
def list_projects():
    """List all projects"""
    conn = create_connection()
    projects = Project.get_all_projects(conn)
    for project in projects:
        click.echo(project)
    conn.close()

@cli.command()
def list_invoices():
    """List all invoices"""
    conn = create_connection()
    invoices = Invoice.get_all_invoices(conn)
    for invoice in invoices:
        click.echo(invoice.make_invoice_dict())
    conn.close()

if __name__ == "__main__":
    cli()