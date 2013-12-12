from django.contrib import admin
from models import Operator

class OperatorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Operator, OperatorAdmin)