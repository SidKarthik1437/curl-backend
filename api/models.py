from django.db import models

# Create your models here.
class Script(models.Model):
    body = models.JSONField(_(""), encoder=, decoder=)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
