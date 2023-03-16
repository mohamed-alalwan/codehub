from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('question/index', views.question_index, name='question_index'),
    path('question/create/', views.CreateQuestion.as_view() , name='create_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='update_question'),
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete')
]