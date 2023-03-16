from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'home.html')

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