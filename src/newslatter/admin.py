from django.contrib import admin
from newslatter.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'timestamp', 'update']

    class Meta:
        model = SignUp


admin.site.register(SignUp, SignUpAdmin)
