from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Entry
import markdown2
import random as rand
from . import util
 
 

def index(request):
    entries = Entry.objects.all()
    return render(request, "wiki/index.html", {"entries": entries})

def entry(request, title):
    """Display a specific entry page."""
    entry_content = util.get_entry(title)  # Fetch the entry using util
    if entry_content:
        content = markdown2.markdown(entry_content)  # Convert Markdown to HTML
        return render(request, "encyclopedia/entry.html", {"title": title, "content": content})
    else:
        # Display a user-friendly message for non-existing entries
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": f"The entry '{title}' does not exist in the encyclopedia."
        })

def newEntry(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if Entry.objects.filter(title=title).exists():
            return render(request, "wiki/createNewPage.html", {"error": "Entry with this title already exists."})
        Entry.objects.create(title=title, content=content)
        return redirect('entry', entry=title)
    return render(request, "wiki/createNewPage.html")

def edit(request, entry):
    entry = get_object_or_404(Entry, title=entry)
    if request.method == "POST":
        content = request.POST['content']
        entry.content = content
        entry.save()
        return redirect('entry', entry=entry.title)
    return render(request, "wiki/edit.html", {"entry": entry})

def random(request):
    entries = Entry.objects.all()
    entry = rand.choice(entries)
    return redirect('entry', entry=entry.title)

def search(request):
    query = request.GET.get('q', '')
    results = Entry.objects.filter(title__icontains=query)
    return render(request, "wiki/search.html", {"results": results, "query": query})
 
def index(request):
    entries = Entry.objects.all()
    return render(request, "wiki/index.html", {"entries": entries})

def entry(request, entry):
    entry = get_object_or_404(Entry, title=entry)
    content = markdown2.markdown(entry.content)
    return render(request, "wiki/entry.html", {"entry": entry, "content": content})

def newEntry(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if Entry.objects.filter(title=title).exists():
            return render(request, "wiki/createNewPage.html", {"error": "Entry with this title already exists."})
        Entry.objects.create(title=title, content=content)
        return redirect('entry', entry=title)
    return render(request, "wiki/createNewPage.html")

def edit(request, entry):
    entry = get_object_or_404(Entry, title=entry)
    if request.method == "POST":
        content = request.POST['content']
        entry.content = content
        entry.save()
        return redirect('entry', entry=entry.title)
    return render(request, "wiki/edit.html", {"entry": entry})

def random(request):
    entries = Entry.objects.all()
    entry = rand.choice(entries)
    return redirect('entry', entry=entry.title)

def search(request):
    query = request.GET.get('q', '')
    results = Entry.objects.filter(title__icontains=query)
    return render(request, "wiki/search.html", {"results": results, "query": query})
