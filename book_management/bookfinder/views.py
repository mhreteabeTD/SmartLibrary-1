from django.shortcuts import render
from bookmanager.models import Book




# Create your views here.

def welcome(request):
    return render (request,'welcome.html')


def search_books(request):
    query = request.GET.get('q','')
    print(query,flush=True)
    books = Book.objects.filter(title__icontains=query)
    return render(request,'search_results.html',{'books':books,'query':query})
