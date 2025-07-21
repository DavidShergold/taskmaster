from django.test import TestCase
from .models import Task  # Assuming you have a Task model in models.py

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task.",
            completed=False
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")
        self.assertFalse(self.task.completed)

    def test_string_representation(self):
        self.assertEqual(str(self.task), self.task.title)  # Assuming __str__ method returns title

    def test_task_completion(self):
        self.task.completed = True
        self.task.save()
        self.assertTrue(self.task.completed)