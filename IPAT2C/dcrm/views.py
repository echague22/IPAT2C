from django.shortcuts import render

# Create your views here.

def first(request):
    #WRITE HERE

    return render(request, 'home.html')

def register(request):

    return render(request, 'register.html')
