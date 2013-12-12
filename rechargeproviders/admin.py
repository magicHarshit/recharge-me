from django.contrib import admin
from models import RechargeApi

class RechargeApiAdmin(admin.ModelAdmin):
    pass

admin.site.register(RechargeApi, RechargeApiAdmin)