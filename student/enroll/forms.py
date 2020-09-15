from django import forms
from .models import Data

class login(forms.ModelForm):
    class Meta:
        model=Data
        fields=['Name','Email','Password']

        widgets={'Password':forms.PasswordInput(render_value=True)}