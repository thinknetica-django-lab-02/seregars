import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory, DateField, Textarea, ModelForm

from .models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class BirthDateField(DateField):
    def validate(self, value):
        super().validate(value)

        days = (365 * 18) + (18 / 4) + 1

        allow_date = value + datetime.timedelta(days=days)

        if datetime.date.today() < allow_date:
            raise ValidationError("Возраст должен быть больше 18 лет")


ProfileFormset = inlineformset_factory(User,
                                       Profile, extra=1,
                                       fields=('birth_date', 'about'),
                                       field_classes={
                                           'birth_date': BirthDateField,
                                       },
                                       widgets={
                                           'about': Textarea,
                                       })
