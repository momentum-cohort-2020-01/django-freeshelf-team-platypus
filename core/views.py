from django.shortcuts import render

from .models import Book, Category


def book_list(request):
    books = Book.objects.all()
    context = {'books': books, 'request': request}
    return render(request, 'core/book_list.html', context=context)


def sort_list(request, option):
    books = Book.objects.all()
    books = sort_by(books, option)
    context = {'books': books, 'request': request}
    return render(request, 'core/book_list.html', context=context)


def cat_list(request, cat):
    category = Category.objects.get(slug=cat)
    books = Book.objects.filter(category=category)
    context = {'books': books, 'request': request}
    return render(request, 'core/book_list.html', context=context)


def sort_cat_list(request, cat, option):
    category = Category.objects.get(slug=cat)
    books = Book.objects.filter(category=category)
    if option == 'created_at_reverse':
        option = '-created_at'
    books = sort_by(books, option)
    context = {'books': books, 'request': request}
    return render(request, 'core/book_list.html', context=context)


def sort_by(queryset, option):
    return queryset.order_by(option)
