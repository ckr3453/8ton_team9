from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'min1/home.html')

def index(request):
    return render(request, 'min1/index.html')    

def write(request):
    return render(request, 'min1/write.html')

def detail(request):
    return render(request, 'min1/detail.html')