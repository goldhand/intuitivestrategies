from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import *
from apps.carosel.models import CaroselImage 


author_extra_fieldsets = ((None, {"fields": ("dob",)}),)


class CaroselImageInline(admin.TabularInline):
	model = CaroselImage

class BookInline(admin.TabularInline):
	model = Book

class AuthorAdmin(PageAdmin):
	inlines = (BookInline, CaroselImageInline)
	fieldsets = deepcopy(PageAdmin.fieldsets) + author_extra_fieldsets

admin.site.register(Author, AuthorAdmin)

