from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.


class ImageTestClass(TestCase):
    """
    Test class for image module
    """

    def setUp(self):
        """
        Method to create an instance of the image before each test
        """
        self.kite = Location(name="Kitengela")
        self.kite.save_location()

        self.travel = Category(name='Travel')
        self.travel.save_category()

        self.new_image = Image(image_url='image.jpg', name='Gorgon',
                               description='Son of skrygon', location=self.kite, category=self.travel)
        self.new_image.save()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_method(self):
        """
        Test method for save method
        """
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_display_image(self):
        """
        Test method to get an image
        """
        this_image = Image.display_image()
        self.assertTrue(len(this_image)>0)


class CategoryTestClass(TestCase):
    """
    Test class for category module
    """

    def setUp(self):
        """
        Method to create an instance of the image before each test
        """
        self.new_category = Category(name='Travel')

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_method(self):
        """
        Test method for save method
        """
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_show_img_by_category(self):
        """
        Test method to show image based on its location
        """
        this_image1 = Category.display_img_by_category()
        self.assertTrue(len(this_image1)>0)


class LocationTestClass(TestCase):
    """
    Test class for location module
    """

    def setUp(self):
        """
        Method to create an instance of the image before each test
        """
        self.new_location = Location(name='Kite')

    def test_instance(self):
        """
        Test method to check for correct instantiation
        """
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_display_img_by_location(self):
        """
        Test method to display image by location
        """
        this_image2 = Location.display_img_by_location()
        self.assertTrue(len(this_image2)>0)
