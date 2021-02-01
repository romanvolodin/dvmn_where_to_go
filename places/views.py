from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Image, Place


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
    
    context = {"places_data": places_data}
    return render(request, 'index.html', context=context)


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
