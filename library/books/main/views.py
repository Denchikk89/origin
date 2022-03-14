from django.shortcuts import render, redirect
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
    error = ''
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            error = 'написал хуйню'
    form = BooksForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

