from rest_framework.serializers import ModelSerializer

from ads.models import Ad


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(ModelSerializer):
    class Meta:
        model = Ad
        exclude = ['description']
