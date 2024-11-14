# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

from behave import given, when, then

# handle to the task manager application
from taskmanager.app.task_manager import TaskManager


@given("the user is using the task manager application for getting all tasks")
def step_given_user_is_using_task_manager_application(context):
    """Set up the task manager application for the user."""
    context.task_manager = TaskManager()


@when("the user gets all tasks")
def step_when_user_gets_all_tasks(context):
    context.task_manager.get_all_tasks()


@then("the user should see all tasks")
def step_then_user_should_see_all_tasks(context):
    assert context.task_manager.get_all_tasks() == context.task_manager.tasks
