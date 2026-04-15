field_nrom django.db import models


class FileInfo(models.Model):
    path = models.CharField()
    modified = models.DateTimeField()
