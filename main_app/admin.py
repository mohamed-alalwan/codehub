from django.contrib import admin
from .models import Question, Category, Profile, Answer, Badges

# Register your models here.
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Answer)
admin.site.register(Badges)