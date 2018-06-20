from django import forms
from mainapp.models import Youtube , telegram_model

class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = ['Title', 'Description','Categorization',
                 'link']



class telegramForm(forms.ModelForm):
    class Meta:
        model = telegram_model
        fields= ['Title', 'Description','Categorization',
                 'link']
