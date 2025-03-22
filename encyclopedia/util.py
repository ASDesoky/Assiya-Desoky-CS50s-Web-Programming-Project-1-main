import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries():
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def save_entry(title, content):
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def get_entry(title):
    filename = f"entries/{title}.md"
    if not default_storage.exists(filename):
        return None
    try:
        with default_storage.open(filename) as f:
            return f.read().decode("utf-8")
    except UnicodeDecodeError:
        with default_storage.open(filename) as f:
            return f.read().decode("latin-1")


def delete_entry(title):
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        print(f"Deleting file: {filename}")  # Debugging print statement
        default_storage.delete(filename)



