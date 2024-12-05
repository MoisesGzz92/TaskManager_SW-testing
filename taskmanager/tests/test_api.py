# GNU General Public License v3.0
# Copyright (C) 2024 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.

import unittest
from taskmanager.app.api import app
from taskmanager.app.task_manager import TaskManager


class APITestCase(unittest.TestCase):
    """
    Unit tests for the TaskManager API.
    """

    @classmethod
    def setUpClass(cls):
        """Set up the Flask application for testing."""
        cls.app = app.test_client()
        cls.app.testing = True
        cls.task_manager = TaskManager()

    def add_task(self, name, description):
        """Helper method to add a task."""
        return self.app.post("/task", json={"name": name, "description": description})

    def delete_task(self, name):
        """Helper method to delete a task."""
        return self.app.delete(f"/task/{name}")

    def update_task(self, name, new_name, new_description):
        """Helper method to update a task."""
        return self.app.put(
            f"/task/{name}", json={"name": new_name, "description": new_description}
        )

    def test_add_task_valid(self):
        """Test adding a valid task."""
        response = self.add_task("Task 1", "Description 1")
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Task created successfully", response.data)

    def test_add_task_invalid_empty_name(self):
        """Test adding a task with an empty name."""
        response = self.add_task("", "Description 1")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Name is required", response.data)

    def test_add_task_invalid_none_name(self):
        """Test adding a task with None as name."""
        response = self.add_task(None, "Description 1")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Name is required", response.data)

    def test_remove_task_valid(self):
        """Test removing an existing task."""
        self.add_task("Task 1", "Description 1")
        response = self.delete_task("Task 1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task deleted successfully", response.data)

    def test_remove_task_invalid_non_existing(self):
        """Test removing a task that does not exist."""
        response = self.delete_task("Non-existing Task")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Task not found", response.data)

    def test_update_task_valid(self):
        """Test updating an existing task."""
        self.add_task("Task 1", "Description 1")
        response = self.update_task("Task 1", "Updated Task", "Updated Description")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task updated successfully", response.data)

    def test_update_task_invalid_non_existing(self):
        """Test updating a task that does not exist."""
        response = self.update_task("Non-existing Task", "Updated Task", "Updated Description")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Task with name 'Non-existing Task' not found.", response.data)

    def test_update_task_invalid_empty_new_name(self):
        """Test updating a task with an empty new name."""
        self.add_task("Task 1", "Description 1")
        response = self.update_task("Task 1", "", "Updated Description")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"New Name is required", response.data)

    def test_clear_tasks(self):
        """Test clearing all tasks."""
        self.add_task("Task 1", "Description 1")
        response = self.app.delete("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"All tasks were deleted succesfully", response.data)

    def test_clear_tasks_no_tasks(self):
        """Test clearing tasks when no tasks exist."""
        response = self.app.delete("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"All tasks were deleted succesfully", response.data)

    def test_add_task_invalid_description_length(self):
        """Test adding a task with a description longer than 255 characters."""
        long_description = "A" * 256
        response = self.add_task("Task 1", long_description)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Name or description cannot be longer than 255 characters", response.data)

    def test_update_task_invalid_description_length(self):
        """Test updating a task with a description longer than 255 characters."""
        self.add_task("Task 1", "Description 1")
        long_description = "A" * 256
        response = self.update_task("Task 1", "Task 1", long_description)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b"New Name or description cannot be longer than 255 characters", response.data
        )


if __name__ == "__main__":
    unittest.main()
