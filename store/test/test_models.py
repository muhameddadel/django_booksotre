from django.test import TestCase
from store.models import *


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.detal = Category.objects.create(name = 'django', slug = 'django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.detal
        self.assertTrue(isinstance(data, Category))