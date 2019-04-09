from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .models import Profile, Student

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    email = forms.EmailField(label = (u'Email Adress')) #for labelling
    nsu_id = forms.IntegerField(label = (u'NSU ID'))
    #nsu_ID = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        mail = cleaned_data.get('email')
        nsuID = cleaned_data.get('nsu_id')
        x = "afsaf"
        if Student.objects.filter(email = mail).count() > 0:
            x = get_object_or_404(Student, email=mail).id
        if x != nsuID:
            raise forms.ValidationError("ID and email don't match")

    def clean_email(self):
        data = self.cleaned_data['email']
        std = Student.objects.filter(email = data)
        if Student.objects.filter(email = data).count() == 0:
            raise forms.ValidationError("Must be an official NorthSouth email address")
        return data

    def clean_nsu_id(self):
        data = self.cleaned_data['nsu_id']
        std = Student.objects.filter(email = data)
        if Student.objects.filter(id = data).count() == 0:
            raise forms.ValidationError("Must be a valid id")
        return data

    class Meta:
        model = User
        fields = ['username','nsu_id', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    def clean_email(self):
        data = self.cleaned_data['email']
        if Student.objects.filter(email = data).count() == 0:
            raise forms.ValidationError("Must be an official NorthSouth email address")
        return data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    def clean_nsu_id(self):
        data = self.cleaned_data['nsu_id']
        if Student.objects.filter(id = data).count() == 0:
            raise forms.ValidationError("Must be an official NSU student ID")
        return data

    def clean_fb_link(self):
        data = self.cleaned_data['fb_link']
        if "facebook.com/" not in data:   # any check you need
            raise forms.ValidationError("Must be your facebook profile link")
        return data

    class Meta:
        model = Profile
        fields = [
            'nsu_id',
            'status',
            'image',
            'bio',
            'fb_link',
            'insta_link',
            'git_link',
            'linkedin_link',
            'twitter_link',
        ]
