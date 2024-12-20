import click
from models.Client import Client
from models.Project import Project
from db import create_connection
from tabulate import tabulate  # For better table display


def display_main_menu():
    """Display the main menu with available tables."""
    print("\n=== Freelancer Job Tracker ===")
    print("1. Manage Clients")
    print("2. Manage Projects")
    print("3. Exit")


def display_client_operations():
    """Display client-related operations."""
    print("\n=== Client Operations ===")
    print("1. Add Client")
    print("2. List Clients")
    print("3. Delete Client")
    print("4. Back to Main Menu")

def display_project_operations():
    """Display project-related operations."""
    print("\n=== Project Operations ===")
    print("1. Add Project")
    print("2. List Projects")
    print("3. Update Project Status")
    print("4. Delete Project")
    print("5. Back to Main Menu")


def main():
    """Interactive CLI for managing freelancer tasks."""
    while True:
        display_main_menu()
        choice = input("\nSelect an option (1-3): ").strip()

        if choice == "1":  # Manage Clients
            while True:
                display_client_operations()
                client_choice = input("\nSelect an operation (1-4): ").strip()

                if client_choice == "1":  # Add Client
                    name = input("Enter client name: ").strip()
                    email = input("Enter client email: ").strip()
                    client = Client.create_client(name, email)
                    print(f"Client added successfully: {client}")

                elif client_choice == "2":  # List Clients
                    clients = Client.get_all_clients()
                    if clients:
                        print("\nClients:")
                        print(tabulate([c.make_dict() for c in clients], headers="keys"))
                    else:
                        print("No clients found.")

                elif client_choice == "3":  # Delete Client
                    client_id = input("Enter client ID to delete: ").strip()
                    try:
                        Client.delete_client(int(client_id))
                        print(f"Client with ID {client_id} deleted successfully.")
                    except ValueError:
                        print("Invalid client ID. Please enter a number.")

                elif client_choice == "4":  # Back to Main Menu
                    break

                else:
                    print("Invalid choice. Please select a valid operation.")

        elif choice == "2":  # Manage Projects
            while True:
                display_project_operations()
                project_choice = input("\nSelect an operation (1-5): ").strip()

                if project_choice == "1":  # Add Project
                    name = input("Enter project name: ").strip()
                    description = input("Enter project description: ").strip()
                    client_id = input("Enter associated client ID: ").strip()
                    try:
                        project = Project(name=name, description=description, client_id=int(client_id))
                        project.save_to_db()
                        print(f"Project '{name}' added successfully!")
                    except ValueError:
                        print("Invalid client ID. Please enter a number.")

                elif project_choice == "2":  # List Projects
                    projects = Project.get_all_projects()
                    if projects:
                        print("\nProjects:")
                        print(tabulate(projects, headers=["ID", "Name", "Description", "Client ID", "Status"]))
                    else:
                        print("No projects found.")

                elif project_choice == "3":  # Update Project Status
                    project_id = input("Enter project ID: ").strip()
                    status = input("Enter new status (ongoing/completed): ").strip().lower()
                    if status not in ['ongoing', 'completed']:
                        print("Invalid status. Please enter 'ongoing' or 'completed'.")
                        continue
                    try:
                        Project.update_status(int(project_id), status)
                        print(f"Project {project_id} status updated to '{status}' successfully.")
                    except ValueError:
                        print("Invalid project ID. Please enter a number.")

                elif project_choice == "4":  # Delete Project
                    project_id = input("Enter project ID to delete: ").strip()
                    try:
                        Project.delete_project(int(project_id))
                        print(f"Project with ID {project_id} deleted successfully.")
                    except ValueError:
                        print("Invalid project ID. Please enter a number.")

                elif project_choice == "5":  # Back to Main Menu
                    break

                else:
                    print("Invalid choice. Please select a valid operation.")

        elif choice == "3":  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
