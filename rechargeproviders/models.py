from django.db import models

class RechargeApi(models.Model):
    name = models.CharField(max_length=200)
    successful = models.IntegerField(default=1)
    failed = models.IntegerField(default=0)

    def success_rate(self):
        return (self.successful*100)/(self.successful+self.failed)

    def __unicode__(self):
        return self.name

