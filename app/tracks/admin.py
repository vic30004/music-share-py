from django.contrib import admin
from .models import Track, Like
# Register your models here.


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'posted_by')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'posted_by')
    list_per_page = 25


admin.site.register(Track, TrackAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'track')
    list_display_links = ('id',)
    search_fields = ('id', 'user')
    list_per_page = 25


admin.site.register(Like, LikeAdmin)
