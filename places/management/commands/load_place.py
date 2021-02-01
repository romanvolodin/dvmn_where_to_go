import os

import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from places.models import Image, Place


def download_json(json_url):
    response = requests.get(json_url)
    response.raise_for_status()
    return response.json()


def add_place(json):
    place, created = Place.objects.get_or_create(
        title=json['title'],
    )
    return place


def add_image_to_place(place, image_url, upload_to):
    file_name = os.path.basename(image_url)
    file_path = os.path.join(upload_to, file_name)
    r = requests.get(image_url)
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
            json = download_json(options["json_url"])
        except requests.HTTPError as err:
            return self.stderr.write(str(err))

        place = add_place(json)
        self.stdout.write(self.style.SUCCESS(f'Place created: {place.title}.'))
        self.stdout.write(f'{len(json["imgs"])} images found.')
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)
        for index, image_url in enumerate(json['imgs'], start=1):
            image = add_image_to_place(place, image_url, settings.MEDIA_ROOT)
            self.stdout.write(f'{index}. {image.image}')
        self.stdout.write(self.style.SUCCESS(f'Images added.'))