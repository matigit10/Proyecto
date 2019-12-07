from django.contrib import admin

# Register your models here.

from .models import TarjetasVideos,Driver

admin.site.register(TarjetasVideos)
admin.site.register(Driver)