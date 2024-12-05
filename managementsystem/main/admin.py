from django.contrib import admin

# Register your models here.
from . models import Member,GalleryImage,News,Sermon
 
admin.site.register(Member)
admin.site.register(GalleryImage)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title',)
    ordering = ('-published_date',)


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'preacher', 'published_date')
    search_fields = ('title', 'preacher')
    list_filter = ('published_date',)
