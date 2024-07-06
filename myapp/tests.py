# myapp/tests.py

from django.test import TestCase
from django.urls import reverse
from myapp.models import MyModel
#rom myapp.utils import calculate_temperature

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name='Test', city='New York', temperature=15)

    def test_model_creation(self):
        obj = MyModel.objects.get(name='Test')
        self.assertEqual(obj.city, 'New York')
        self.assertEqual(obj.temperature, 15)



class ViewsTestCase(TestCase):
    def test_hello_view(self):
        url = reverse('hello-view')
        response = self.client.get(url, {'visitor_name': 'Mark'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('greeting', response.json())
        self.assertIn('Mark', response.json()['greeting'])

# Add more tests for forms, views, etc. as needed

