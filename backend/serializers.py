import datetime
from rest_framework import serializers
from .models import City, Itinerary, Planning

from rest_framework import status
from rest_framework.response import Response



class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = ('id', 'name', 'description')


class ItinerarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Itinerary
        fields = ('id', 'city', 'start_day', 'end_day', 'peoples')

