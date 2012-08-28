from django.contrib import admin
from apps.userprofile.models import UserProfile
from copy import deepcopy
from imagekit.admin import AdminThumbnail
from mezzanine.pages.admin import PageAdmin


class UserProfileAdmin(admin.ModelAdmin):
        list_display = ('__str__', 'admin_thumbnail')
        admin_thumbnail = AdminThumbnail(image_field='thumbnail')

admin.site.register(UserProfile, UserProfileAdmin)
