# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from flask import Flask, request, jsonify
from .task_manager import TaskManager

# initialize Flask app
app = Flask(__name__)

# instanz unseres TaskManagers
task_manager = TaskManager()


# route für alle tasks
@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    # return all tasks
    # HTTP status code 200 == OK
    return jsonify(task_manager.get_all_tasks()), 200


@app.route("/task", methods=["POST"])
def add_task():
    # get data from request
    data = request.get_json()
    # extract name and description from data
    name = data.get("name")
    description = data.get("description")

    # check if name and description are valid
    if not name:
        return jsonify({"error": "Name is required"}), 400
    if len(name) > 255 or (description and len(description) > 255):
        return jsonify({"error": "Name or description cannot be longer than 255 characters"}), 400

    # add task to task manager
    task_manager.add_task(name, description)
    # return to user that creation was successful
    # return HTTP status code 201 == Created
    return jsonify({"message": "Task created successfully"}), 201


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


@app.route("/tasks/<name>", methods=["DELETE"])
def remove_task(name):
    # try to remove task from task manager
    try:
        task_manager.remove_task(name)
        # return HTTP status code 200 == OK
        return jsonify({"message": "Task removed successfully"}), 200
    except KeyError:
        # return HTTP status code 404 == Not Found
        return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods=["DELETE"])
def clear_tasks():
    # clear all tasks in task manager
    task_manager.clear_tasks()
    # return HTTP status code 200 == OK
    return jsonify({"message": "All tasks removed successfully"}), 200


@app.errorhandler(Exception)
def handle_exception(e):
    # return HTTP status code 500 == Internal Server Error
    return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
