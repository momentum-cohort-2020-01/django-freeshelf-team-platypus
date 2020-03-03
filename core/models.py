from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    name = models.CharField(
        max_length=64, help_text="The programming language a book covers")
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Book(models.Model):

    title = models.CharField(max_length=100, help_text='Title of the book')
    author = models.CharField(max_length=100, help_text='Author of the book')
    description = models.TextField(help_text='Description of the book')
    url = models.URLField(max_length=256)
    category = models.ManyToManyField(
        Category, related_name='category', help_text="Choose a programming language this book covers")
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.user.username}, Book PK: {self.book.pk}'
