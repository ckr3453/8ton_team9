from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'app/index.html')    

def write(request):
    return render(request, 'app/write.html')    