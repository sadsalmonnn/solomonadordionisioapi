from rest_framework import serializers
from .models import Link, Links


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "name", "url"]
        read_only_fields = ["id"]


class LinksSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Links
        fields = ["id", "links"]
        read_only_fields = ["id", "links"]
