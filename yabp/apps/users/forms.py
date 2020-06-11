from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(
        widget=forms.widgets.DateInput(
            format=('%Y-%m-%d'),
            attrs={"type": "date"}
        )
    )
    location = forms.CharField()

    class Meta:
        model = Profile
        fields = ['birthday', 'location', 'bio']
