from django.contrib import admin
from . import models


class NoteAdmin(admin.ModelAdmin):
    list_display = ['note_title', 'note_content', 'author']


admin.site.register(models.Note, NoteAdmin)
