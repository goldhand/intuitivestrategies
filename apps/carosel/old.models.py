from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField  
from imagekit.processors import ResizeToFill, Adjust
from mezzanine.pages.models import Page

from myproject.apps.author.models import Author

class Carosel(Author):
#	title			= models.CharField(max_length=50)
#	slug			= models.SlugField(unique=True)
#	description		= models.TextField()
#	authors			= models.ForeignKey(Author, null=True)
#	carosel_images		= models.ForeignKey('CaroselImage', null=True)

	def __unicode__(self):
		return self.slug


class CaroselImage(models.Model):
	image			= ProcessedImageField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(460, 300)], upload_to="{{ MEDIA_ROOT }}uploads", format='JPEG', options={'quality': 90})
	thumbnail		= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(220, 75)], image_field='image', cache_to='cache/thumbnails/', format='JPEG', options={'quality':90})
#	title			= models.CharField(max_length=50, null=True)
#	slug			= models.SlugField(null=True)
#	description		= models.TextField(null=True)
#	page			= models.ForeignKey(Author, null=True)
	carosels		= models.ForeignKey(Carosel, null=True)
#	carosel_pages		= models.ManyToManyField(Author, through=Carosel, null=True)
	

	def __unicode__(self):
		return self.slug


