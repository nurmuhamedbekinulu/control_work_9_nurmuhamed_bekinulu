from django.contrib import admin
from webapp.models.photos import Photo


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'caption', 'author' , 'created_at', 'updated_at', 'is_deleted', 'deleted_at')
    list_filter = ('caption', 'author', 'users' , 'created_at')
    search_fields = ('caption', 'author', 'users')
    fields = ('photo', 'caption', 'author')
    readonly_fields = ('id', 'created_at', 'updated_at', 'is_deleted', 'deleted_at')


admin.site.register(Photo, PhotoAdmin)
