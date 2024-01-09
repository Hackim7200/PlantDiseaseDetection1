from rest_framework import serializers
from api.models import api

##Serializer are used to convert complex query returns into json format##
class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = api
        fields = '__all__'