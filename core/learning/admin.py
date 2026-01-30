from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Course, Module, Enrollment

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Enrollment)
