from task.models import Task
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class createform(forms.ModelForm):
    title = forms.CharField(required=False)
    """user=forms.CharField(widget=forms.HiddenInput(),initial='value')
    title = forms.CharField(max_length=50)
    discription = forms.TimeField()
    complete=forms.BooleanField()"""

    class Meta:
        model=Task
        fields=('title','discription')

    """def __init__(self, *args, **kwargs):
        super(createform, self).__init__(*args, **kwargs)
        self.fields['title'].required = False"""


class SighnUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","password1","password2")
    def save(self,commit=True):
        user=super().save(commit=commit)
        Profile.objects.create(user=user)
        return user