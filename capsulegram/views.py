from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CapsuleGram


# show all capsule gram posts
class CapsulePosts(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    model = CapsuleGram
    template_name = 'capsulegram/gram_page.html'
    queryset = CapsuleGram.objects.order_by('-upload_date')  # dash is to order by descending order


# for uploading an image to capsule gram
class UploadPic(LoginRequiredMixin, CreateView):
    model = CapsuleGram
    template_name = 'capsulegram/upload.html'
    fields = ('image', 'caption')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = self.request.user  # set the owner of the post to the current logged in user
        post.save()

        return HttpResponseRedirect(reverse('index'))  # take to gram home page after uploading
