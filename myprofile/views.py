from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from login.forms import *
from .forms import *


# for a user to access their profile page
@login_required
def profile_page(request):
    context = {}
    return render(request, 'myprofile/profile.html', context=context)  # takes you to profile page


# to allow user to edit their profile information
@login_required
def edit_profile(request):
    current_user = request.user  # get the current logged in user
    form = UserProfileForm(instance=current_user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=current_user)

        if form.is_valid():
            form.save()
            form = UserProfileForm(instance=current_user)  # update info on page

    context = {'form': form}

    return render(request, 'myprofile/edit_profile.html', context=context)


# adding a profile picture to profile page
@login_required
def add_profile_pic(request):
    form = ProfilePicForm()
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)

        if form.is_valid():
            current_user = form.save(commit=False)
            current_user.user = request.user
            current_user.save()

            return HttpResponseRedirect(reverse('my_profile:profile'))  # go back to home page after updating pic

    context = {'form': form}

    return render(request, 'myprofile/profile_pic.html', context=context)


# changing/updating your profile picture
@login_required
def update_profile_pic(request):
    # this user already has a profile image so we need to access the instance of the user
    form = ProfilePicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        # replacing image
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user.user_profile)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('my_profile:profile'))  # return to profile page

    context = {'form': form}

    return render(request, 'myprofile/profile_pic.html', context=context)


@login_required
def change_password(request):
    current_user = request.user  # get the current logged in user
    changed = False
    form = PasswordChangeForm(current_user)  # django built-in

    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)

        if form.is_valid():
            form.save()
            changed = True

    context = {'form': form,
               'changed': changed
               }

    return render(request, 'myprofile/change_password.html', context=context)
