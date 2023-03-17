
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Question, Category, Answer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm


# =======================Category Section========================



def home(request):
    categories = Category.objects.all()
    return render(request,'home.html', {'categories': categories})

def about(request):
    return render(request,'about.html')


# =======================Qustion Section========================


def question_index(request):
    questions = Question.objects.all()
    return render(request,'question/question_index.html', {'questions': questions})

def question_detail(request, question_id):
    question= Question.objects.get(id=question_id)
    
    return render(request, 'question/question_detail.html', {
        'question': question,
        
        })


class CreateQuestion(CreateView):
    model= Question
    fields = '__all__'
    

class QuestionUpdate(UpdateView):
    model = Question
    fields = '__all__'

class QuestionDelete(DeleteView):
    model = Question
    success_url = '/question/'




# =======================Answer Section========================

def answer_index(request):
    answers = Answer.objects.all()
    return render(request,'question/question_index.html', {'answers': answers})


class CreateAnswer(CreateView):
    model= Answer
    fields = '__all__'
    

class AnswerUpdate(UpdateView):
    model = Answer
    fields = '__all__'

class AnswerDelete(DeleteView):
    model = Answer
    


# =======================Sign Up Section========================
def signup(request):
    if request.method == 'POST':
        # Make a 'user' form object with the data from the browser
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save user to DB
            user = form.save()
            # Log in the user automatically once they sign up
            login(request, user)
            messages.success(request,f"Account was successfully created! Welcome {user.username}!")
            return redirect('home')
        
    # If there's a bad post or get request
    formSecond = SignUpForm()
    try:
        formSecond.errors.update(form.errors)
    except Exception as e:
        print(e)
    context = {'form': formSecond}
    return render(request, 'registration/signup.html', context)
