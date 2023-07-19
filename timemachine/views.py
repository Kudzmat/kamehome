from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.models import UserProfile
from .forms import CharacterForm
from .models import TimelineStory
from .functions import light_scenario, dark_scenario
import uuid


# the landing page for the time machine
@login_required
def get_ready(request):
    form = CharacterForm()

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        option = request.POST.get('choice')
        return redirect('time_machine:time_travel', option=option)

    context = {'form': form}

    return render(request, 'timemachine/ready.html', context=context)


@login_required
def time_travel(request, option):

    user_profile = UserProfile.objects.get(user=request.user)  # get the current user's UserProfile

    if option == 'Something light hearted':

        # get story content and description using function
        content, title = light_scenario()

        # create slug which will create a unique string for each story
        slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())

        new_story = TimelineStory(author=user_profile, description=content, dragon_title=title, slug=slug)
        new_story.save()

    else:
        # get story content and description using function
        content, title = dark_scenario()

        # create slug which will create a unique string for each story
        slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())

        new_story = TimelineStory(author=user_profile, description=content, dragon_title=title, slug=slug)
        new_story.save()

    context = {'content': content}

    return render(request, 'timemachine/scenario.html', context=context)

