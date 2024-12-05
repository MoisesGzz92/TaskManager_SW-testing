
# Task Manager API

A simple REST API for managing tasks using Flask. This API allows you to create, retrieve, update, and delete tasks.

## Features

- Add new tasks
- Retrieve all tasks
- Update existing tasks
- Delete tasks
- Clear all tasks

![API Endpoints](./assets/task_manager_api.jpeg)

## Usage

1. **Run the Flask API:**

   ```bash
   python taskmanager/app/api.py
   ```

   The API will be available at `http://127.0.0`.

2. **Interact with the API using tools like Postman or curl.**

## API Endpoints

- **GET /tasks**
  - Returns all tasks.

- **POST /tasks**
  - Adds a new task.
  - **Request Body:**
    ```json
    {
      "name": "Task Name",
      "description": "Task Description"
    }
    ```

- **DELETE /tasks/<task-name>**
  - Removes a task by its name.

- **PUT /tasks/<task-name>**
  - Updates a task by its name.
  - **Request Body:**
    ```json
    {
      "name": "Updated Task Name",
      "description": "Updated Task Description"
    }
    ```

- **DELETE /tasks**
  - Clears all tasks.

## Testing

You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) (only in Linux terminal such as WSL), [Insomnia](https://insomnia.rest/), a browser extesion such as [Talend API Designer](https://www.talend.com/products/talend-api-designer/) to test the API endpoints.
During our session we used Talend.

The following examples are based on [curl](https://curl.se/) (only in Linux terminal such as WSL).

1. Get all tasks:

   ```bash
   curl -X GET http://127.0.0.1:5001/tasks
   ```

2. Add a task (POST):

   ```bash
   curl -X POST http://127.0.0.1:5001/task \
     -H "Content-Type: application/json" \
     -d '{"name": "My Task", "description": "This is a task description."}'
   ```

5. Update a task (PUT):

   ```bash
   curl -X PUT http://127.0.0.1:5001/task/My%20Task \
     -H "Content-Type: application/json" \
     -d '{"name": "Updated Task", "description": "Updated description."}'
   ```

4. Remove a task (DELETE):

   ```bash
   curl -X DELETE http://127.0.0.1:5001/task/Updated%20Task
   ```



5. Clear all tasks:

   ```bash
   curl -X DELETE http://127.0.0.1:5001/tasks
   ```
