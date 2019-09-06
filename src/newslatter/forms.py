import re
from django import forms
from newslatter.models import SignUp


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['email', 'full_name']

    def clean_email(self):
        email = self.data.get('email')
        if not re.match(r'[a-zA-Z][\w]{4,32}@[a-z\d]{3,}([.]+[a-z0-9]{2,})+', email):
            return forms.ValidationError('Email format error.')
        instance = SignUp.objects.filter(email=email)
        if instance.exists():
            return forms.ValidationError('Email has already benn used.')
        return email
