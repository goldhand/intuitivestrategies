from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *


uploadfile_extra_fieldsets = ((None, {"fields": ("content",)}),)


class UploadFileAdmin(PageAdmin):
        fieldsets = deepcopy(PageAdmin.fieldsets) + uploadfile_extra_fieldsets

admin.site.register(UploadFile, UploadFileAdmin)

