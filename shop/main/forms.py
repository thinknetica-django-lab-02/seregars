from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    e_mail = forms.CharField()