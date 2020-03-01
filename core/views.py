from django.shortcuts import render

from .models import Book, Category


def book_list(request):
    sort_option = request.GET.get('sort', 'date')
    books = Book.objects.all()
    books = sort_by(books, sort_option)
    context = {'books': books, 'request': request}
    return render(request, 'core/book_list.html', context=context)


def cat_list(request, cat):
    sort_option = request.GET.get('sort', 'date')
    category = Category.objects.get(slug=cat)
    books = Book.objects.filter(category=category)
    books = sort_by(books, sort_option)
    context = {'books': books, 'request': request}
    return render(request, 'core/book_list.html', context=context)


def sort_by(queryset, option):
    options = {'date': 'created_at',
               'date-reverse': '-created_at',
               'author': 'author',
               'title': 'title'}
    return queryset.order_by(options[option])
