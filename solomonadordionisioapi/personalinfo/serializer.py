from rest_framework import serializers
from .models import PersonalInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ['title', 'company', 'location', 'startdate', 'enddate', 'description']