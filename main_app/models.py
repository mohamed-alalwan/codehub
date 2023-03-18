from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=1000)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('question_index')
    
    def __str__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=1000)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('answer_index')
    
    def __str__(self):
        return self.title


class Reply(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=1000)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('reply_index')
    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='main_app/static/images/profile/', blank=True)
    bio = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return str(self.user)

class Badges(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='main_app/static/images/badges/', blank=True)
    point_limit =models.IntegerField()

    def __str__(self):
        return self.name