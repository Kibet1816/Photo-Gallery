from django.shortcuts import render
from .models import Image

# Create your views here.


def index(request):
    """
    View function to render the landing page
    """
    return render(request, 'index.html')


def categories(request):
    """
    Function to render categories page
    """
    images = Image.display_image()
    return render(request, 'all-photos/categories.html', {"images": images})


def travel(request):
    """
    """
    images = Image.display_image()
    return render(request, 'all-photos/travel.html', {"images": images})


def food(request):
    """
    """
    images = Image.display_image()
    return render(request, 'all-photos/food.html', {"images": images})


def sport(request):
    """
    """
    images = Image.display_image()
    return render(request, 'all-photos/sport.html', {"images": images})


def animals(request):
    """
    """
    images = Image.display_image()
    return render(request, 'all-photos/animals.html', {"images": images})


def architecture(request):
    """
    """
    images = Image.display_image()
    return render(request, 'all-photos/architecturel.html', {"images": images})


def landscapes(request):
    """
    """
    images = Image.display_image()
    return render(request, 'all-photos/landscapes.html', {"images": images})
