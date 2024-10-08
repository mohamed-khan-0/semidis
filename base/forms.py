from django import forms
from django.forms import ModelForm
from .models import Room, Topic, Message
from django.core.exceptions import ValidationError


def validate_file_size(value):
    limit = 10 * 1024 * 1024  # 10 MB in bytes
    if value.size > limit:
        raise ValidationError('File size cannot exceed 10 MB.')

class RoomForm(ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

class MassageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    media = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False, validators=[validate_file_size])

    def clean_media(self):
        media = self.cleaned_data.get('media')
        if media and not media.content_type.startswith('audio'):
            raise forms.ValidationError('Only audio files are allowed.')
        return media

    class Meta:
        model = Message
        fields = ['body', 'media']