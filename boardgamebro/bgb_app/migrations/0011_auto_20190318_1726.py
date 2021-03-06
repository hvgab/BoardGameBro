# Generated by Django 2.1.7 on 2019-03-18 16:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bgb_app', '0010_auto_20190318_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gamenight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Describe the gamenight')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='gamenight was held at')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('public', models.BooleanField(default=False, help_text='Is this location a public location? ex. Cafe, Pub, Library, etc')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='email_communication',
            field=models.BooleanField(default=True, verbose_name='Would you like to get awesome news from us?'),
        ),
        migrations.AddField(
            model_name='gamenight',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='host_of', to='bgb_app.Player'),
        ),
        migrations.AddField(
            model_name='gamenight',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bgb_app.Location'),
        ),
        migrations.AddField(
            model_name='gamenight',
            name='players',
            field=models.ManyToManyField(to='bgb_app.Player'),
        ),
    ]
