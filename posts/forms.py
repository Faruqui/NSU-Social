from django import forms
from . import models
from groups.models import Group, GroupMember


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("group", "message")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (
                models.Group.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )

    def clean(self):
        cleaned_data = super().clean()
        grp_name = cleaned_data.get('group')
        msg = cleaned_data.get('message')
        grp = Group.objects.filter(name = grp_name)

        if user not in grp.members.all:
            raise forms.ValidationError("You are not in this group!!")
