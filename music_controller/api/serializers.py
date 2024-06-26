from rest_framework import serializers
from .models import Room

# RoomSerializer class to serialize Room model data into JSON format

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host' , 'guest_can_pause', 'votes_to_skip', 'created_at')
        