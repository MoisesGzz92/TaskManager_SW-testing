# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import unittest
from taskmanager.app.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """
    Unit tests for the TaskManager class.
    """

    def setUp(self):
        """Set up a TaskManager instance for testing."""
        self.task_manager = TaskManager()

    # Valid test cases
    def test_add_task_valid(self):
        """Test adding a valid task."""
        self.task_manager.add_task("Task 1", "Description 1")
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_add_task_valid_empty_description(self):
        """Test adding a task with an empty description."""
        self.task_manager.add_task("Task 1", "")
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when the dictionary is empty."""
        self.assertEqual(self.task_manager.get_all_tasks(), {})

    def test_get_task_by_name_valid(self):
        """Test getting a task by name that exists."""
        self.task_manager.add_task("Task 1", "Description 1")
        task = self.task_manager.get_task_by_name("Task 1")
        self.assertEqual(task["Task 1"]["description"], "Description 1")

    def test_remove_task_valid(self):
        """Test removing a task that exists."""
        self.task_manager.add_task("Task 1", "Description 1")
        self.task_manager.remove_task("Task 1")
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_update_task_valid(self):
        """Test updating an existing task."""
        self.task_manager.add_task("Task 1", "Description 1")
        updated = self.task_manager.update_task(
            "Task 1",
            new_task_name="Updated Task 1",
            new_task_description="Updated Description",
        )
        self.assertTrue(updated)
        task = self.task_manager.get_task_by_name("Updated Task 1")
        self.assertEqual(task["Updated Task 1"]["description"], "Updated Description")

    def test_clear_tasks(self):
        """Test clearing all tasks."""
        self.task_manager.add_task("Task 1", "Description 1")
        self.task_manager.clear_tasks()
        self.assertEqual(len(self.task_manager.tasks), 0)

    # Invalid test cases
    def test_add_task_invalid_empty_name(self):
        """Test adding a task with an empty name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task("", "Description 1")
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_add_task_invalid_none_name(self):
        """Test adding a task with None as name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task(None, "Description 1")
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_add_task_invalid_name_length(self):
        """Test adding a task with a name longer than 255 characters."""
        long_name = "A" * 256
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task(long_name, "Description 1")
        self.assertEqual(
            str(context.exception), "Name or description cannot be longer than 255 characters"
        )

    def test_add_task_invalid_description_length(self):
        """Test adding a task with a description longer than 255 characters."""
        long_description = "A" * 256
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task("Task 1", long_description)
        self.assertEqual(
            str(context.exception), "Name or description cannot be longer than 255 characters"
        )

    def test_get_task_by_name_invalid_empty_name(self):
        """Test getting a task by an empty name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.get_task_by_name("")
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_get_task_by_name_invalid_none_name(self):
        """Test getting a task by None as name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.get_task_by_name(None)
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_get_task_by_name_invalid_non_existing(self):
        """Test getting a task by a name that does not exist."""
        with self.assertRaises(KeyError) as context:
            self.task_manager.get_task_by_name("Non-existing Task")
        self.assertEqual(
            str(context.exception), "\"Task with name 'Non-existing Task' not found.\""
        )

    def test_remove_task_invalid_empty_name(self):
        """Test removing a task with an empty name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.remove_task("")
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_remove_task_invalid_none_name(self):
        """Test removing a task with None as name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.remove_task(None)
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_remove_task_invalid_non_existing(self):
        """Test removing a task that does not exist."""
        with self.assertRaises(KeyError) as context:
            self.task_manager.remove_task("Non-existing Task")
        self.assertEqual(
            str(context.exception), "\"Task with name 'Non-existing Task' not found.\""
        )

    def test_update_task_invalid_empty_name(self):
        """Test updating a task with an empty name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.update_task("", new_task_name="Updated Task 1")
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_update_task_invalid_none_name(self):
        """Test updating a task with None as name."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.update_task(None, new_task_name="Updated Task 1")
        self.assertEqual(str(context.exception), "Name cannot be empty")

    def test_update_task_invalid_empty_new_name(self):
        """Test updating a task with an empty new name."""
        self.task_manager.add_task("Task 1", "Description 1")
        with self.assertRaises(ValueError) as context:
            self.task_manager.update_task(
                "Task 1", new_task_name="", new_task_description="Updated Description"
            )
        self.assertEqual(str(context.exception), "New Name is required")

    def test_update_task_invalid_non_existing(self):
        """Test updating a task that does not exist."""
        with self.assertRaises(KeyError) as context:
            self.task_manager.update_task(
                "Non-existing Task",
                new_task_name="Updated Task",
                new_task_description="Updated Description",
            )
        self.assertEqual(
            str(context.exception), "\"Task with name 'Non-existing Task' not found.\""
        )


if __name__ == "__main__":
    unittest.main()
