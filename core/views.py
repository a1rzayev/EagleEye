from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def books(request):
    return render(request, 'book.html')