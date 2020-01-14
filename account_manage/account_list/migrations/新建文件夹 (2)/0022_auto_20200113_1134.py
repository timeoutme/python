# Generated by Django 2.2.5 on 2020-01-13 03:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account_list', '0021_merge_20200113_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='account',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='child',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounts',
            name='child_birthday',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='city',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='family_monthly_income',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounts',
            name='personal_monthly_income',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accounts',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
