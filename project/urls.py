from django.contrib import admin
from django.urls import path, include
import app.views, userapp.views
from app import urls as app_urls
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index, name='index'),
    path('app/', include(app_urls)),
    path('login/', userapp.views.login, name="login"),
    path('register/', userapp.views.Register.as_view(), name="register"),
    path('logout/', userapp.views.logout, name="logout"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

