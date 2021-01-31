from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import (
    Place,
    Image,
)


def index(request):

    places = Place.objects.all()

    places_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.place_id,
                    "detailsUrl": reverse('place-details', kwargs={'place_id': place.id})
                }
            } for place in places
        ]
    }
    
    template = loader.get_template('index.html')
    context = {"places_data": places_data}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.all()
    return JsonResponse(
        {
            "title": place.title,
            "imgs": [
                image.image.url for image in images
            ],
            "description_short": place.short_description,
            "description_long": place.long_description,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude
            }
        },
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
