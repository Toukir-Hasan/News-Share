from django.contrib import admin
from .models import ReadLater,LikedNews

# Register your models here.
class Read(admin.ModelAdmin):
     list_display = ('url_name', 'title',)

class Liked(admin.ModelAdmin):
     list_display = ('url_name', 'title',)
     
admin.site.register(ReadLater,Read)
admin.site.register(LikedNews,Liked)