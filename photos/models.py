from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Category model class
    """
    name = models.CharField(max_length=250)

    def save_category(self):
        self.save()

    @classmethod
    def display_img_by_category(cls):
        img_cat = cls.objects.all()

        return img_cat

class Location(models.Model):
    """
    Location model class
    """
    image = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img

class Image(models.Model):
    """
    Image model class
    """
    image = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )
    image_url = models.CharField(max_length = 250,default = 'image.jpg')

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img

class Architecture(models.Model):
    """
    Architecture model class
    """
    architecture = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )
    image_url = models.CharField(max_length = 250,default = 'image.jpg')

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img

class Animals(models.Model):
    """
    Animals Model class
    """
    animal = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )
    image_url = models.CharField(max_length = 250,default = 'image.jpg')

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img

class Landscapes(models.Model):
    """
    Landscape model class
    """
    landscape = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )
    image_url = models.CharField(max_length = 250,default = 'image.jpg')

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img

class Sport(models.Model):
    """
    Sport model class
    """
    sport = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )
    image_url = models.CharField(max_length = 250,default = 'image.jpg')

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img

class Travel(models.Model):
    """
    Travel model class
    """
    travel = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )
    image_url = models.CharField(max_length = 250,default = 'image.jpg')

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img

class Food(models.Model):
    """
    Food model class
    """
    food = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )
    image_url = models.CharField(max_length = 250,default = 'image.jpg')

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img