from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(ReleaseLbl)
admin.site.register(Track)
admin.site.register(MasterDb)
admin.site.register(UserPlaylist)
admin.site.register(UserCredentials)