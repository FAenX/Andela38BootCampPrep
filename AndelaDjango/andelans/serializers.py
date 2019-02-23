from rest_framework import serializers
from .models import Andelan

# model serializer


class AndelansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Andelan
        fields = ('first_name', 'second_name', 'language')
