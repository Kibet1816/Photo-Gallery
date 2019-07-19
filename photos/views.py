from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View function to render the landing page
    """
    return render (request,'index.html')
