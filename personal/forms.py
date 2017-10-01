from django import forms
from personal.models import Post
from personal.models import Signup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(forms.ModelForm):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'name': 'name'
        }
    ))

    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'name': 'email'
        }
    ))

    class Meta:
        model = Signup
        fields = ('contact_name', 'contact_email')




class ContactForm(forms.ModelForm):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            'name': 'name'
        }
    ))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'name': 'email'
        }
    ))
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment',
            'name': 'comments',
            'row': '5'
        }
    ))

    class Meta:
        model = Post
        fields = ('contact_name', 'contact_email', 'content')



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            #'password1',
            #'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user






















