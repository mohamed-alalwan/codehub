from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Question

# Create your views here.
def home(request):
    return render(request, 'home.html')

def question_index(request):
    questions = Question.objects.all()
    return render(request,'question/question_index.html', {'questions': questions})

def question_detail(request, question_id):
    question= Question.objects.get(id=question_id)
    
    return render(request, 'question/question_detail.html', {
        'question': question,
        
        })




# =======================Classes========================

class CreateQuestion(CreateView):
    model= Question
    fields = '__all__'
    

class QuestionUpdate(UpdateView):
    model = Question
    fields = '__all__'

class QuestionDelete(DeleteView):
    model = Question
    success_url = '/question/index'

class QuestionDetail(DetailView):
    model = Question