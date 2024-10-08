from django import forms
from django.forms import ModelForm
from .models import Room, Topic, Message


class RoomForm(ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

class MassageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    media = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Message
        fields = ['body', 'media']