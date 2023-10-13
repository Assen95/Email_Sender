from django.db import models
from django.utils import timezone


class Email(models.Model):
    subject = models.CharField(
        max_length=25,
        null=False,
        blank=False,
    )
    to_email = models.EmailField(
        max_length=30,
        null=False,
        blank=False,
    )
    content = models.TextField(
        max_length=255,
        null=True,
        blank=True
    )
