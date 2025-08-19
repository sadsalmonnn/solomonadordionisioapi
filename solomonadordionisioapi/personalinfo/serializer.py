from rest_framework import serializers
from .models import PersonalInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ['id', 'title', 'content']
        read_only_fields = ["id"]
