from django.db import models
"""import django.contrib.auth.models
class Permission:
     app_label = 'DeluxeEditWeb'
"""
class Meta:
    app_label = 'DeluxeEditWeb'

class FileInfo(models.Model):
    path = models.CharField()
    modified = models.DateTimeField()
