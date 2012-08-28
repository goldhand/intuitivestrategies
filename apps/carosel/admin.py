from copy import deepcopy
from django.contrib import admin
from .models import CaroselImage
from imagekit.admin import AdminThumbnail
from mezzanine.pages.admin import PageAdmin


#class CaroselImageInline(admin.TabularInline):
#	model = CaroselImage
#	list_display = ('__str__', 'admin_thumbnail')
#	admin_thumbnail = AdminThumbnail(image_field='thumbnail')
#	prepopulated_fields = {'slug':('title',)}


class CaroselImageAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'admin_thumbnail')
	admin_thumbnail = AdminThumbnail(image_field='thumbnail')
#	prepopulated_fields = {'slug':('title',)}



#class CaroselAdmin(PageAdmin):
#	inlines = (CaroselImageInline,)
#	prepopulated_fields = {'slug':('title',)}


#admin.site.register(Carosel, CaroselAdmin)
admin.site.register(CaroselImage, CaroselImageAdmin)

