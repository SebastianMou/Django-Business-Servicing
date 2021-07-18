from django.contrib.auth.models import User
from django.test import TestCase
from Shop.models import Category, Product

class TestCategoriesModel(TestCase):

    def setup(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_models_entry(self):
        '''
        Test Category models data insertion/types/field attributes
        '''

        data = self.data1
        self.assertTrue(isinstance(data, Category))


    def test_category_models_entry(self):
        '''
        Test Category model default name
        '''
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
    def setup(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='sebastian')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginner', price='20.00', image='django')
        
    def test_products_models_entry(self):
        """
            Test product model data insertion/typefild attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')






