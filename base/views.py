from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from django.http import HttpResponse

from .forms import RoomForm

# Create your views here.
# rooms = [
#         {'id': 1, 'name': 'Room 1 : Learn Django'},
#         {'id': 2, 'name': 'Room 2 : Practice Django'},
#         {'id': 3, 'name': 'Room 3 : Make Money'},
#     ]
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
                                Q(topic__name__icontains=q) | 
                                Q(name__icontains=q) | 
                                Q(description__icontains=q))
    
    t = request.GET.get('t') if request.GET.get('t') != None else ''
    rooms = rooms.filter(topic__name__icontains=t)
                                
    topics = Topic.objects.all()
    count = rooms.count()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room(request, room_number):
    room = Room.objects.get(id=room_number)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room-form.html', context)


def update_room(request, room_number):
    room = Room.objects.get(id=room_number)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room-form.html', context)


def delete_room(request, room_number):
    room = Room.objects.get(id=room_number)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'room': room}
    return render(request, 'base/delete.html', context)