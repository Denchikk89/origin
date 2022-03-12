from django.shortcuts import render
from.models import Books


def index(request):
    book = Books.objects.all()
    return render(request, 'main/index.html', {'book':book})


def about(request):
    return render(request, 'main/abot.html')


def base(request):
    return render(request, 'main/base.html')