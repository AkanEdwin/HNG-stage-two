from rest_framework import serializers
from .models import Persons


class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('first_name', 'last_name', 'email', 'track',)

