from .models import Books
from django.forms import ModelForm, TextInput


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ["Book_name", "author"]
        widgets = {
            "Book_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название книги'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'автор'
            }),

        }
