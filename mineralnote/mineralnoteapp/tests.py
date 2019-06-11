from django.test import TestCase
from .models import Product, ProductType, Review

# Create your tests here.

class ProductTypeTest(TestCase):
   def test_string(self):
       type=ProductType(typename="Selenium")
       self.assertEqual(str(type), type.typename)

   def test_table(self):
       self.assertEqual(str(ProductType._meta.db_table), 'Selenium')

class ProductTest(TestCase):
   #set up one time sample data
   def setup(self):
       type = ProductType(typename='mineral')
       product=Product(productname='citrine', producttype=type, productprice='500.00')
       return product
   def test_string(self):
       prod = self.setup()
       self.assertEqual(str(prod), prod.productname)
  
   #test the discount property
   def test_discount(self):
       prod=self.setup()
       self.assertEqual(prod.memberdiscount(), 25.00)

   def test_type(self):
       prod=self.setup()
       self.assertEqual(str(prod.producttype), 'amethist')

   def test_table(self):
       self.assertEqual(str(Product._meta.db_table), 'product')