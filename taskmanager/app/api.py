# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from flask import Flask, request, jsonify
from flask_cors import CORS
from task_manager import TaskManager

# initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:8080", "http://127.0.0.1:8080"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type"],
        }
    },
)

# instanz unseres TaskManagers
task_manager = TaskManager()


# route für alle tasks
@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    tasks = task_manager.get_all_tasks()
    if not tasks:
        return jsonify([]), 200  # Return empty array instead of empty dict
    return jsonify(list(tasks.values())), 200  # Convert dict to list if needed


@app.route("/task", methods=["POST"])
def add_task():
    # get data from request
    data = request.get_json()
    print("Received data:", data)  # Debug print
    print("Request headers:", request.headers)  # Debug print

    # extract name and description from data
    name = data.get("name")
    description = data.get("description")
    print("Extracted name:", name)  # Debug print
    print("Extracted description:", description)  # Debug print

    # check if name and description are valid
    if not name:
        return jsonify({"error": "Name is required"}), 400

    try:
        # add task to task manager
        task_manager.add_task(name, description)
        return jsonify({"message": "Task created successfully"}), 201
    except Exception as e:
        print("Error adding task:", str(e))  # Debug print
        return jsonify({"error": str(e)}), 400


# remove one task from the task manager
@app.route("/task/<task_name>", methods=["DELETE"])
def delete_task(task_name):
    try:
        # delete task from task manager
        task_manager.remove_task(task_name)
        # return to user that deletion was successful
        return jsonify({"message": "Task deleted successfully"}), 200

    except KeyError:
        # return 404 if task does not exist
        return jsonify({"error": "Task not found"}), 404


@app.route("/task/<string:task_name>", methods=["PUT"])
def update_task(task_name):
    # get data from request
    data = request.get_json()
    # extract new name and description from data
    new_name = data.get("name")
    new_description = data.get("description")

    try:
        # try to update task in task manager
        task_manager.update_task(task_name, new_name, new_description)
        # return HTTP status code 200 == OK
        return jsonify({"message": "Task updated successfully"}), 200
    except KeyError:
        # return HTTP status code 404 == Not Found
        return jsonify({"error": f"Task with name '{task_name}' not found."}), 404
    except ValueError as e:
        # return HTTP status code 400 == Bad Request
        return jsonify({"error": str(e)}), 400


@app.route("/tasks", methods=["DELETE"])
def clear_all_tasks():
    # delete all tasks
    task_manager.clear_tasks()
    # return to user that delete was succesful
    return jsonify({"message": "All tasks were deleted succesfully"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
