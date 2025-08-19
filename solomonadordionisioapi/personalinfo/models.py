from django.db import models

# Create your models here.
class Hobby(models.Model):
  title = models.CharField(max_length=200)

  def __str__(self):
    return self.title
  

class PersonalInfo(models.Model):
  age = models.IntegerField()
  address = models.CharField(max_length=200)
  university = models.CharField(max_length=200)
  highschool = models.CharField(max_length=200)
  hobbies = models.ManyToManyField(Hobby, related_name="hobbies", blank=True)
  