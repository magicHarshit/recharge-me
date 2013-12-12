from django.db import models
from django.contrib.auth.models import User
from operators.models import Operator
from rechargeproviders.models import RechargeApi

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
