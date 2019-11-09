<<<<<<< HEAD
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
    print(all_posts)
    return render(request,'app/all_posts.html', {'all_posts':all_posts})


def area_posts(request):
    if request.method == 'POST':
        area = request.POST.get('area')
        area_posts = Post.objects.filter(area = area)
        return render(request, 'app/area_posts.html', {'area_posts':area_posts})

# from google.cloud import language
# from google.cloud.language import enums, types
# from google_images_download import google_images_download
    

# def test(request):# User Authentication

#     def init_entities(text):
#     # Preprocessing: Encoding
#         if isinstance(text, six.binary_type):
#             text = text.decode('utf-8')

#         # Instantiates a plain text document.
#         document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

#         # Detects entities in the document
#         entities = client.analyze_entities(document).entities

#         if len(entities) == 0:
#             print("Keyword None\n Exit")
#             exit()
#         else:
#             print(entities[0].name)
#             return entities[0].name


#     ##### Google image downloade module #####
#     def download_images(query):
#         # Set arguments
#         arguments = {
#             "keywords": query,
#             "limit": 1,
#             "print_urls": True,
#             "size": "medium",
#             "output_directory": "C:/Users/david/Desktop/부엉이/teamproject/project/static/img", # 절대경로로 수정하세요.
#             "no_directory": True,
#         }
#         try:
#             # a = response.download(arguments)
#             # print(a)
#             # print(type(a))
#             # print(a[0].get(query))
#             # b = str(a[0].get(query))
#             # c = ''

#             # i = len(b) - 3
#             # while (b[i] != '\\'):
#             #     c += b[i]
#             #     i -= 1
#             # c = str(c)
            
#             # c = c[::-1]
#             a = response.download(arguments)
#             print(a)
#             print(type(a))
#             print(a[0].get(query))
#             b = str(a[0].get(query))
#             b=b[2:len(b)-2]
#             print(b)

#             return b

#         except FileNotFoundError:
#             arguments = {"keywords": query,
#                         "format": "jpg",
#                         "limit": 1,
#                         "print_urls": True,
#                         "size": "medium"
#                         }
#             try:
#                 response.download(arguments)
#             except:
#                 pass


#     #credential_path = "파일이름.json" , 절대경로로 수정하세요.
#     credential_path = "C:/Users/david/Desktop/부엉이/teamproject/app/handle8ton-a089bd5358fe.json"
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

#     # Instantiates Client
#     client = language.LanguageServiceClient()

#     # Instantiates downloader
#     response = google_images_download.googleimagesdownload()

#     # Analysing Entities in Text

#     #게시글 제목
#     text = '저희 동네 쓰레기장 건설에 반대합니다.'

#     # download_images(init_entities(str 변수입력))
#     c = download_images(init_entities(text))
#     c = str(c)
#     c = c.replace(r"\\","/")
#     print(c)
#     return render(request, 'app/test.html', {'photo_src' : c , 'title' : text})

