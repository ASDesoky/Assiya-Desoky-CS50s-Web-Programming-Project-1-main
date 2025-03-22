from django.test import TestCase
from .models import MyModel

class MyModelTest(TestCase):
    def setUp(self):
        MyModel.objects.create(name="Sample Model", description="This is a sample description")
    
    def test_model_content(self):
        my_model = MyModel.objects.get(id=1)
        expected_object_name = f'{my_model.name}'
        self.assertEqual(expected_object_name, 'Sample Model')

