from django.db import models

# Create your models here.
class RechargeApi(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=200)
