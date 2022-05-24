from django.shortcuts import render

# Create your views here.
def home(request):
    # Returning the landing page
    return render(request,'home.html',{})
def second(request):
    # Returning the second page
    return render(request,'second.html',{})
def third(request):
    # Returning the third page
    return render(request,'third.html',{})

