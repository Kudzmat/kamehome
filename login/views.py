from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *


# signing up for a Kame House account
def sign_up(request):
    form = SignupForm()
    registered = False

    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True  # a message will pop up to let the user know that their registration was a success

    context = {
        'form': form,
        'registered': registered
    }

    return render(request, 'login/signup.html', context=context)


# When a user wants to login to their account
def login_user(request):
    form = AuthenticationForm()  # this form comes built in with django

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # authenticating
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # making sure the entries match what's in our
            # database
            # logging in
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))  # redirect to homepage after a user is logged in

    context = {'form': form}

    return render(request, 'login/login.html', context=context)


# when a user decides to logout
@login_required  # this decorator ensures that a user must be logged in to access this function
def logout_user(request):
    logout(request)  # logout comes built in with django
    return HttpResponseRedirect(reverse('login:login'))  # takes you back to login page after logging out



