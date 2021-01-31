from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255, blank=True)
    longitude = models.FloatField(verbose_name="долгота", default=0)
    latitude = models.FloatField(verbose_name="широта", default=0)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, default=0, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return "{} {}".format(self.order, self.place.title)
