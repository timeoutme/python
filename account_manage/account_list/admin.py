from django.contrib import admin
from .models import Accounts

# Register your models here.

class Accounts_admin(admin.ModelAdmin):
    list_display = ('id','account','area','province','city','county','sex','birthday','edu','trade','position','marriage','working','child','zip_code','create_time','user')

admin.site.register(Accounts, Accounts_admin)