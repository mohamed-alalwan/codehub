from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=1000)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('question_index')


class Answer(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=1000)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('answer_index')


class Reply(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField(max_length=1000)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('reply_index')


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class Profile(models.Model):
    points = models.IntegerField()


class Badges(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField()
    point_limit =models.IntegerField()