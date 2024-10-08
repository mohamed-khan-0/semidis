from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic, Message
from django.http import HttpResponse
from .forms import RoomForm, MassageForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required



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
                                Q(description__icontains=q) | 
                                Q(host__username__icontains=q))
    
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
    messages = room.message_set.all().order_by('-created_at')
    participants = room.participants.all()
    mform = MassageForm()
    if request.method == 'POST':
        mform = MassageForm(request.POST, request.FILES)
        if mform.is_valid():
            massageForm = mform.save(commit=False)
            massageForm.user = request.user
            massageForm.room = room
            massageForm.save()
            room.participants.add(request.user)
            return redirect('room', room_id=room.id)
    context = {'room': room , 'messages': messages , 'participants': participants, 'mform': mform}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)  # Create room instance but don't save it yet
            room.host = request.user  # Set the host to the current user
            room.save()  # Now save the room with the host
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room-form.html', context)

@login_required(login_url='login')
def update_room(request, room_id):
    """
    View to handle the updating of a room
    """
    room = Room.objects.get(id=room_id)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return redirect('home')
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


@login_required(login_url='login')
def delete_room(request, room_id):
    """
    View to handle the deletion of a room
    
    Args:
        request (HttpRequest): The request object
        room_number (str): The id of the room to delete
    """
    room = Room.objects.get(id=room_id)

    if request.user != room.host:
        return redirect('home')

    if request.method == 'POST':
        # Delete the room when the form is submitted
        room.delete()
        return redirect('home')
    # Render the delete confirmation page
    context = {'room': room}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if request.user != message.user:
        return redirect('home')
    message.delete()
    return redirect('room', room_id=message.room.id)

def loginPage(request):
    page = 'login'
    # If the user is already authenticated, redirect to the home page
    
    if request.user.is_authenticated:
        return redirect('home')
    
    # Handling the POST request to authenticate the user
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Optional: You can add an error message here for invalid login
                pass
        else:
            # Optional: Handle form errors here
            pass
    else:
        form = AuthenticationForm()

    context = {'form': form, 'page': page}
    return render(request, 'base/login_register.html', context)


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    page = 'register'
    context = {'form': form, 'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
