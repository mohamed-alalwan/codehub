from django.urls import path
from . import views
urlpatterns = [
    # Catrgory Urls
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Question Urls
    path('question/', views.question_index, name='question_index'),
    path('question/create/', views.CreateQuestion.as_view() , name='create_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='update_question'),
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),

    # Answer Urls
    path('answer/', views.answer_index, name="answer_index"),
    path('answer/create', views.CreateAnswer.as_view(), name='create_answer'),
    path('answer/<int:answer_id>/', views.answer_detail, name="answer_detail"),
    path('answer/<int:pk>/update/', views.AnswerUpdate.as_view(), name="answer_update"),
    path('answer/<int:pk>/delete/', views.AnswerDelete.as_view(), name="answer_delete"),
   
    # Reply Urls
    path('reply/', views.reply_index, name="reply_index"),
    path('reply/create', views.CreateReply.as_view(), name="create_reply"),
    path('reply/<int:reply_id>', views.reply_detail, name="reply_detail"),
    path('reply/<int:pk>/update/', views.ReplyUpdate.as_view(), name="reply_update"),
    path('reply/<int:pk>/delete/', views.ReplyDelete.as_view(), name="reply_delete"),

    # Auth Urls
    path('signup/', views.signup, name='signup'),
    
    # Profile Urls
    path('profile/', views.profile_index, name='profile_index'),
    path('profile/update', views.profile_update, name='profile_update'),

    # Category Urls
    path('category/<int:category_id>', views.category_detail, name='category_detail'),
]