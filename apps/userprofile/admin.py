from django.contrib import admin
from apps.userprofile.models import UserProfile, CompanyProfile
from copy import deepcopy
from imagekit.admin import AdminThumbnail
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import TabularDynamicInlineAdmin



class UserProfileAdmin(admin.ModelAdmin):
        list_display = ('__str__', 'admin_thumbnail')
        admin_thumbnail = AdminThumbnail(image_field='thumbnail')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CompanyProfile)
