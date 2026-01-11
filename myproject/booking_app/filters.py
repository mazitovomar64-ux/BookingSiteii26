from django_filters.rest_framework import FilterSet
from .models import Hotel, Room



class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'city': ['exact'],
            'country': ['exact'],
            'hotel_stars': ['exact'],
            'service': ['exact'],
        }


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'status_room': ['exact'],
            'price': ['gt','lt'],
        }