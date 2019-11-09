from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import View

from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request, 'base.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.POST['password'] == request.POST['password_verify']:
            try:
                if not User.objects.filter(email=request.POST['email']):
                    user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                    auth.login(request, user)
                else:
                    raise Exception
            except Exception:
                return render(request, 'register.html')
            return redirect('index')
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': '아이디 혹은 패스워드가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'base.html')
    return render(request, 'base.html')