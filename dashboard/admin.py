from django.contrib import admin
from .models import ReadLater,LikedNews,Catagory

# Register your models here.
class Read(admin.ModelAdmin):
     list_display = ('url_name', 'title',)

class Liked(admin.ModelAdmin):
     list_display = ('url_name', 'title',)

class Cat(admin.ModelAdmin):
     list_display = ('fav1', 'fav2','fav3', 'fav4','fav5',)
     
admin.site.register(ReadLater,Read)
admin.site.register(LikedNews,Liked)
admin.site.register(Catagory,Cat)