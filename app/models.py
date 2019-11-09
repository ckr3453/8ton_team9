from django.db.models import *
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimeStampedModel(Model):
    create_at = DateTimeField(auto_now_add = True)
    updated_at = DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    user = ForeignKey(User, on_delete = CASCADE)
    category = CharField(max_length = 100)
    area = CharField(max_length = 100, default = "강남구")
    title = CharField(max_length = 100)
    content = TextField()
    likes_count = IntegerField(default = 0)
    star_rating = IntegerField(default = 0)
    image = ImageField(upload_to = "img/")
    likes = ManyToManyField(User, related_name = "liked_users")
    dday = DateTimeField()


    def __str__(self):
        return self.title

    def Starzips(self):
        return Starzip.objects.filter(post = self)    



class Starzip(TimeStampedModel):
    post = ForeignKey(Post, on_delete = CASCADE)
    star_rating = IntegerField(default=0)

    def __str__(self):
        return self.star_rating


