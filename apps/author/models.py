from django.db import models
from mezzanine.pages.models import Page
#from apps.carosel.models import Carosel


class Author(Page):
	#page_carosel	= models.ForeignKey('Carosel', null=True)
	dob		= models.DateTimeField()


class Book(models.Model):

	author		= models.ForeignKey("Author")
	cover		= models.ImageField(upload_to="authors")
