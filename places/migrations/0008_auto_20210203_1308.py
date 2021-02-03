# Generated by Django 3.1.5 on 2021-02-03 13:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20210131_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='место'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.CharField(blank=True, default=uuid.uuid1, max_length=255, verbose_name='id места'),
        ),
    ]
