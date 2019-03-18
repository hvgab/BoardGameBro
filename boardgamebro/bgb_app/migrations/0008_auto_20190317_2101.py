# Generated by Django 2.1.7 on 2019-03-17 20:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bgb_app', '0007_auto_20190317_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_of', to='bgb_app.Profile'),
        ),
        migrations.AddField(
            model_name='player',
            name='deleted_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='player was deleted at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]
