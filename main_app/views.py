
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Question, Category, Answer, Reply, Profile, Badge
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import SignUpForm, UpdateProfileForm, UpdateUserForm
from django.contrib.messages.views import SuccessMessageMixin



# =======================Category Section========================

def home(request):
    categories = Category.objects.all()
    questions = None
    for category in categories:
        if(questions is None):
            questions = Question.objects.filter(category=category).order_by('-date')[:3]
        else:
            questions |= Question.objects.filter(category=category).order_by('-date')[:3]

    return render(request,'home.html', {'categories': categories, 'questions': questions})

def about(request):
    return render(request,'about.html')


# =======================Qustion Section========================
@login_required
def question_index(request):
    questions = Question.objects.all()
    return render(request,'question/question_index.html', {'questions': questions})

@login_required
def question_detail(request, question_id):
    question= Question.objects.get(id=question_id)
    
    return render(request, 'question/question_detail.html', {
        'question': question,
        
        })


class CreateQuestion(LoginRequiredMixin,CreateView):
    model= Question
    fields = ['title', 'body', 'category']
    def form_valid(self, form) :
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = '__all__'

class QuestionDelete(LoginRequiredMixin , DeleteView):
    model = Question
    success_url = '/question/'


# =======================Answer Section========================
@login_required
def answer_index(request):
    answers = Answer.objects.all()
    return render(request,'answer/answer_index.html', {'answers': answers})

@login_required
def answer_detail(request, answer_id):
    answer= Answer.objects.get(id=answer_id)
    
    return render(request, 'answer/answer_detail.html', {
        'answer': answer,
        
        })


class CreateAnswer(LoginRequiredMixin,CreateView):
    model= Answer
    fields = '__all__'
    

class AnswerUpdate(LoginRequiredMixin,UpdateView):
    model = Answer
    fields = '__all__'

class AnswerDelete(LoginRequiredMixin,DeleteView):
    model = Answer
    success_url = '/answer/'


# =======================Reply Section========================

@login_required
def reply_index(request):
    replies = Reply.objects.all()
    return render(request,'reply/reply_index.html', {'replies': replies})

@login_required
def reply_detail(request, reply_id):
    reply = Reply.objects.get(id=reply_id)
    
    return render(request, 'reply/reply_detail.html', {
        'reply': reply,
        
        })


class CreateReply(LoginRequiredMixin,CreateView):
    model= Reply
    fields = '__all__'
    

class ReplyUpdate(LoginRequiredMixin,UpdateView):
    model = Reply
    fields = '__all__'

class ReplyDelete(LoginRequiredMixin,DeleteView):
    model = Reply
    success_url = '/reply/'


# =======================Auth Section========================


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

def change_password(request):
    if request.method == 'POST':
        # Make a 'user' form object with the data from the browser
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            login(request, request.user)
            messages.success(request,"Your password has been changed successfully!")
            return redirect('home')
        
    # If there's a bad post or get request
    formSecond = PasswordChangeForm(request.user)
    try:
        formSecond.errors.update(form.errors)
    except Exception as e:
        print(e)
    context = {'form': formSecond}
    return render(request, 'registration/change_password.html', context)



# =======================Profile Section========================
@login_required
def profile_index(request):
    profile = Profile.objects.get(user = request.user)
    badges_profile_doesnt_have = Badge.objects.exclude(id__in = profile.badges.all().values_list('id'))
    return render(request, 'profile/index.html', {'badges' : badges_profile_doesnt_have} )

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile_index')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile/update.html', {'user_form': user_form, 'profile_form': profile_form})

# =======================Category Section========================
@login_required
def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    questions = Question.objects.filter(category=category).order_by('-date')
    return render(request, 'category/detail.html', {'category': category, 'questions': questions})

class BadgeList(ListView):
    model = Badge

class BadgeDetail(DetailView):
    model = Badge

class BadgeCreate(CreateView):
    model = Badge
    fields = '__all__'

class BadgeUpdate(UpdateView):
    model = Badge
    fields = '__all__'


class BadgeDelete(DeleteView):
    model = Badge
    success_url = '/profile/'

@login_required
def add_badge(request, profile_id, badge_id):
    Profile.objects.get(id=profile_id).badges.add(badge_id)
    return redirect('/profile/')

@login_required
def remove_badge(request, profile_id, badge_id):
    Profile.objects.get(id=profile_id).badges.remove(badge_id)
    return redirect('/profile/')