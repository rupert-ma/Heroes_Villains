from django.db import models
from django.forms import CharField
from supers.models import Super

# Create your models here.

class SuperType(models.Model):
    type = models.CharField(max_length=255)
    super = models.ForeignKey(Super, on_delete=models.CASCADE)