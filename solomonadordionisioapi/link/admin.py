from django.contrib import admin

# Register your models here.

from .models import Link, Links


class LinkInline(admin.TabularInline):
    model = Links.links.through
    extra = 1


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    exclude = ("links",)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass
