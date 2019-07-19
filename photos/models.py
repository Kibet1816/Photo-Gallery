from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Category model class
    """
    name = models.CharField(max_length=250)

class Location(models.Model):
    """
    Location model class
    """
    name = models.CharField(max_length=250)

class Image(models.Model):
    """
    Image model class
    """
    image_url = models.ImageField(max_length = 250)
    name = models.CharField(max_length = 250 )
    description = models.CharField(max_length = 250)
    location = models.ForeignKey(Location , default = 1)
    category = models.ForeignKey(Category , default = 1)
    date = models.DateTimeField(auto_now_add = True)