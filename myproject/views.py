from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index page.")

def entry(request, entry):
    return HttpResponse(f"This is the entry page for {entry}.")

def newEntry(request):
    return HttpResponse("This is the new entry page.")

def edit(request, entry):
    return HttpResponse(f"This is the edit page for {entry}.")

def random(request):
    return HttpResponse("This is the random page.")

def search(request):
    return HttpResponse("This is the search page.")

# Adding the new index view
def new_index(request):
    return HttpResponse("Hello, world!")