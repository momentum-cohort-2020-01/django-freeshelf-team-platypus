from django import forms

from .models import Book, Category

class SuggestionBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'url', )

        

class SuggestionCategory(forms.ModelForm):

    class Meta:
        model = Category
        fields= ('name',)