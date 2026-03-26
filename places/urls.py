from django.urls import path
from . import views
from .views import places_api, add_place

urlpatterns = [
    path('', views.map_view, name='map'),
    path('places/', places_api),
    path('add-place/', add_place),
]