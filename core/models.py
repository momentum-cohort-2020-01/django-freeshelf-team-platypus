from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(
        max_length=64, help_text="The programming language a book covers")

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=100, help_text='Title of the book')
    author = models.CharField(max_length=100, help_text='Author of the book')
    description = models.TextField(help_text='Description of the book')
    url = models.URLField(max_length=256)
    categrory = models.ManyToManyField(
        Category, related_name='category', help_text="Choose a programming language this book covers")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} by {self.author}"
