from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestClass(TestCase):
    """
    Test class for image module
    """

    def setUp(self):
        """
        Method to create an instance of the image before each test
        """


    # def test_instance(self):
    #     """
    #     Test method to check for correct instantiation
    #     """
    #     self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        """
        Test method for save method
        """


class CategoryTestClass(TestCase):
    """
    Test class for category module
    """
    def setUp(self):
        """
        Method to create an instance of the image before each test
        """
        self.new_category = Category(name = 'Travel')

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.new_category,Category))

    def test_save_method(self):
        """
        Test method for save method
        """
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

class LocationTestClass(TestCase):
    """
    Test class for location module
    """
    def setUp(self):
        """
        Method to create an instance of the image before each test
        """
        self.new_location = Location(name = 'Kite')

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)