from django.contrib import admin
from .models import Accounts,User_account

# Register your models here.

class Accounts_admin(admin.ModelAdmin):
    list_display = ('id','account','area','province','city','county','sex','birthday','edu','trade','position','marriage','working','child','zip_code','create_time','hide_time','user')
    list_per_page = 20
    list_editable = ['sex','account']

admin.site.register(Accounts, Accounts_admin)


admin.site.register(User_account)