from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]

ProfileFormSet = inlineformset_factory(User, Profile, extra=1, fields=('about',))

