from django.contrib import admin
from .models import Feedback, Videos

admin.site.site_header = 'ESV Admin Panel'
admin.site.register(Feedback)(admin.ModelAdmin)
admin.site.register(Videos)(admin.ModelAdmin)
