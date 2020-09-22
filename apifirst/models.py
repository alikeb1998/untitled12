from django.db import models


# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField("auto_now_add=true")
    active = models.BooleanField()


class animals(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=300)
