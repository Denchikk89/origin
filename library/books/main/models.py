from django.db import models


class Books(models.Model):
    Book_name = models.CharField('Название книги', max_length=150)
    author = models.CharField('Автор', max_length=150)

    def __str__(self):
        return self.Book_name
