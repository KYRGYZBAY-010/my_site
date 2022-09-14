from rest_framework import serializers
from .models import I_m, Projects


class ImSerializers(serializers.ModelSerializer):


    class Meta:
        model = I_m
        fields = ['title', 'img', 'about', 'date']


class ProjectSerializers(serializers.ModelSerializer):


    class Meta:
        model = Projects
        fields = ['title', 'icons', 'url']


class BotSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phon = serializers.CharField(max_length=30)
    name_company = serializers.CharField(max_length=120)
    email = serializers.EmailField(max_length=120)


    class Meta:
        fieds = ['name', 'phone', 'name_company', 'email']