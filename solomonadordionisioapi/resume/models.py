from django.db import models

# Create your models here.


class Resume(models.Model):
    resume_uri = models.TextField()
    date = models.DateField()
