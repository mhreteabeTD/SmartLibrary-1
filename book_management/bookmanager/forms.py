from django import forms
from .models import *

class BookForm(forms.ModelForm):
    shelves = forms.ModelMultipleChoiceField(
        queryset=Shelf.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )
    class Meta:
        model=Book
        fields=["title","author",'shelves','rating']

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

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name','description']
