from django.contrib import admin
from models import PhoneNumber, UserAccount

class PhoneNumberAdmin(admin.ModelAdmin):
    pass

class UserAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(UserAccount, UserAccountAdmin)