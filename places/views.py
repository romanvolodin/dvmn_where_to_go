from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import (
    Place,
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
                    "detailsUrl": place.details_url
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
    return JsonResponse(
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": place.details_url
            }
        },
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
