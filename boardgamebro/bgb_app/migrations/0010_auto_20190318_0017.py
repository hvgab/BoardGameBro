# Generated by Django 2.1.7 on 2019-03-17 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgb_app', '0009_auto_20190317_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='player is deleted'),
        ),
    ]
