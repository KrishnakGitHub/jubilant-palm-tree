from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    # confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email', 'address_line1', 'city', 'state', 'pincode', 'user_type']
        widgets = {
            'password1': forms.PasswordInput,
            'password2': forms.PasswordInput,
        }
