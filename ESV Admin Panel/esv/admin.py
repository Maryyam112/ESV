from django.contrib import admin

from esv.models import Feedback
from esv.models import Video

admin.site.site_title = 'ESV'
admin.site.site_header = 'ESV Admin Panel'
admin.site.register(Feedback)
admin.site.register(Video)

