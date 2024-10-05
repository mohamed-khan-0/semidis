from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:room_number>', views.room, name='room'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:room_number>', views.update_room, name='update_room'),
    path('delete_room/<str:room_number>', views.delete_room, name='delete_room'),
]