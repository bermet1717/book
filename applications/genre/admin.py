from django.contrib import admin

# Register your models here.

from applications.genre.models import Genre
admin.site.register(Genre)