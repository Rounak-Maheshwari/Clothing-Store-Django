from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from .models import Profile, Address

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=25)

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = ['photo']

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ["first_name", "last_name", "phone_number", "street", "city", "state", "pincode", "is_default"]