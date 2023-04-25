from unittest import skip
from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from store.models import *
from store.views import *


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name = 'django', slug = 'django')
        User.objects.create(username = 'admin')
        self.data1 = Product.objects.create(category_id = 1, title = 'django beginners', created_by_id = 1,
                                            slug = 'django-beginners', price = '20.00', image = 'django' )

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)  
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 400)   

    def test_product_detail_url(self):
        """
        Test products response status
        """
        response = self.c.get(reverse('store:product-detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)
  
    def test_category_detail_url(self):
        """
        Test categories response status
        """
        response = self.c.get(reverse('store:category-list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code valdiation
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertEqual(response.status_code, 200)
