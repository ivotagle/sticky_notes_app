'''To test the view urls, the whole CRUD process and its redirections'''
# notes/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from ..models import Note


class NoteViewsTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note content."
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('notes:note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_list.html')
        self.assertContains(response, self.note.title)

    def test_note_detail_view(self):
        response = self.client.get(reverse('notes:note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_detail.html')
        self.assertContains(response, self.note.title)
        self.assertContains(response, self.note.content)

    def test_note_create_view(self):
        response = self.client.post(reverse('notes:note_create'), {
            'title': "New Note",
            'content': "This is a new note content."
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertEqual(Note.objects.last().title, "New Note")

    def test_note_update_view(self):
        response = self.client.post(reverse('notes:note_update', args=[self.note.pk]), {
            'title': "Updated Note",
            'content': "This is an updated note content."
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Note")

    def test_note_delete_view(self):
        response = self.client.post(reverse('notes:note_delete', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
