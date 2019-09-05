import re
from django import forms
from newslatter.models import SignUp


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

    def clean_email(self):
        email = self.data.get('email')
        if not re.match(r'[a-z][\w]{5,32}@[a-z\d]{2,}([\.]{1,}[a-z0-9]{2,}){1,}', email):
            return forms.ValidationError('Email format error.')
        return email
