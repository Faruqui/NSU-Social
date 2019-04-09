from django import forms
from . import models
from groups.models import Group, GroupMember
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("group", "message")
        model = models.Post

    def clean(self):
        cleaned_data = super().clean()
        grp_name = cleaned_data.get('group')

        if Group.objects.filter(members = User).count() == 0:
            raise forms.ValidationError("You are not in this group")
