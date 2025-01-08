# Freelancer Job Tracker

## Overview
The Freelancer Job Tracker is a command-line interface (CLI) application designed for freelancers to efficiently manage their clients, projects, and invoices. It allows users to perform CRUD (Create, Read, Update, Delete) operations on clients and projects, track project statuses, and keep records of related data in an SQLite database.

---

## Features

- **Client Management:** Add, list, and delete clients.
- **Project Management:**
  - Add new projects linked to a specific client.
  - List all existing projects.
  - Update project statuses (e.g., ongoing, completed).
  - Delete projects.
- **SQLite Database:** Persistent storage of clients and projects.
- **Tabular Output:** Displays data in user-friendly tables using the `tabulate` library.

---

## Prerequisites

Before running the project, ensure the following are installed on your system:

1. **Python (>=3.8):** Required to execute the application.
2. **Virtual Environment (optional but recommended):** To manage project dependencies.
3. **Required Python Packages:**
   - `click`
   - `tabulate`

---

## Installation
you will need to fork this repository first .Be sure to mind every step in the installation instructions.

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:DestinyG-beep/Database-project.git
   cd Database-project

   ```

2. **This file that you have cloned is comprised of the README.md and the (freelancer_job_tracker) that holds all the project files, ie; it is a folder within a folder. For this project to work, you will need to go into that folder**
   ```bash
   cd freelancer_job_tracker
   ```

3. **At this point you have the option to run this application from your terminal or to use it in your code editor.**
     If you do not want to go to your editor . just continue to the next step of the instructrions.
     If you want to open it in your editor write this in your terminal;
      ```bash
   code .
   ```
   or however you do to open your terminal
    
4. **Install Dependencies:**
   ```bash
   pipenv install
   ```

5. **In the terminal of either your editor or your virtual environment, set up the working environment for this application;
    ```bash
   pipenv shell
   ```

6. **Initialize the Database:**
   Run the `db.py` script to create the necessary SQLite database and tables:
   ```bash
   python db.py
   ```
   This will create a `freelancer_tracker.db` file in the project directory.If you do not notice any changes , do not worry since the file is already in the folder

---

## Usage

Run the main `cli.py` script to start the Freelancer Job Tracker application:
```bash
python cli.py
```

### Main Menu
The main menu offers the following options:
```plaintext
=== Freelancer Job Tracker ===
1. Manage Clients
2. Manage Projects
3. Exit
```

Select an option by entering the corresponding number.

### Client Operations
If you choose `1` (Manage Clients), you will see the following options:
```plaintext
=== Client Operations ===
1. Add Client
2. List Clients
3. Delete Client
4. Back to Main Menu
```
- **Add Client:** Provide the name and email of the client.
- **List Clients:** View all clients in a tabular format.
- **Delete Client:** Enter the client ID to delete them.
- **Back to Main Menu:** Return to the main menu.

### Project Operations
If you choose `2` (Manage Projects), you will see the following options:
```plaintext
=== Project Operations ===
1. Add Project
2. List Projects
3. Update Project Status
4. Delete Project
5. Back to Main Menu
```
- **Add Project:** Provide the project name, description, and associated client ID.
- **List Projects:** View all projects in a tabular format with their details.
- **Update Project Status:** Change the status of a project (e.g., from `ongoing` to `completed`).
- **Delete Project:** Enter the project ID to delete it.
- **Back to Main Menu:** Return to the main menu.

### Exit
If you choose `3` (Exit), the application will close.

---

## Example Workflow

1. **Add a Client:**
   ```plaintext
   Enter client name: John Doe
   Enter client email: john.doe@example.com
   Client added successfully: {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'}
   ```

2. **Add a Project:**
   ```plaintext
   Enter project name: Website Design
   Enter project description: Design a portfolio website.
   Enter associated client ID: 1
   Project 'Website Design' added successfully!
   ```

3. **List Projects:**
   ```plaintext
   Projects:
     ID    Name              Description                 Client ID    Status
   ----  ----------------  --------------------------  -----------  --------
      1  Website Design    Design a portfolio website           1    ongoing
   ```

4. **Update Project Status:**
   ```plaintext
   Enter project ID: 1
   Enter new status (ongoing/completed): completed
   Project 1 status updated to 'completed' successfully.
   ```

---

## Project Structure

```
Freelancer-Job-Tracker/
├── cli.py               # Main CLI application
├── db.py                # Database initialization and connection
├── models/
│   ├── __init__.py      # Model package initializer
│   ├── Client.py        # Client model
│   ├── Project.py       # Project model
├── freelancer_tracker.db # SQLite database file (created after running db.py)
├── requirements.txt     # Required Python dependencies
└── README.md            # Documentation file
```

---

## Dependencies

The project relies on the following Python packages:

- **`click`**: For building the CLI interface.
- **`tabulate`**: For formatting data into tables in the terminal.

These dependencies are listed in the `requirements.txt` file and can be installed via pip:
```bash
pip install -r requirements.txt
```

---

## Known Issues and Improvements

1. **Error Handling:**
   - Limited error handling for invalid inputs (e.g., invalid client or project IDs).
   - Could be enhanced with custom exceptions.

2. **Data Validation:**
   - Email validation could be added when creating clients.
   - Project deadlines could be validated to ensure correct date format.

3. **Search Functionality:**
   - Adding search features for clients or projects would improve usability.

4. **Reporting:**
   - Exporting project or client data to a file (e.g., CSV) could be useful for users.

---

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

