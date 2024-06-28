# creating notes/models.py
'''This will create the main class in our Notes. This will interact with the
database.'''
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
