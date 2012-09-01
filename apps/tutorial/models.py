from django.db import models
from mezzanine.pages.models import Page
from mezzanine.blog.models import BlogCategory
from mezzanine.generic.fields import CommentsField, RatingField
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust


class Tutorial(Page):
	categories 	= models.ManyToManyField(BlogCategory, verbose_name=_("Categories"), blank=True, related_name="tutorials")
	allow_comments 	= models.BooleanField(verbose_name=_("Allow comments"), default=True)
	comments 	= CommentsField(verbose_name=_("Comments"))
	rating 		= RatingField(verbose_name=_("Rating"))

	position	= models.IntegerField(help_text="The position to order on menu")
        image                   = ProcessedImageField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(460, 300)], upload_to="uploads", format='JPEG', options={'quality': 90})
	content		= models.TextField()

	class Meta:
	        verbose_name = _("Tutorial")
	        verbose_name_plural = _("Tutorials")
        	ordering = ("position",)


class Section(models.Model):
	title		= models.CharField(max_length=100)
	position	= models.IntegerField(help_text="The position to order on menu")
	content		= models.TextField()
	tutorial	= models.ForeignKey(Tutorial)
