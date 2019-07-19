from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Category model class
    """
    name = models.CharField(max_length=250)

    def save_category(self):
        self.save()

class Location(models.Model):
    """
    Location model class
    """
    name = models.CharField(max_length=250)

    def save_location(self):
        self.save()

class Image(models.Model):
    """
    Image model class
    """
    image_url = models.ImageField(max_length = 250)
    name = models.CharField(max_length = 250 )
    description = models.CharField(max_length = 250)
    location = models.ForeignKey(Location , default = 1)
    category = models.ForeignKey(Category , default = 1)
    # date = models.DateTimeField(auto_now_add = True)

    def save_image(self):
        self.save()