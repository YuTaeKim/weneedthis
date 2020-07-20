from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Idea,Comment,Feedback

admin.site.register(User)
admin.site.register(Idea)
admin.site.register(Comment)
admin.site.register(Feedback)
