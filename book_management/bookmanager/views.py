from django.http import Http404
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import *
# Create your views here


"""
Book related views
"""

def home(request):
    return render(request, 'bookmanager/home.html')  



def book_list(request):
    books=Book.objects.all()
    return render(request,'bookmanager/book_list.html',{'books':books})

def add_book(request):
    if request.method == "POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'bookmanager/add_book.html',{"form":form})

def edit_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        form = BookForm (request.POST , instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request,'bookmanager/edit_book.html',{'form':form})

"""
Library configuration related views
"""

def configure_library(request):
    if request.method == "POST":
        level_form = LibraryLevelForm(request.POST, prefix='level')
        Shelf_form = ShelfForm(request.POST , prefix='shelf')

        if 'add_level' in request.POST and level_form.is_valid():
            level_form.save()
            return redirect('configure_library')

        if 'add_shelf' in request.POST and Shelf_form.is_valid():
            Shelf_form.save()
            return redirect('configure_library')
    else:
        level_form = LibraryLevelForm(prefix='level')
        Shelf_form = ShelfForm(prefix='shelf')
    
    library_levels = LibraryLevel.objects.all().order_by('level_number')
    return render(
        request,
        'bookmanager/configure_library.html',
        {
        'level_form' : level_form,
        'Shelf_form' : Shelf_form,
        'library_levels' : library_levels
        }

    )


    
def stats(request):

    return render(request,'bookmanager/stats.html')

def add_library_level(request):
    if request.method == 'POST':
        form = LibraryLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('configure_library')
    else:
        form = LibraryLevelForm()
    return render(request, 'bookmanager/add_library_level.html' , {'form':form})

def edit_library_level(request,pk):
    level = get_object_or_404(LibraryLevel,pk=pk)
    if request.method == "POST":
        form = LibraryLevelForm (request.POST , instance=level)
        if form.is_valid():
            form.save()
            return redirect('configure_library')
    else:
        form = LibraryLevelForm(instance=level)
    return render(request,'bookmanager/add_library_level.html',{'form':form})







def add_shelf(request,level_number):
    try:
        level = LibraryLevel.objects.get(level_number=level_number)
    except LibraryLevel.DoesNotExist:
        raise Http404("Level Doesn't exist")
    
    if request.method == 'POST':
        form = ShelfForm(request.POST)
        if form.is_valid():
            shelf=form.save(commit=False)
            shelf.level=level
            shelf.save()
            return redirect('configure_library')
    else:
        form = ShelfForm()
    return render(request, 'bookmanager/add_shelve.html' , {'form':form})


def add_section(request, level_number):
    try:
        level = LibraryLevel.objects.get(level_number=level_number)
    except LibraryLevel.DoesNotExist:
        raise Http404("Level Doesn't exist")
    
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section=form.save(commit=False)
            section.level=level
            section.save()
            return redirect('configure_library')
    else:
        form = SectionForm()
    return render(request, 'bookmanager/add_section.html' , {'form':form})




def edit_shelf(request,pk):
    shelf = get_object_or_404(Shelf,pk=pk)
    if request.method == "POST":
        form = ShelfForm (request.POST , instance=shelf)
        if form.is_valid():
            form.save()
            return redirect('configure_library')
    else:
        form = ShelfForm(instance=shelf)
    return render(request,'bookmanager/add_shelf.html',{'form':form})

def edit_section(request,pk):
    section = get_object_or_404(Section,pk=pk)
    if request.method == "POST":
        form = SectionForm (request.POST , instance=section)
        if form.is_valid():
            form.save()
            return redirect('configure_library')
    else:
        form = SectionForm(instance=section)
    return render(request,'bookmanager/add_section.html',{'form':form})

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Section
from django.contrib import messages  # Optional, for sending feedback messages to the template

def delete_section(request, pk):
    section = get_object_or_404(Section, pk=pk)

    if request.method == 'POST':
        section.delete()
        messages.success(request, "Section successfully deleted.")  # Optional feedback message
        return redirect(reverse('configure_library'))  # Redirect to the library configuration page

    return render(request, 'bookmanager/delete_section_confirm.html', {'section': section})