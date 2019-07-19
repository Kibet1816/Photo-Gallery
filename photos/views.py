from django.shortcuts import render

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
    return render(request,'all-photos/categories.html')

def location(request):
    """
    Function to render location file
    """
    return render(request,'all-photos/location.html')