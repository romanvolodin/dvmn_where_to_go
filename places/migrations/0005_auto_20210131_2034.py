# Generated by Django 3.1.5 on 2021-01-31 20:34

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20210131_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='номер по порядку'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='место'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='id места'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=255, verbose_name='заголовок'),
        ),
    ]
