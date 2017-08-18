from django.contrib import admin
from .models import Master, Account

class MasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nickname']

class AccountAdmin(admin.ModelAdmin):
    list_display = ['master', 'site', 'userid', 'password']

admin.site.register(Master, MasterAdmin)
admin.site.register(Account, AccountAdmin)
