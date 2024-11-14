# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then

# handle to the task manager application
from taskmanager.app.task_manager import TaskManager

# TODO: GRUPPE 1 - Add BDD steps for removing a task


@given("the user of the task manager application wants to delete an existing task")
def step_given_user_is_using_task_manager_application(context):
    # Instanziierung eines TaskManager und speichern in context
    """Set up the task management application for the user."""
    context.task_manager = TaskManager()  # Initialize the task manager
    context.task_manager.clear_tasks()  # Clear any existing tasks for a fresh start


@given('the name of the task to be deleted is "{task_name}"')
def step_user_defines_task_as_irrelevant(context, task_name):
    # Erzeugen eines tasks mit Namen “task_name” und speichern mittels add_task()
    """Add a new task with the given name."""
    context.task_manager.add_task(
        task_name, "Dummy description"
    )  # Add the task using the task manager

    # prüfen mit assert, ob task in task list verfügbar, z.B.: mit get_all_tasks()
    """Check that the newly created task is in the list of tasks."""
    tasks = context.task_manager.get_all_tasks()  # Retrieve all tasks
    assert any(
        task["name"] == task_name for task in tasks
    ), "The task {task_name} was not found in the list of tasks."


@when('the user erases the task "{task_name}" from the list of tasks')
def step_when_user_erases_task(context, task_name):
    # hier wird nun die von euch implementierte remove_task() Funktion gerufen
    context.task_manager.remove_task(task_name)  # Erase task using task manager


@then('the task "{task_name}" does not exist in the list of tasks anymore')
def step_when_the_task_disappears_from_the_list(context, task_name):
    """Check that the erased task is not in the list of tasks anymore"""
    # liste aller tasks abrufen mit get_all_tasks() und
    tasks = context.task_manager.get_all_tasks()  # Retrieve all tasks
    # mit assert überprüfen ob ein task mit Namen “task_name” existiert

    try:

        context.task_manager.get_task_by_name(task_name)

        assert (
            False
        ), f"Task with name '{task_name}' should not exist, but it was found."

    except KeyError:
        # Task does not exist, which is the expected behavior
        pass
