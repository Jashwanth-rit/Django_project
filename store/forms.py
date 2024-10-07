from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms



from django.contrib.auth.forms import PasswordChangeForm

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'})
    )
    address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'})
    )

    class Meta:
        model = UserProfile
        fields = ['phone', 'address']
        labels = {
            'phone': '',
            'address': '',
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Add additional initialization if needed


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
        }

class UpdateUserForm(UserChangeForm):
    # ... (existing code remains unchanged)

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # Include UserProfileForm fields in the same form
        self.user_profile = UpdateUserProfileForm(instance=self.instance.userprofile)
        self.fields['username'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super(UpdateUserForm, self).save(commit)
        user_profile = self.user_profile.save(commit)
        return user


class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Current Password'})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'})
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']


class UpdateUserForm(UserChangeForm):
    password1 = None
    password2 = None
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),)
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),)
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),)
   

    class Meta:
        model  =  User

        fields = ('username','first_name','last_name','email')

        # fields = "__all__" # Gets all the columns
        # fields  = ('name','address') # Get only name , address column
        labels = {
             'username':'',
              'first_name':'',
               'last_name':'',
                'email':'',
                 

        }
        widgets = {
            'username':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter name'}),
             
        }
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
       



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),)
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),)
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),)
   

    class Meta:
        model  =  User

        fields = ('username','first_name','last_name','email','password1','password2')

        # fields = "__all__" # Gets all the columns
        # fields  = ('name','address') # Get only name , address column
        labels = {
             'username':'',
              'first_name':'',
               'last_name':'',
                'email':'',
                 'password1':'',
                  'password2':'',

        }
        widgets = {
            'username':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter name'}),
             
        }
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
