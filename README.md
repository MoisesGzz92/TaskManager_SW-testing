# Task Management Application

This web application is designed to manage tasks or to-dos in the form of a list. It allows users to perform the following key features using a web browser:

- **Add a Task**: Users can create a new task with a description. Each task is automatically assigned a unique ID and starts with a status of “not completed.”
- **View All Tasks**: Users can retrieve a complete list of tasks, including details like task ID, description, and completion status, for an easy overview of ongoing tasks.
- **Mark a Task as Completed**: Users can mark tasks as completed using the task’s ID, changing the task’s status from “not completed” to “completed.”
- **Delete a Task**: Users can remove tasks by their ID. Once deleted, a task is permanently removed from the task list.

If you are a user and want to use the application, follow the instructions in the [Running the project](#running-the-project) section.
If you are a developer and want to run the project locally, follow the instructions in the [Development](#development) section.

## Project Description

This project consists of two parts:

- A Python API built with Flask, located in the `taskmanager` directory
- A Vue.js browser application for managing tasks in a web browser, located in the `vue-task-manager` directory

# [Running the project](#running-the-project)

If you are a user and want to use the application, we are recommending to use the provided Docker files.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- OCI compliant container engine (e.g. Docker, Podman, etc.)
- OCI compliant compose tool (e.g. Docker Compose, Podman Compose, etc.)

For simplicity, we are using Docker in this example.

## Run the web application using Docker Compose

```bash
# Navigate to the project root directory
cd TaskManager_SW-testing

# Run the web application using Docker Compose
# it will take a while to build the first time
docker compose -f docker-compose/docker-compose.yml up --build

# open the web application in your default browser
open http://localhost:8080

# use the following command to stop the web application
docker compose -f docker-compose/docker-compose.yml down
```

## Run the web application using only Docker

```bash
# navigate to the project root directory
cd TaskManager_SW-testing

# build the flask backend application
docker build -t taskmanager-flask taskmanager/

# build the vue frontend application
docker build -t taskmanager-vue vue-task-manager/

# 1st terminal: run the flask backend application using Docker
docker run -p 5001:5001 taskmanager-flask

# 2nd terminal: run the vue frontend application using Docker
docker run -p 8080:8080 taskmanager-vue
```

# [Development](#development)

If you are a developer and want to run the project locally, you need to install the required packages and run the tests.


## Prerequisites (Flask API)

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- pip (Python package installer)

## Prerequisites (Vue.js Frontend)

Before you begin, ensure you have met the following requirements:

- Node.js >= 23.3.0 and npm >= 10.9.0

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/MoisesGzz92/TaskManager_SW-testing
   cd TaskManager_SW-testing
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   # On Windows use
   .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r taskmanager/requirements.txt
   ```

## Running Tests (Task Manager API)

To ensure the application works as expected, you can run tests using `pytest` and `behave`.

### Running Unit Tests (Pytest)

To run the unit tests within the `taskmanager` directory using `pytest`, execute the following command in your terminal:

```bash
pytest
```

### Running Behavior-Driven Tests (Behave)

To run the behavior-driven tests within the `taskmanager` directory using `behave`, execute the following command in your terminal:

```bash
behave
```

## Running Taskmanager Flask API Backend

To run the Flask backend within the `taskmanager` directory, execute the following command in your terminal:

```bash
# navigate to the taskmanager directory
cd taskmanager

# run the Flask backend
python app/api.py
```

## Running Taskmanager Vue.js Frontend

To run the Vue.js frontend within the `vue-task-manager` directory, execute the following command in your terminal:

```bash
# navigate to the vue-task-manager directory
cd vue-task-manager

# run the Vue.js frontend
npm run serve
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
