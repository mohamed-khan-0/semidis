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
    """
    Handles the home page and search feature.
    """
    # Get the search query from the URL (if any)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    # Get all the rooms (filtered by search query)
    rooms = Room.objects.filter(
                                # Find rooms that match any of the following
                                Q(topic__name__icontains=q) | 
                                Q(name__icontains=q) | 
                                Q(description__icontains=q))
    
    # Get the topic filter from the URL (if any)
    t = request.GET.get('t') if request.GET.get('t') != None else ''
    
    # Filter the rooms by topic name
    rooms = rooms.filter(topic__name__icontains=t)
    
    # Get all the topics
                                
    topics = Topic.objects.all()
    
    # Count the number of rooms
    count = rooms.count()
    
    # Create a context dictionary
    context = {
        'rooms': rooms,  # The filtered rooms
        'topics': topics,  # All the topics
        'count': count   # The number of rooms
    }
    
    # Render the home template with the context
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)


def room(request, room_id):
    room = Room.objects.get(id=room_id)
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


def update_room(request, room_id):
    """
    View to handle the updating of a room
    """
    room = Room.objects.get(id=room_id)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        # Get the form data from the request
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            # Save the changes to the database
            form.save()
            # Redirect to the home page
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room-form.html', context)



def delete_room(request, room_id):
    """
    View to handle the deletion of a room
    
    Args:
        request (HttpRequest): The request object
        room_number (str): The id of the room to delete
    """
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        # Delete the room when the form is submitted
        room.delete()
        return redirect('home')
    # Render the delete confirmation page
    context = {'room': room}
    return render(request, 'base/delete.html', context)
