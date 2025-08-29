from django.db import models


# settings.configure(DEBUG=True)

class FileInfo(models.Model):
    path = models.CharField()
    modified = models.DateTimeField()


