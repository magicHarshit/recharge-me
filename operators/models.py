from django.db import models

# Create your models here.
class Operator(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=200)
