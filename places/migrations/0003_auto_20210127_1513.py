# Generated by Django 3.1.5 on 2021-01-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='details_url',
        ),
        migrations.AddField(
            model_name='place',
            name='description_long',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True),
        ),
    ]
