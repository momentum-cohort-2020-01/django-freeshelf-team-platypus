from django.shortcuts import render

from .models import Book, Category


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'core/book_list.html', context=context)


def cat_list(request, cat):
    category = Category.objects.get(slug=cat)
    books = Book.objects.filter(category=category)
    context = {'books': books}
    return render(request, 'core/book_list.html', context=context)
