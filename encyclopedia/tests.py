from django.test import TestCase
from django.urls import reverse
from . import util

class EncyclopediaTests(TestCase):

    def setUp(self):
        util.save_entry("Page1", "# This is the entry page for Page1")

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "All Pages")

    def test_entry_view(self):
        response = self.client.get(reverse('entry', args=['Page1']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the entry page for Page1")

    def test_new_entry_view(self):
        response = self.client.get(reverse('new_entry'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create New Page")

    def test_edit_view(self):
        response = self.client.get(reverse('edit_entry', args=['Page1']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Edit Entry: Page1")

    def test_random_view(self):
        response = self.client.get(reverse('random_page'))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        follow_response = self.client.get(response.url)
        self.assertEqual(follow_response.status_code, 200)

    def test_search_view(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Search Results")

    def test_delete_entry(self):
        # Ensure the entry exists
        response = self.client.get(reverse('entry', args=['Page1']))
        self.assertEqual(response.status_code, 200)

        # Delete the entry
        response = self.client.post(reverse('delete_entry', args=['Page1']))
        self.assertEqual(response.status_code, 302)  # Redirect status

        # Ensure the entry no longer exists
        response = self.client.get(reverse('entry', args=['Page1']))
        print("Response status code after deletion:", response.status_code)
        self.assertEqual(response.status_code, 404)