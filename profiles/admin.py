from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Profile)

class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio',)
