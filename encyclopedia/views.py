from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import util
import markdown2
import random
import random as rand
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

def search(request):
    """Search for entries containing a query string."""
    query = request.GET.get('q', '').strip()  # Get the search query
    
    # Check for an exact match
    if util.get_entry(query):  
        return redirect('entry', title=query)  # Redirect to the entry page

    # Find partial matches (case-insensitive substring search)
    results = [entry for entry in util.list_entries() if query.lower() in entry.lower()]
    
    # Render search results if there are matches
    if results:
        return render(request, "encyclopedia/search.html", {"query": query, "results": results})
    
    # Redirect to /wiki/<query> with no matches found
    return HttpResponseRedirect(reverse('entry', args=[query]))




def random_page(request):
    """Redirect to a random encyclopedia entry."""
    entries = util.list_entries()  # Use the util function to list all entries
    if entries:
        random_entry = rand.choice(entries)  # Pick a random entry
        return redirect('entry', title=random_entry)
    return redirect('index')  # Redirect to the index if no entries exist


def index(request):
    """Render the index page with a list of all entries."""
    entries = util.list_entries()  # Use util to list all entries
    return render(request, "encyclopedia/index.html", {"entries": entries})
 

 
def entry(request, title):
    """Display a specific entry page."""
    entry_content = util.get_entry(title)  # Fetch the entry
    if entry_content:
        # Convert Markdown content to HTML
        content = markdown2.markdown(entry_content)
        exists = True
    else:
        # Display an error message if the entry doesn't exist
        content = f"<p>The entry '{title}' does not exist in the encyclopedia.</p>"
        exists = False

    return render(request, "encyclopedia/entry.html", {"title": title, "content": content, "exists": exists})



def new_entry(request):
    """Create a new encyclopedia entry."""
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Check if an entry with the same title already exists
        if util.get_entry(title):
            return render(request, "encyclopedia/new.html", {"error": "An entry with this title already exists."})

        util.save_entry(title, content)  # Save the entry using util
        return redirect('entry', title=title)
    return render(request, "encyclopedia/new.html")


def edit_entry(request, title):
    """Edit an existing encyclopedia entry."""
    content = util.get_entry(title)  # Fetch the current content using the title
    if not content:
        return HttpResponse("The requested entry was not found.", status=404)

    if request.method == "POST":
        updated_content = request.POST.get('content')
        util.save_entry(title, updated_content)  # Save the updated content
        return redirect('entry', title=title)

    return render(request, "encyclopedia/edit.html", {"title": title, "content": content})


def delete_entry(request, title):
    """Delete an entry."""
    if request.method == "POST":
        util.delete_entry(title)  # Delete the entry using the util function
        return redirect('index')
    return render(request, "encyclopedia/delete.html", {"title": title})