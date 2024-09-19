from django.db import models
import uuid
from pathlib import Path


class Page(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="title")
    body = models.TextField(max_length=2000, verbose_name="body")
    page_date = models.DateField(verbose_name="date")
    picture = models.ImageField(
        upload_to="diary/picture/", blank=True, null=True, verbose_name="photo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return self.title
    def delete(self, *args,**kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)