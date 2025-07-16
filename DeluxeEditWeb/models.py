from django.db import models


class FileInfo(models.Model):
    app_label= 'DeluxeEditWeb'
    path = models.CharField()
    modified = models.DateTimeField()
