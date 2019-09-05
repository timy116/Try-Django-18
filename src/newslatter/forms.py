from django import forms
from newslatter.models import SignUp


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['email', 'full_name']
