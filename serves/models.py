from django.db import models
from django.utils import timezone

from .consts import ANNOUNCEMENT_CHOICES, POST_CHOICES


class Announcement(models.Model):
    name = models.CharField(max_length=256)
    theme = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    link = models.URLField()
    action = models.CharField(max_length=256, choices=ANNOUNCEMENT_CHOICES)
    length = models.SmallIntegerField()
    date = models.DateTimeField(default=timezone.now)


class Post(models.Model):
    theme = models.CharField(max_length=256)
    description = models.TextField()
    action = models.CharField(max_length=256, choices=POST_CHOICES)
    region = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    url = models.URLField()
    emoji = models.BooleanField()
    length = models.SmallIntegerField()
    date = models.DateTimeField(default=timezone.now)
