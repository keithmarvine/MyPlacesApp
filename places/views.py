from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from .models import Place
import json


def places_api(request):
    places = Place.objects.all()

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.location.x,  # longitude
                    place.location.y   # latitude
                ]
            },
            "properties": {
                "name": place.name
            }
        }

        geojson["features"].append(feature)

    return JsonResponse(geojson)



def map_view(request):
    return render(request, 'places/map.html')

@csrf_exempt
def add_place(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        lat = data.get('lat')
        lng = data.get('lng')

        place = Place.objects.create(
            name=name,
            location=Point(lng, lat)
        )

        return JsonResponse({
            "status": "success",
            "name": place.name,
            "lat": lat,
            "lng": lng
        })