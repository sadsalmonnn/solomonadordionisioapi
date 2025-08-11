from django.contrib import admin
from .models import Project, Tag


class TagInline(admin.TabularInline):
    model = Project.tags.through
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
