# Generated by Django 2.2.5 on 2019-12-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_list', '0013_accounts_hide_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='child_birthday',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='hide_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
