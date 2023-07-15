from django.shortcuts import render, HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, 'index.html')
