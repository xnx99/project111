from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from userena.forms import SignupForm
from accounts.models import CommonProfile

class SignupForm(SignupForm):
    ar_first_name = forms.CharField(label=CommonProfile._meta.get_field('ar_first_name').verbose_name,
                                max_length=30)
    ar_middle_name = forms.CharField(label=CommonProfile._meta.get_field('ar_middle_name').verbose_name,
                                max_length=30)
    ar_last_name = forms.CharField(label=CommonProfile._meta.get_field('ar_last_name').verbose_name,
                                max_length=30)
    en_first_name = forms.CharField(label=CommonProfile._meta.get_field('en_first_name').verbose_name,
                                max_length=30)
    en_middle_name = forms.CharField(label=CommonProfile._meta.get_field('en_middle_name').verbose_name,
                                max_length=30)
    en_last_name = forms.CharField(label=CommonProfile._meta.get_field('en_last_name').verbose_name,
                                max_length=30)
    mobile_number = forms.CharField(label=CommonProfile._meta.get_field('mobile_number').verbose_name)

    def clean(self):
        # Call the parent class's clean function.
        cleaned_data = super(SignupForm, self).clean()
        for field in cleaned_data:
            if isinstance(cleaned_data[field], unicode):
                cleaned_data[field] = cleaned_data[field].strip()

        if 'email' in cleaned_data:
            cleaned_data['email'] = cleaned_data['email'].lower()

        return cleaned_data

    def save(self):
        # Derive usernames from email address
        self.cleaned_data['username'] = self.cleaned_data['username'].lower()

        # Save the parent form and get the user
        new_user = super(SignupForm, self).save()

        CommonProfile.objects.create(user=new_user,
                                     ar_first_name=self.cleaned_data['ar_first_name'],
                                     ar_middle_name=self.cleaned_data['ar_middle_name'],
                                     ar_last_name=self.cleaned_data['ar_last_name'],
                                     en_first_name=self.cleaned_data['en_first_name'],
                                     en_middle_name=self.cleaned_data['en_middle_name'],
                                     en_last_name=self.cleaned_data['en_last_name'],
                                     alternative_email=self.cleaned_data['alternative_email'],
                                     mobile_number=self.cleaned_data['mobile_number'],
                                     )
        return new_user
