"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app.views, userapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userapp.views.index, name='index'),
    path('login/', userapp.views.login, name="login"),
    path('register/', userapp.views.Register.as_view(), name="register"),
    path('logout/', userapp.views.logout, name="logout"),
    path('test/', app.views.test, name="test")
]
