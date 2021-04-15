import datetime
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory, DateField, Textarea

from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]


class BirthDateField(DateField):
    def validate(self, value):
        super().validate(value)

        days = (365 * 18) + (18 / 4) + 1

        allow_date = value + datetime.timedelta(days = days)

        if datetime.date.today() < allow_date:
            raise ValidationError("Возраст должен быть больше 18 лет")

ProfileFormSet = inlineformset_factory(User, Profile, extra=1, fields=('about', 'birth_date',), field_classes={'birth_date': BirthDateField,}, widgets={'about': Textarea})
