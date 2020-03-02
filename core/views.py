from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SuggestionBook, SuggestionCategory
from django.http import HttpResponse
from .models import Book, Category




def book_list(request):
    sort_option = request.GET.get('sort', 'date')
    books = Book.objects.all()
    books = sort_by(books, sort_option)
    context = {'books': books, 'request': request, 'categories': Category.objects.all()}
    return render(request, 'core/book_list.html', context=context)


def cat_list(request, cat):
    sort_option = request.GET.get('sort', 'date')
    category = Category.objects.get(slug=cat)
    books = Book.objects.filter(category=category)
    books = sort_by(books, sort_option)
    context = {'books': books, 'request': request, 'categories': Category.objects.all()}
    return render(request, 'core/book_list.html', context=context)

@login_required(login_url='/accounts/login/')
def book_suggestion(request):
    if request.method == "POST":
        form = SuggestionBook(request.POST)
        if form.is_valid():
            book = form.save()
            # book.save()
        return redirect('book_list')
    else:
        form = SuggestionBook()
    return render(request, 'core/book_suggestion.html', {'form': form})

def sort_by(queryset, option):
    options = {'date': 'created_at',
               'date-reverse': '-created_at',
               'author': 'author',
               'title': 'title'}
    return queryset.order_by(options[option])

def log_in(request):
    return render(request, 'core/log_in.html')
