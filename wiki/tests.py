from django.test import TestCase
from .models import Entry

class EntryModelTest(TestCase):

    def setUp(self):
        Entry.objects.create(title="Sample Entry", content="This is a sample entry content")

    def test_entry_content(self):
        entry = Entry.objects.get(title="Sample Entry")
        self.assertEqual(entry.content, "This is a sample entry content")