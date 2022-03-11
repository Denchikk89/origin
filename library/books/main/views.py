from django.shortcuts import render
from.models import Books


def index(request):
    Book = Books.objects.all()
    return render(request, 'main/index.html', {'Books':Books})


def about(request):
    return render(request, 'main/abot.html')


def base(request):
    return render(request, 'main/base.html')