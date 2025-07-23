from django.db import models
# from django.conf import settings
"""from django.contrib.auth.models import Permission

class Permission:
    natur1al_key='c'
    app_label = 'DeluxeEditWeb'
"""

# settings.configure(DEBUG=True)

class FileInfo(models.Model):
    path = models.CharField()
    modified = models.DateTimeField()
    class Meta:
        app_label = 'DeluxeEditWeb'


