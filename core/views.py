from django.shortcuts import render

from .models import Book


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'core/book_list.html', context=context)


def cat_list(request, cat):
    books = Book.objects.filter(category__name__iexact=cat)
    context = {'books': books}
    return render(request, 'core/book_list.html', context=context)
