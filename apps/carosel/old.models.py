from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust
#from mezzanine.pages.models import Page
from apps.author.models import Author


class CaroselImage(models.Model):
        image                   = ProcessedImageField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(460, 300)], upload_to="{{ MEDIA_ROOT }}uploads", format='JPEG', options={'quality': 90})
        thumbnail               = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(220, 75)], image_field='image', cache_to='cache/thumbnails/', format='JPEG', options={'quality':90})
	author          = models.ForeignKey(Author)


