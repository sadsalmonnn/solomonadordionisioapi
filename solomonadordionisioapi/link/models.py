from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name


# Create your models here.
class Links(models.Model):
    links = models.ManyToManyField(Link, related_name="links", blank=True)
