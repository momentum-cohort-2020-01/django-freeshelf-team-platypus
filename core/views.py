from django.shortcuts import render

import csv


def book_list(request):
    with open('sample_books.csv', 'r') as f:
        book_reader = csv.DictReader(f)
        books = [book for book in book_reader]
    context = {'books': books}
    return render(request, 'core/book_list.html', context=context)
