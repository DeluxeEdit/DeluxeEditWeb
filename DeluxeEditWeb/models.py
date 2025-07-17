from django.db import models
class Meta:
    app_label = 'DeluxeEditWeb'

class FileInfo(models.Model):
    path = models.CharField()
    modified = models.DateTimeField()
