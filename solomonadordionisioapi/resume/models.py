from django.db import models


class Resume(models.Model):
    resume_uri = models.URLField(default='', blank=True)
    date = models.DateTimeField(null=True, blank=True)
