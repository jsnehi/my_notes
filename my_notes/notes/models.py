from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone


class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, blank=True, null=True)
    detail = models.TextField()
    created_by = models.ForeignKey(User, related_name="created_user_ids", on_delete=models.CASCADE, blank=True, null=True)
    shared_with = models.ManyToManyField(User, related_name='shared_notes',blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class NotesHistory(models.Model):
    note = models.ForeignKey(Notes, related_name="history_note", on_delete=models.CASCADE)
    history_detail = models.JSONField(default=dict)

    def __str__(self):
        return self.note.title