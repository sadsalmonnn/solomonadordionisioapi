from rest_framework import serializers
from .models import Project, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
        read_only_fields = ['id']

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_titles = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'tags', 'tag_titles']
        read_only_fields = ['id']

    def create(self, validated_data):
        tag_titles_str = validated_data.pop('tag_titles', '')
        tag_titles = [t.strip() for t in tag_titles_str.split(',') if t.strip()]
        project = Project.objects.create(**validated_data)

        tags = []
        for title in tag_titles:
            tag, created = Tag.objects.get_or_create(title=title.strip())
            tags.append(tag)
        project.tags.set(tags)
        return project

    def update(self, instance, validated_data):
        tag_titles = validated_data.pop('tag_titles', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if tag_titles is not None:
            tags = []
            for title in tag_titles:
                tag, created = Tag.objects.get_or_create(title=title.strip())
                tags.append(tag)
            instance.tags.set(tags)
        instance.save()
        return instance