from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SuggestionBook, SuggestionCategory
from django.http import HttpResponse
from .models import Book, Category, Favorite
from django.contrib.auth.models import User


def book_list(request):
    sort_option = request.GET.get('sort', 'date')
    books = Book.objects.filter(approved=True)
    books = sort_by(books, sort_option)
    user = User.objects.get(username=request.user.username)
    context = {'favorites': get_user_fave_pks(user), 'books': books, 'request': request,
               'categories': Category.objects.all()}
    return render(request, 'core/book_list.html', context=context)


def cat_list(request, cat):
    sort_option = request.GET.get('sort', 'date')
    category = Category.objects.get(slug=cat)
    books = Book.objects.filter(category=category, approved=True)
    books = sort_by(books, sort_option)
    user = User.objects.get(username=request.user.username)
    context = {'favorites': get_user_fave_pks(user), 'books': books, 'request': request,
               'categories': Category.objects.all()}
    return render(request, 'core/book_list.html', context=context)


@login_required(login_url='/accounts/login/')
def favorite_list(request):
    sort_option = request.GET.get('sort', 'date')
    user = User.objects.get(username=request.user.username)
    favorites = Favorite.objects.filter(user=user)
    favorites = fave_sort_by(favorites, sort_option)
    books = [favorite.book for favorite in favorites]
    context = {'favorites': get_user_fave_pks(user), 'books': books, 'request': request,
               'categories': Category.objects.all()}
    return render(request, 'core/book_list.html', context=context)


@login_required(login_url='/accounts/login/')
def suggestion_list(request):
    sort_option = request.GET.get('sort', 'date')
    books = Book.objects.filter(approved=False)
    books = sort_by(books, sort_option)
    user = User.objects.get(username=request.user.username)
    context = {'favorites': get_user_fave_pks(user), 'books': books, 'request': request,
               'categories': Category.objects.all()}
    return render(request, 'core/book_list.html', context=context)


@login_required(login_url='/accounts/login/')
def book_suggestion(request):
    if request.method == "POST":
        form = SuggestionBook(request.POST)
        if form.is_valid():
            book = form.save()
        return redirect('book_list')
    else:
        form = SuggestionBook()
    return render(request, 'core/book_suggestion.html', {'form': form})


@login_required(login_url='/accounts/login/')
def favorite(request, pk):
    user = User.objects.get(username=request.user.username)
    book = Book.objects.get(pk=pk)
    is_fave = Favorite.objects.filter(user=user, book=book)
    if is_fave:
        is_fave[0].delete()
    else:
        fave_instance = Favorite(user=user, book=book)
        fave_instance.save()


def sort_by(queryset, option):
    options = {'date': 'created_at',
               'date-reverse': '-created_at',
               'author': 'author',
               'title': 'title'}
    return queryset.order_by(options[option])


def fave_sort_by(queryset, option):
    options = {'date': 'book__created_at',
               'date-reverse': '-book__created_at',
               'author': 'book__author',
               'title': 'book__title'}
    return queryset.order_by(options[option])


def get_user_fave_pks(user):
    fave_items = Favorite.objects.filter(user=user)
    return [fave.book.pk for fave in fave_items]
