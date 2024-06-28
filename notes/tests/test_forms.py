'''To validate the form and to test that it does not accept empty forms.'''
# notes/tests/test_forms.py

from django.test import SimpleTestCase
from ..forms import NoteForm


class NoteFormTest(SimpleTestCase):

    def test_note_form_valid_data(self):
        form = NoteForm(data={
            'title': "Test Note",
            'content': "This is to test the content."
        })
        self.assertTrue(form.is_valid())

    def test_note_form_no_data(self):
        form = NoteForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
