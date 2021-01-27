from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255, blank=True)
    longitude = models.FloatField(verbose_name="долгота", default=0)
    latitude = models.FloatField(verbose_name="широта", default=0)
    details_url = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, default=0, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    path = models.ImageField()

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return "{} {}".format(self.order, self.place.title)
