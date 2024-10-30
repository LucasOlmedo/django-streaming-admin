from django.contrib import admin
from .models import Video, Tag

class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ('published_at', 'likes', 'views', 'author')
    list_display = ('title', 'is_published', 'published_at', 'likes', 'views')
    search_fields = ('title',)
    list_filter = ('is_published', 'tags')
    date_hierarchy = 'published_at'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user

        return super().save_model(request, obj, form, change)

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
