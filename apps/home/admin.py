from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import *


home_extra_fieldsets = ((None, {"fields": ("home_theme", "feat_tuts")}),)

class HomeSlidesInline(TabularDynamicInlineAdmin):
	model = HomeSlides

class HomePageAdmin(PageAdmin):
	inlines = (HomeSlidesInline,)
	fieldsets = deepcopy(PageAdmin.fieldsets) + home_extra_fieldsets

admin.site.register(HomePage, HomePageAdmin)

