from django.contrib import admin

# Register your models here.

from .models import Room, Message, Topic, UserProfile

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
admin.site.register(UserProfile)