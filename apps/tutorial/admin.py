from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import *


tutorial_extra_fieldsets = ((None, {"fields": ("categories", "allow_comments", "position", "image", "content",)}),)

class SectionInline(TabularDynamicInlineAdmin):
	model = Section

class TutorialAdmin(PageAdmin):
	inlines = (SectionInline,)
	fieldsets = deepcopy(PageAdmin.fieldsets) + tutorial_extra_fieldsets

admin.site.register(Tutorial, TutorialAdmin)

