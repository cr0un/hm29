from rest_framework import serializers

from users.models import User
from users.serializers import LocationSerializer
from .models import Ad, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class AdSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    location = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ['id', 'name', 'author', 'price', 'description', 'is_published', 'category', 'image', 'location']

    def get_location(self, obj):
        return LocationSerializer(obj.author.locations.first()).data

