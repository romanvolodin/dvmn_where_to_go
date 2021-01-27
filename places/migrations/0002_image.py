# Generated by Django 3.1.5 on 2021-01-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('path', models.ImageField(upload_to='')),
                ('place', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='places.place')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]