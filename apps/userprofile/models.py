from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_facebook.models import FacebookProfileModel


class UserProfile(FacebookProfileModel):
	user 		= models.OneToOneField(User)
	name		= models.CharField(max_length=100)	
	user_image		= ProcessedImageField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(100, 110)], upload_to="uploads", format='JPEG', options={'quality': 90})
	thumbnail	= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(60, 60)], image_field='image', cache_to='cache/thumbnails/', format='JPEG', options={'quality':90})

	def __unicode__(self):
		return self.name

def create_userprofile_user_callback(sender, instance, created, **kwargs):
	userprofile, new = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_userprofile_user_callback, sender=User)
