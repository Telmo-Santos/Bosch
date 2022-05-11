from django.contrib import admin
from .models import Driver, Track, Team

# Register your models here.
# Adding Tables to admin page for easier access
admin.site.register(Driver)
admin.site.register(Team)
admin.site.register(Track)
