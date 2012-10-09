from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from mezzanine.pages.models import Page


def re_img_span(span="1-12", display="ldt"):
	#returns images cropped for responsive design, l=large desktop, d=desktop, t=tablet, none=thumbnail     
	if display == "l":
        	div = 70
        	margin = 30
        elif display == "d":
                div = 60
                margin = 20
        elif display == "t":
                div = 42
                margin = 20
        else:
                return (60, 60)
        w = (span*(div+margin)-margin)
        if span <= 3:
                h = (w*1.2)
        else:
                h = (w*0.6)
        return w, int(round(h))

class CompanyProfile(Page):
	company_title		= models.CharField(max_length=100, null=True, blank=True)
	about			= models.TextField(null=True, blank=True)

	t = re_img_span(9, "t")
	d = re_img_span(9, "d")
	l = re_img_span(9, "l")
	profile_image		= models.ImageField(upload_to="companyprofile", default="home/will/Workspace/django/mezzanine/myproject/static/img/bg_blue.gif")
	limage		= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(l[0], 220)], image_field='profile_image', cache_to='cache/limage/', format='JPEG', options={'quality':90})
	dimage		= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(d[0], 220)], image_field='profile_image', cache_to='cache/dimage/', format='JPEG', options={'quality':90})
	timage		= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(t[0], 220)], image_field='profile_image', cache_to='cache/timage/', format='JPEG', options={'quality':90})


	website		= models.URLField(max_length=100, null=True, blank=True)
	

class UserProfile(models.Model):

	t = re_img_span(2, "t")
	d = re_img_span(2, "d")
	l = re_img_span(2, "l")

	user 		= models.OneToOneField(User, null=True)
	alias		= models.CharField(max_length=100)
	tagline		= models.CharField(max_length=200, help_text="make it short and catchy!", null=True, blank=True)
	about_me	= models.TextField(null=True, blank=True)

	profile_image	= models.ImageField(upload_to="userprofile", null=True, blank=True)

	limage		= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(l[0], 220)], image_field='profile_image', cache_to='cache/limage/', format='JPEG', options={'quality':90})
	dimage		= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(d[0], 220)], image_field='profile_image', cache_to='cache/dimage/', format='JPEG', options={'quality':90})
	timage		= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(t[0], 220)], image_field='profile_image', cache_to='cache/timage/', format='JPEG', options={'quality':90})
	lthumbnail	= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(90, 70)], image_field='limage', cache_to='cache/lthumbnail/', format='JPEG', options={'quality':90})
	thumbnail	= ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(30, 30)], image_field='limage', cache_to='cache/thumbnails/', format='JPEG', options={'quality':90})

	facebook	= models.CharField(max_length=100, verbose_name="facebook    www.facebook.com/*", null=True, blank=True)
	twitter		= models.CharField(max_length=50, verbose_name="twitter    @*", null=True, blank=True)
	google_plus	= models.CharField(max_length=100, help_text="enter the number sequence on in the url bar on your g+ profile page", verbose_name="google plus    www.plus.google.com/*", null=True, blank=True)
	linkedin	= models.CharField(max_length=100, verbose_name="linkedin    www.linkedin.com/*", null=True, blank=True)
	youtube		= models.CharField(max_length=100, verbose_name="youtube    www.youtube.com/*", null=True, blank=True)

	companyprofile	= models.ForeignKey(CompanyProfile, null=True, blank=True)
	position_title	= models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return self.alias


def create_userprofile_user_callback(sender, instance, **kwargs):
	userprofile, new = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_userprofile_user_callback, User)


