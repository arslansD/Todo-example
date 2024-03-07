from django.test import TestCase

from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='Test',
            body='Test body'
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'Test')
        self.assertEqual(self.todo.body, 'Test body')
        self.assertEqual(str(self.todo), 'Test')
