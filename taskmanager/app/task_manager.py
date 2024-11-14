# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.


class TaskManager:
    """
    This class manages a list of tasks. It initializes an empty list of tasks.
    """

    def __init__(self):
        """
        Initializes the TaskManager with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task_name, task_description):
        """
        Adds a new task to the list of tasks.
        """
        self.tasks.append({"name": task_name, "description": task_description})

    def get_all_tasks(self):
        """
        Returns all tasks.
        """
        return self.tasks

    def get_task_by_name(self, task_name):
        """Find a task by its name."""
        for task in self.tasks:
            if task["name"] == task_name:
                return task
        raise KeyError(f"Task with name '{task_name}' not found.")

    # TODO: GRUPPE 1: Add a method to remove a task from the list of tasks
    def remove_task(self, task_name):
        """
        Erases a task from the list of tasks.
        """
        # self.tasks.append({'name': task_name})
        # self.tasks.remove({'name': task_name})
        self.tasks = [task for task in self.tasks if task["name"] != task_name]

    # TODO: GRUPPE 2: Add a method to update a task in the list of tasks

    # TODO: GRUPPE 3: Add a method to get a task from the list of tasks

    def clear_tasks(self):
        """
        Clears the list of tasks.
        """
        self.tasks = []
