from django.contrib import admin
from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('write/',views.write, name = "write"),
    path('postcreate/', views.postcreate, name = "postcreate"),
    path('post_like/<int:post_id>/', views.post_like, name="post_like"),
    path('all_posts/', views.all_posts, name = "all_posts"),
    path('area_posts/', views.area_posts, name = "area_posts"),

]