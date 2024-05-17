from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'favorite_team']
        widgets = {
            'favorite_team': forms.RadioSelect()
        }
