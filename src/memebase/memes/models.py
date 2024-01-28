from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _


class MediaType(models.TextChoices):
    IMG = "IMG", _("Image")
    GIF = "GIF", _("Gif")
    VIDEO = "VID", _("Video")


class Meme(models.Model):
    template = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    media_file = models.FileField(upload_to='memes', null=False, blank=False)
    type = models.CharField(max_length=3, choices=MediaType, default=MediaType.IMG)
    uploaded_at = models.DateTimeField(default=datetime.now)
