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
    name = models.CharField(max_length=250)

    def save_location(self):
        self.save()

    @classmethod
    def show_img_by_location(cls):
        img_loc = cls.objects.all()

        return img_loc

class Image(models.Model):
    """
    Image model class
    """
    image = models.ImageField(upload_to = 'images/',default = 'image.jpg')
    name = models.CharField(max_length = 250 )

    def save_image(self):
        self.save()

    @classmethod
    def display_image(cls):
        img = cls.objects.all()

        return img