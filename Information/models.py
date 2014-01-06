from django.db import models
from django.contrib.auth.models import User



class Operator(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class RechargeApi(models.Model):
    name = models.CharField(max_length=200)
    successful = models.IntegerField(default=1)
    failed = models.IntegerField(default=0)

    def success_rate(self):
        return (self.successful*100)/(self.successful+self.failed)

    def __unicode__(self):
        return self.name



class PhoneNumber(models.Model):
    phnumber = models.CharField(max_length=10)
    added_by = models.ForeignKey(User, related_name='numbers_added')
    operator = models.ForeignKey(Operator)
    is_successful = models.BooleanField(default=False)
    api_used = models.ForeignKey(RechargeApi, null=True)
    added_when = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.phnumber

class UserAccount(models.Model):
    account = models.OneToOneField(User)
    balance = models.IntegerField(default=0)

    def __unicode__(self):
        return self.account.username

