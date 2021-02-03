import uuid

from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name="заголовок", max_length=255)
    place_id = models.CharField(verbose_name="id места", max_length=255, blank=True, default=uuid.uuid1)
    longitude = models.FloatField(verbose_name="долгота")
    latitude = models.FloatField(verbose_name="широта")
    short_description = models.TextField(verbose_name="Короткое описание", blank=True)
    long_description = HTMLField(verbose_name="Длинное описание", blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="место", related_name='images')
    order = models.PositiveIntegerField(default=0, verbose_name="номер по порядку")
    image = models.ImageField(verbose_name="картинка")

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return "{} {}".format(self.order, self.place.title)
