from django.db import models

# from django.contrib.auth.models import User
# Create your models here.

class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=40)
    area = models.CharField(max_length=10)
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    county = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    age = models.IntegerField()
    birthday = models.CharField(max_length=30)
    edu = models.CharField(max_length=10)
    trade = models.CharField(max_length=30)
    position = models.CharField(max_length=10)
    marriage =models.CharField(max_length=10)
    working = models.CharField(max_length=10)
    child = models.IntegerField()
    child_age = models.IntegerField()
    child_birthday = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=30)
    personal_monthly_income = models.CharField(max_length=20)
    family_monthly_income = models.CharField(max_length=20)
    hide_time = models.DateField()


    class Meta:
        ordering = ['-id']
        

class User_account(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120,unique=True,null=False)    
    password = models.CharField(max_length=256)    
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_time']


