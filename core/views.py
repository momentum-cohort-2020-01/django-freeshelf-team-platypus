from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SuggestionForm
from django.http import HttpResponse
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

@login_required
def book_suggestion(request):
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_list')
    else:
        form = SuggestionForm()
    return render(request, 'core/book_suggestion.html', {'form': form})
