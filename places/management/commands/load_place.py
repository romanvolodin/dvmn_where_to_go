import os

import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from places.models import Image, Place


def add_image_to_place(place, image_url, upload_to):
    file_name = os.path.basename(image_url)
    file_path = os.path.join(upload_to, file_name)
    r = requests.get(image_url)
    r.raise_for_status()
    with open(file_path, 'wb') as f:
        f.write(r.content)
    image = Image(place=place, image=file_name)
    image.save()
    return image


class Command(BaseCommand):
    help = "Loads json data from given url and creates place with images."
    
    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        try:
            response = requests.get(options["json_url"])
            response.raise_for_status()
        except requests.HTTPError as err:
            return self.stderr.write('Не можем найти указанный файл. Убедитесь, что введенная ссылка верна.')

        raw_place = response.json()
        place, created = Place.objects.get_or_create(
            title=raw_place['title'],
            longitude=raw_place['coordinates']['lng'],
            latitude=raw_place['coordinates']['lat'],
            defaults={
                'short_description': raw_place['description_short'],
                'long_description': raw_place['description_long'],
            }
        )
        self.stdout.write(self.style.SUCCESS(f'Place created: {place.title}.'))
        self.stdout.write(f'Trying to download {len(raw_place["imgs"])} images...')
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        for index, image_url in enumerate(raw_place['imgs'], start=1):
            try:
                image = add_image_to_place(place, image_url, settings.MEDIA_ROOT)
                self.stdout.write(f'{index}. {image.image}')
            except requests.HTTPError as err:
                self.stderr.write(str(err))
        self.stdout.write('Done.')
