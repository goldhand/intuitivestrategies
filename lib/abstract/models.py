from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust

def span12():
	s = 1
	spanlist = []
	for spanx in range(1, 13):
		spanlist.append((str(s), ('span'+str(s))))
		s += 1
	return spanlist

SPAN_CHOICES = span12()

class ResponseImage(models.Model):
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
	title 		= models.CharField(max_length=100, null=True)
	slug		= models.SlugField(max_length=100, null=True)
	width		= models.CharField(max_length=10, choices=SPAN_CHOICES, null=True)
	height		= models.IntegerField(null=True)
	response_img	= models.ImageField(upload_to="responseimgs", null=True)
	description	= models.TextField(null=True)

	t = re_img_span(width, "t")
        d = re_img_span(width, "d")
        l = re_img_span(width, "l")
	
	limage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(l[0], height)], image_field='response_img', cache_to='cache/limage/', format='JPEG', options={'quality':90})
        dimage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(d[0], height)], image_field='response_img', cache_to='cache/dimage/', format='JPEG', options={'quality':90})
        timage          = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(t[0], height)], image_field='response_img', cache_to='cache/timage/', format='JPEG', options={'quality':90})
        thumbnail       = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(60, 60)], image_field='timage', cache_to='cache/thumbnails/', format='JPEG', options={'quality':90})

	def __unicode__(self):
		return self.slug



