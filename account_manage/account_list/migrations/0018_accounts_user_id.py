# Generated by Django 3.0 on 2019-12-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_list', '0017_auto_20191226_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
