from django import forms

from .models import Book, Category

class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'url')
