import os
import uuid
import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from places.models import (
    Place,
    Image,
)


def download_json(json_url):
    response = requests.get(json_url)
    if response.status_code != 200:
        return
    return response.json()


def add_place(json):
    place, created = Place.objects.get_or_create(
        title=json['title'],
        longitude=json['coordinates']['lng'],
        latitude=json['coordinates']['lat'],
        description_short=json['description_short'],
        description_long=json['description_long'],
    )
    if created:
        place.place_id = uuid.uuid1()
        place.save()
    return place


def add_image_to_place(place, image_url, upload_to):
    file_name = os.path.basename(image_url)
    file_path = os.path.join(upload_to, file_name)
    r = requests.get(image_url)
    with open(file_path, 'wb') as f:
        f.write(r.content)
    image = Image(place=place, path=file_name)
    image.save()
    return image


class Command(BaseCommand):
    help = "Loads json data from given url and creates place with images."
    
    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        json = download_json(options["json_url"])
        if json is None:
            return self.stderr.write(f'Url does not exits.')
        place = add_place(json)
        self.stdout.write(self.style.SUCCESS(f'Place created: {place.title}.'))
        self.stdout.write(f'{len(json["imgs"])} images found.')
        for index, image_url in enumerate(json['imgs'], start=1):
            image = add_image_to_place(place, image_url, settings.MEDIA_ROOT)
            self.stdout.write(f'{index}. {image.path}')
        self.stdout.write(self.style.SUCCESS(f'Images added.'))