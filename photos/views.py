from django.shortcuts import render
from .models import Image

# Create your views here.

def index(request):
    """
    View function to render the landing page
    """
    return render (request,'index.html')

def categories(request):
    """
    Function to render categories page
    """
    images = Image.display_image()
    return render(request,'all-photos/categories.html',{"images":images})

def location(request):
    """
    Function to render location file
    """
    images = Image.display_image()
    return render(request,'all-photos/location.html',{"images":images})