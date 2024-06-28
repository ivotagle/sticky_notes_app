''''To test the model note creation'''

# notes/tests/test_models.py

from django.test import TestCase
from ..models import Note


class NoteModelTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="This is to test the content."
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is to test the content.")
        self.assertTrue(self.note.created_at)
        self.assertTrue(self.note.updated_at)

    def test_note_str(self):
        self.assertEqual(str(self.note), "Test Note")
