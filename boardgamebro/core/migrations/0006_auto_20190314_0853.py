# Generated by Django 2.1.7 on 2019-03-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190311_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='games',
            field=models.ManyToManyField(blank=True, null=True, to='core.Game'),
        ),
    ]