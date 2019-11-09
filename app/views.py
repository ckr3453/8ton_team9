from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Count, Q
from userapp.views import login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.http import HttpResponse, HttpResponseRedirect
import json
import pdb


def home(request):
    return render(request, 'home.html')
 

def index(request):
    if request.method == "POST":
        area= request.POST.get('area')
        return render(request,'app/write.html', {'area':area})
    return render(request, 'index.html')    

def write(request):
    user = request.user
    if user.is_anonymous:
        return redirect('login')
    return render(request, 'app/write.html')


def postcreate(request):
    if request.method == "POST":
        user = request.user
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        dday = request.POST.get('dday')
        post = Post.objects.create(user = user, category = category, title = title, content = content, image = image, dday = dday)    
        return redirect('app:all_posts')



def post_like(request, post_id):
   user = request.user
   if user.is_anonymous:
       return redirect('login')
   post = get_object_or_404(Post, pk=post_id)
   is_like = user in post.likes.all()
   if is_like:
       post.likes.remove(user)
       if not post.likes_count == 0:
           post.likes_count -= 1
           post.save()
       message = "like_cancel"
   else:
       post.likes.add(user)
       post.likes_count += 1
       post.save()
       message = "like"
   context = {
              'message': message,
              'likes_count': post.likes_count,
              }
   return HttpResponse(json.dumps(context), content_type="application/json")


def all_posts(request):
    all_posts = Post.objects.all()
    return render(request,'app/all_posts.html', {'all_posts':all_posts})
