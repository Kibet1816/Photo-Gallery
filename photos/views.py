from django.shortcuts import render
from .models import Image,Travel,Landscapes,Animals,Architecture,Food,Sport

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
    images = Travel.display_image()
    return render(request, 'all-photos/travel.html', {"images": images})


def food(request):
    """
    """
    images = Food.display_image()
    return render(request, 'all-photos/food.html', {"images": images})


def sport(request):
    """
    """
    images = Sport.display_image()
    return render(request, 'all-photos/sport.html', {"images": images})


def animals(request):
    """
    """
    animals = Animals.display_image()
    return render(request, 'all-photos/animals.html', {"animals": animals})


def architecture(request):
    """
    """
    images = Architecture.display_image()
    return render(request, 'all-photos/architecture.html', {"images": images})


def landscapes(request):
    """
    """
    images = Landscapes.display_image()
    return render(request, 'all-photos/landscapes.html', {"images": images})
