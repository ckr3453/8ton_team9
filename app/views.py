<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'min1/home.html')

def index(request):
    return render(request, 'min1/index.html')    

def write(request):
    return render(request, 'min1/write.html')

def detail(request):
    return render(request, 'min1/detail.html')
=======
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'app/index.html')    
>>>>>>> b941d08daaaec027193a711294aee4416f57b535
