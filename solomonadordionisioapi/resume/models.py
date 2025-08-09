from django.db import models

# Create your models here.

class Resume(models.model):
    resume = models.FileField(upload_to="resume/%Y/%m/%d/")
    date = models.DateField()
    