from django.utils.translation import ugettext_lazy as _
from django.db import models
from mezzanine.pages.models import Page
from mezzanine.blog.models import *
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust
from apps.tutorial.models import Tutorial


import datetime
import time
current_time = datetime.datetime.now().date()

def trendScore(post, ctime=current_time):
	pTime		= post.publish_date.date()
	pTimeDelta 	= ctime - pTime
	pRate		= post.rating_average*post.rating_count
	pScore		= pRate*(1-(pTimeDelta.days/200))
	if pScore <= 0:
		pScore = 1
	return pScore

def allBlogPosts():
	allPosts = []
	for post in BlogPost.objects.all():
		score = trendScore(post)
		allPosts.append((score, post))
	allPosts = sorted(allPosts, reverse=True)
	return allPosts

TRENDING_BLOGS = allBlogPosts()

class HomePage(Page):
	home_theme	= models.CharField(max_length=50)
	feat_tuts 	= models.ManyToManyField(Tutorial, blank=True)
	feat_blogs	= TRENDING_BLOGS[:10]
        class Meta:
                verbose_name = _("Home Page")
                verbose_name_plural = _("Home Pages")

	def __unicode__(self):
		return self.home_theme



class HomeSlides(models.Model):
        #returns images cropped for responsive design, l=large desktop, d=desktop, t=tablet, none=thumbnail     
        def re_img_span(span="1-12", display="ldt"):
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
        title           = models.CharField(max_length=100, null=True)
        slug            = models.SlugField(max_length=100, null=True)
        response_img    = models.ImageField(upload_to="responseimgs", null=True)
        description     = models.TextField(null=True)
	homepage	= models.ForeignKey(HomePage)	
	
	width = 8
	height = 350
        t = re_img_span(width, "t")
        d = re_img_span(width, "d")
        l = re_img_span(width, "l")

        limage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(l[0], height)], image_field='response_img', cache_to='cache/limage/', format='JPEG', options={'quality':90})
        dimage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(d[0], height)], image_field='response_img', cache_to='cache/dimage/', format='JPEG', options={'quality':90})
        timage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(t[0], height)], image_field='response_img', cache_to='cache/timage/', format='JPEG', options={'quality':90})
        thumbnail       = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(60, 60)], image_field='timage', cache_to='cache/thumbnails/', format='JPEG', options={'quality':90})

        def __unicode__(self):
                return self.slug





