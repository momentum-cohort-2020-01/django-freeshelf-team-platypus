from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=100, help_text='Title of the book')
    author = models.CharField(max_length=100, help_text='Author of the book')
    description = models.TextField(help_text='Description of the book')
    url = models.URLField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
