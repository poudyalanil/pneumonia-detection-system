from django import forms
from ums.models import Normal_User, User_Support_Ticket
from django.contrib.auth.models import User


class Register_Form(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user


class Normal_User_Form(forms.ModelForm):
    class Meta:
        model = Normal_User
        fields = ['phone', 'gender', 'country', 'profile_pic']


class User_Update_Form(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user


class Normal_User_Update_Form(forms.ModelForm):
    class Meta:
        model = Normal_User
        fields = ['phone', 'gender', 'country', 'profile_pic']


class Issue_New_Ticket(forms.ModelForm):
    class Meta:
        model = User_Support_Ticket
        fields = ['title', 'message']
