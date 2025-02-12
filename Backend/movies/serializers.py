from rest_framework import serializers
from movies.models import movies_model

class movie_serializer(serializers.ModelSerializer):
    class Meta:
        model = movies_model
        fields= '__all__'