"""
Definition of models.
"""

from django.db import models


class FileInfo(models.Model):
    path = models.CharField()
    modified = models.DateTimeField()

