from django.db import models
from mezzanine.pages.models import Page
#from apps.carosel.models import Carosel


class Author(Page):
	#page_carosel	= models.ForeignKey('Carosel', null=True)
	dob		= models.DateTimeField()

	def can_add(self, request):
		return self.children.count() == 0

	def can_delete(self, request):
		return request.user.is_superuser or self.parent is not None


class Book(models.Model):

	author		= models.ForeignKey("Author")
	cover		= models.ImageField(upload_to="authors")
