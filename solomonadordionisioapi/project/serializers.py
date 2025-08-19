# from rest_framework import serializers
# from .models import Project


# class ProjectSerializer(serializers.ModelSerializer):
#     # tags = TagSerializer(many=True, read_only=True)
#     tag_titles = serializers.CharField(required=False)

#     class Meta:
#         model = Project
#         fields = ["id", "title", "description", "tags"]
#         read_only_fields = ["id"]

    # def create(self, validated_data):
    #     tag_titles_str = validated_data.pop("tag_titles", "")
    #     tag_titles = [
    #         t.strip().lower() for t in tag_titles_str.split(",") if t.strip()
    #     ]
    #     project = Project.objects.create(**validated_data)

    #     tags = []
    #     for title in tag_titles:
    #         tag, created = Tag.objects.get_or_create(title=title)
    #         tags.append(tag)
    #     project.tags.set(tags)
    #     return project

    # def update(self, instance, validated_data):
    #     tag_titles = validated_data.pop("tag_titles", None)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)

    #     if tag_titles is not None:
    #         tag_titles_list = [
    #             t.strip().lower() for t in tag_titles.split(",") if t.strip()
    #         ]
    #         tags = []
    #         for title in tag_titles_list:
    #             tag, created = Tag.objects.get_or_create(title=title)
    #             tags.append(tag)
    #         instance.tags.set(tags)

    #     instance.save()
    #     return instance
from rest_framework import serializers
from .models import Project
from tag.models import Tag
from tag.serializers import TagSerializer

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, source='tags'
    )

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'tags', 'tag_ids']