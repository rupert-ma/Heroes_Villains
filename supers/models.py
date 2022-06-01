from django.db import models
from super_types.models import SuperType

# Create your models here.
class Power(models.Model):
    name = models.CharField(max_length=255)


class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.ManyToManyField(Power, related_name='primary_ability')
    secondary_ability = models.ManyToManyField(Power, related_name='secondary_ability')
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)

