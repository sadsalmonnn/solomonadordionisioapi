from django.db import models
class Tag(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects", blank=True)