from django import forms
from mainapp.models import Youtube

class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = ['Title', 'uploadedby', 'Description',
                   'is_deleted' ]


