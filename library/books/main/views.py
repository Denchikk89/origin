from django.shortcuts import render
from.models import Books
from.forms import BooksForm


def index(request):
    book = Books.objects.all()
    return render(request, 'main/index.html', {'book': book})


def about(request):
    return render(request, 'main/abot.html')


def base(request):
    return render(request, 'main/base.html'),


def create(request):
    form = BooksForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

