# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.


class TaskManager:
    """
    This class manages a dictionary of tasks. It initializes an empty dictionary of tasks.
    """

    def __init__(self):
        """
        Initializes the TaskManager with an empty dictionary of tasks.
        """
        self.tasks = {}

    def add_task(self, task_name, task_description):
        """
        Adds a new task to the dictionary of tasks.
        """
        # Check if the task name is valid
        if task_name is None or task_name == "":
            raise ValueError("Name cannot be empty")
        # Check if the task description is valid
        if len(task_name) > 255 or len(task_description) > 255:
            raise ValueError("Name or description cannot be longer than 255 characters")
        if task_name in self.tasks:
            raise ValueError("Task with this name already exists.")
        self.tasks[task_name] = {"description": task_description}

    def get_all_tasks(self):
        """
        Returns all tasks as a dictionary.
        """
        return self.tasks

    def get_task_by_name(self, task_name):
        """Find a task by its name."""
        if task_name is None or task_name == "":
            raise ValueError("Name cannot be empty")
        if task_name not in self.tasks:
            raise KeyError(f"Task with name '{task_name}' not found.")
        return {task_name: self.tasks[task_name]}

    def remove_task(self, task_name):
        """
        Erases a task from the dictionary of tasks.
        """
        if task_name is None or task_name == "":
            raise ValueError("Name cannot be empty")
        if task_name not in self.tasks:
            raise KeyError(f"Task with name '{task_name}' not found.")
        del self.tasks[task_name]

    def update_task(self, task_name, new_task_name=None, new_task_description=None):
        """
        Updates an existing task's name and/or description.
        :param task_name: The name of the task to update.
        :param new_task_name: The new name of the task (optional).
        :param new_task_description: The new description of the task (optional).
        :return: True if the task was updated, False if the task was not found.
        """
        if task_name is None or task_name == "":
            raise ValueError("Name cannot be empty")
        if task_name not in self.tasks:
            return False  # Task not found

        # Check if the new name is valid
        if new_task_name == "":
            raise ValueError("Name cannot be empty")
        if new_task_description == "":
            raise ValueError("Description cannot be empty")

        # Update the task
        if new_task_name:
            self.tasks[new_task_name] = self.tasks.pop(task_name)
            self.tasks[new_task_name]["description"] = (
                new_task_description
                if new_task_description
                else self.tasks[new_task_name]["description"]
            )
        elif new_task_description:
            self.tasks[task_name]["description"] = new_task_description

        return True  # Task updated successfully

    def clear_tasks(self):
        """
        Clears the dictionary of tasks.
        """
        self.tasks.clear()
