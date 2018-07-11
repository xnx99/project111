from django import forms
from mainapp.models import Youtube , telegram_model , fresheyes_post , fresheyes_comment ,post ,comment

#youtube form.
class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = ['Title', 'Description','Categorization',
                 'link']


#telegram form.
class telegramForm(forms.ModelForm):
    class Meta:
        model = telegram_model
        fields= ['Title', 'Description','Categorization',
                 'link']

#fresh eyes form.
class fresheyesForm(forms.ModelForm):
    class Meta:
        model = fresheyes_post
        fields= ['Title', 'help_type','Categorization',
                 'file']


class fresheyes_commentForm(forms.ModelForm):
    class Meta:
        model = fresheyes_comment
        fields= ['text', 'file']

#study group forms

class postForm(forms.ModelForm):
     class Meta:
         model = post
         fields= ['title','body','Categorization',
                  'image']


class commentForm(forms.ModelForm):
     class Meta:
         model = comment
         fields= ['body']


#<<ask about the fields needed for the comment>>


