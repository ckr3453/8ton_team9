from django.contrib import admin
from django.urls import path
import app.views, userapp.views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('detail/', views.detail, name='detail'),
    path('login/', userapp.views.login, name="login"),
    path('register/', userapp.views.Register.as_view(), name="register"),
    path('logout/', userapp.views.logout, name="logout"),
]
