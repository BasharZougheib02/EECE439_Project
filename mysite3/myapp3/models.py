from django.db import models

class Contactlist(models.Model):
 id = models.IntegerField(primary_key=True)
 name = models.CharField(max_length=200)
 address = models.CharField(max_length=200)
 profession = models.CharField(max_length=200)
 profession2 = models.CharField(max_length=200)
 number = models.CharField(max_length=200)
 email = models.CharField(max_length=200)

 def __str__(self):
  return self.title
