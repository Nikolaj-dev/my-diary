from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    note_title = models.CharField(max_length=256, blank=False, unique=True)
    note_content = models.TextField()
    created_time = models.DateTimeField(auto_created=True, auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return str(self.note_title)

    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'notes'
        ordering = ['created_time']