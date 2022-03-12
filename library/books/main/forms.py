from .models import Books
from django.forms import ModelForm, TextInput


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ["Book_name", "author"]
