from django import forms
from .models import Book , LibraryLevel , Shelf

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=["title","author",'location','rating']

class LibraryLevelForm(forms.ModelForm):
    class Meta:
        model = LibraryLevel
        fields=[
            'level_number',
            'description',
        ]

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        exclude = ['level']
        fields = [
            'level',
            'shelf_number',
            'description'
        ]