from django.contrib import admin
from .models import CustomUser, Trainer, Room, Schedule, Booking

admin.site.register(CustomUser)
admin.site.register(Trainer)
admin.site.register(Room)
admin.site.register(Schedule)
admin.site.register(Booking)
