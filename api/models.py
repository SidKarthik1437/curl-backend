from django.db import models
import jsonfield
# Create your models here.


class Script(models.Model):
    body = jsonfield.JSONField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)


class File(models.Model):
    name = models.TextField(null=False)
    filestore = models.FileField(upload_to='files')

    def __str__(self):
        return self.name
