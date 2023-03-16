from django.db import models
from django.urls import reverse

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('question_index')


class Answer(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    date = models.DateField()


class Reply(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    date = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class Profile(models.Model):
    points = models.IntegerField()


class Badges(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField()
    point_limit =models.IntegerField()