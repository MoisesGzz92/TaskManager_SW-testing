# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then

# Assuming you have a TaskManager class to manage tasks
from taskmanager.app.task_manager import TaskManager


@given("the user is using the task manager application for adding a task")
def step_given_user_on_application(context):
    """Set up the task management application for the user."""
    context.task_manager = TaskManager()  # Initialize the task manager
    context.task_manager.clear_tasks()  # Clear any existing tasks for a fresh start


@given("the name of a new task and the description of the new task is available")
def step_given_task_name_and_description_available(context):
    """Set up the task management application for the user."""
    context.task_name = "Complete project report"
    context.task_description = "Complete the project report"


@when(
    'the user adds a new task with the name "{task_name}" and the description "{task_description}"'
)
def step_when_user_adds_task(context, task_name, task_description):
    """Add a new task with the given description."""
    context.task_manager.add_task(
        task_name, task_description
    )  # Add the task using the task manager


@then("the newly created task should appear in the total list of tasks")
def step_then_task_appears_in_list(context):
    """Check that the newly created task is in the list of tasks."""
    tasks = context.task_manager.get_all_tasks()  # Retrieve all tasks
    assert any(
        task["description"] == context.task_manager.tasks[-1]["description"]
        for task in tasks
    ), "The task was not found in the list of tasks."
