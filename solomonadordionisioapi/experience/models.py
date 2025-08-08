from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title
    


