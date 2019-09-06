from django.contrib import admin
from newsletter.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'timestamp', 'update']

    class Meta:
        model = SignUp


admin.site.register(SignUp, SignUpAdmin)
