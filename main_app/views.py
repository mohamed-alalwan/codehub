
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Question, Category, Answer, Reply
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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
    return render(request,'answer/answer_index.html', {'answers': answers})

def answer_detail(request, answer_id):
    answer= Answer.objects.get(id=answer_id)
    
    return render(request, 'answer/answer_detail.html', {
        'answer': answer,
        
        })


class CreateAnswer(CreateView):
    model= Answer
    fields = '__all__'
    

class AnswerUpdate(UpdateView):
    model = Answer
    fields = '__all__'

class AnswerDelete(DeleteView):
    model = Answer
    success_url = '/answer/'



# =======================Reply Section========================

def reply_index(request):
    replies = Reply.objects.all()
    return render(request,'reply/reply_index.html', {'replies': replies})

def reply_detail(request, reply_id):
    reply = Reply.objects.get(id=reply_id)
    
    return render(request, 'reply/reply_detail.html', {
        'reply': reply,
        
        })


class CreateReply(CreateView):
    model= Reply
    fields = '__all__'
    

class ReplyUpdate(UpdateView):
    model = Reply
    fields = '__all__'

class ReplyDelete(DeleteView):
    model = Reply
    success_url = '/reply/'


# =======================Sign Up Section========================
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # Make a 'user' form object with the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save user to DB
            user = form.save()
            # Log in the user automatically once they sign up
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid: Please Try Again!'
    # If there's a bad post or get request
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
