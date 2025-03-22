from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import MyModel

def index(request):
    return HttpResponse("This is the index page.")

def detail(request, pk):
    my_model = get_object_or_404(MyModel, pk=pk)
    return HttpResponse(f"This is the detail page for {my_model.name}.")

def create(request):
    return HttpResponse("This is the create page.")

def update(request, pk):
    my_model = get_object_or_404(MyModel, pk=pk)
    return HttpResponse(f"This is the update page for {my_model.name}.")

def delete(request, pk):
    return HttpResponse("This is the delete page.")

def additional_step(request):
    return HttpResponse("This is the additional step page.")