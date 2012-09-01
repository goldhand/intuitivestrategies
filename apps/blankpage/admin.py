from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *

splash_extra_fieldsets = ((None, {"fields": ("splash_page",)}),)


class SplashAdmin(PageAdmin):
	fieldsets = deepcopy(PageAdmin.fieldsets) + splash_extra_fieldsets
admin.site.register(Splash, SplashAdmin)
